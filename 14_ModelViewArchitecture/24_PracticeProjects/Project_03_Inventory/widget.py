from PySide6.QtWidgets import (QWidget, QVBoxLayout, QMessageBox,
                               QInputDialog, QHeaderView, QSplitter)
from PySide6.QtCore import Qt, Slot, QDir
import os
from ui_widget import Ui_Widget
from inventorymodel import InventoryModel
from inventorydelegates import ImageDelegate, RatingDelegate, SupplierDelegate
from productdetailswidget import ProductDetailsWidget
from inventoryitem import InventoryItem

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        # Set up data directory
        dataDir = QDir.current()
        if not dataDir.exists("data"):
            dataDir.mkdir("data")
        if not dataDir.exists("data/images"):
            dataDir.mkdir("data/images")
        self.dataFilePath = dataDir.filePath("data/inventory.json")

        self.setupModel()
        self.setupConnections()
        self.loadData()
        self.setupDelegates()

    def setupModel(self):
        self.model = InventoryModel(self)
        self.ui.inventoryTableView.setModel(self.model)
        
        # Configure table view
        header = self.ui.inventoryTableView.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Interactive)
        self.ui.inventoryTableView.verticalHeader().setDefaultSectionSize(64)  # For thumbnails
        self.ui.inventoryTableView.setSelectionBehavior(QHeaderView.SelectRows)
        self.ui.inventoryTableView.setSelectionMode(QHeaderView.SingleSelection)
        
        # Create splitter for master-detail view
        splitter = QSplitter(Qt.Horizontal, self)
        splitter.addWidget(self.ui.mainFrame)  # Contains table and buttons
        
        self.detailsWidget = ProductDetailsWidget(self)
        splitter.addWidget(self.detailsWidget)
        
        # Set initial sizes - 60% for table, 40% for details
        splitter.setSizes([600, 400])
        
        # Update layout
        if self.layout():
            QWidget().setLayout(self.layout())
        mainLayout = QVBoxLayout(self)
        mainLayout.addWidget(splitter)
        self.setLayout(mainLayout)

    def setupDelegates(self):
        self.imageDelegate = ImageDelegate(self)
        self.ratingDelegate = RatingDelegate(self)
        self.supplierDelegate = SupplierDelegate(self.model.getSupplierList(), self)

        self.ui.inventoryTableView.setItemDelegateForColumn(InventoryModel.ProductImage, self.imageDelegate)
        self.ui.inventoryTableView.setItemDelegateForColumn(InventoryModel.Rating, self.ratingDelegate)
        self.ui.inventoryTableView.setItemDelegateForColumn(InventoryModel.Supplier, self.supplierDelegate)

    def setupConnections(self):
        self.ui.addButton.clicked.connect(self.onAddItem)
        self.ui.editButton.clicked.connect(self.onEditItem)
        self.ui.deleteButton.clicked.connect(self.onDeleteItem)
        self.ui.manageSuppliersButton.clicked.connect(self.onManageSuppliers)
        self.ui.searchLineEdit.textChanged.connect(self.onSearchTextChanged)
        
        # Connect selection changes to update details panel
        selection_model = self.ui.inventoryTableView.selectionModel()
        selection_model.currentRowChanged.connect(self.onSelectionChanged)
        
        # Connect details panel signals
        self.detailsWidget.imageChanged.connect(self.onImageChanged)
        self.detailsWidget.descriptionChanged.connect(self.onDescriptionChanged)

    @Slot(str)
    def onSearchTextChanged(self, text):
        # TODO: Implement search functionality
        pass

    @Slot()
    def onSelectionChanged(self, current, previous):
        if current.isValid():
            item = self.model.getItem(current.row())
            self.detailsWidget.setItem(item)
        else:
            self.detailsWidget.clearDetails()

    @Slot(str)
    def onImageChanged(self, newPath):
        index = self.ui.inventoryTableView.currentIndex()
        if index.isValid():
            self.model.setData(
                self.model.index(index.row(), InventoryModel.ProductImage),
                newPath
            )

    @Slot(str)
    def onDescriptionChanged(self, newDescription):
        index = self.ui.inventoryTableView.currentIndex()
        if index.isValid():
            item = self.model.getItem(index.row())
            item.description = newDescription
            self.model.updateItem(index.row(), item)

    def loadData(self):
        if self.model.loadFromFile(self.dataFilePath):
            print(f"Data loaded successfully from {self.dataFilePath}")
            if self.ui.inventoryTableView.model().rowCount() > 0:
                self.ui.inventoryTableView.setCurrentIndex(self.model.index(0, 0))

    def saveData(self):
        if not self.model.saveToFile(self.dataFilePath):
            print(f"Failed to save data to {self.dataFilePath}")

    @Slot()
    def onAddItem(self):
        productName, ok = QInputDialog.getText(self, "Add Item", "Product Name:")
        if not ok or not productName:
            return

        if not self.model.isProductNameUnique(productName):
            QMessageBox.warning(self, "Error", "A product with this name already exists.")
            return
        
        # Make sure supplier delegate has latest supplier list
        self.supplierDelegate.setSuppliers(self.model.getSupplierList())

        item = InventoryItem()
        item.productName = productName
        item.quantity = 0
        item.supplier = self.model.getSupplierList()[0] if self.model.getSupplierList() else ""
        item.rating = 0
        item.description = "Enter product description here..."

        if self.model.addItem(item):
            lastRow = self.model.rowCount() - 1
            self.ui.inventoryTableView.setCurrentIndex(self.model.index(lastRow, 0))

    @Slot()
    def onEditItem(self):
        index = self.ui.inventoryTableView.currentIndex()
        if not index.isValid():
            QMessageBox.warning(self, "Error", "Please select an item to edit.")
            return

        self.ui.inventoryTableView.edit(index)

    @Slot()
    def onDeleteItem(self):
        index = self.ui.inventoryTableView.currentIndex()
        if not index.isValid():
            QMessageBox.warning(self, "Error", "Please select an item to delete.")
            return

        reply = QMessageBox.question(
            self, "Confirm Delete", 
            "Are you sure you want to delete this item?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )
        
        if reply == QMessageBox.Yes:
            self.model.removeItem(index.row())
            self.detailsWidget.clearDetails()

    @Slot()
    def onManageSuppliers(self):
        suppliers = self.model.getSupplierList()
        text, ok = QInputDialog.getText(
            self,
            "Manage Suppliers",
            "Enter supplier names (comma-separated):",
            text=",".join(suppliers)
        )
        
        if ok:
            newSuppliers = [s.strip() for s in text.split(",") if s.strip()]
            self.model.setSupplierList(newSuppliers)
            self.supplierDelegate.setSuppliers(newSuppliers)

    def closeEvent(self, event):
        self.saveData()
        super().closeEvent(event)
