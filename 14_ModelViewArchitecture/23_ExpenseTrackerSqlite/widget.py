from PySide6.QtWidgets import (QWidget, QInputDialog, QMessageBox, 
                             QHeaderView, QApplication)
from PySide6.QtCore import QDate, Qt, QFile, QIODevice
from expense import Expense
from expensemodel import ExpenseModel
from expenseproxymodel import ExpenseProxyModel
from PySide6.QtUiTools import QUiLoader


class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        # Load UI from .ui file
        ui_file_path = "widget.ui"
        
        # Load the UI file using loadUiType
        from PySide6.QtUiTools import loadUiType
        
        # Load the UI file
        UI_Form, _ = loadUiType(ui_file_path)
        
        # Set up the UI
        self.ui = UI_Form()
        self.ui.setupUi(self)
        
        # Set up the model
        self.model = ExpenseModel(self)
        
        # Set up proxy model
        self.proxy_model = ExpenseProxyModel(self)
        self.proxy_model.setSourceModel(self.model)
        self.proxy_model.setFilterCaseSensitivity(Qt.CaseInsensitive)
        
        # Set up table view
        self.ui.tableView.setModel(self.proxy_model)
        self.ui.tableView.resizeColumnsToContents()
        self.ui.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableView.setSortingEnabled(True)
        
        # Initialize filter column combo box
        self.ui.filterColumnComboBox.addItems(["All Columns", "Date", "Item", "Amount", "Category"])
        
        # Connect signals and slots
        self.ui.addExpenseButton.clicked.connect(self.on_addExpenseButton_clicked)
        self.ui.removeExpenseButton.clicked.connect(self.on_removeExpenseButton_clicked)
        self.ui.filterLineEdit.textChanged.connect(self.on_filterLineEdit_textChanged)
        self.ui.filterColumnComboBox.currentIndexChanged.connect(self.on_filterColumnComboBox_currentIndexChanged)
    
    def on_addExpenseButton_clicked(self):
        item, ok = QInputDialog.getText(self, "Add Expense", 
                                       "Item name:", text="Coffee")
        if ok and item:
            amount, ok = QInputDialog.getDouble(self, "Add Expense", 
                                              "Amount:", 0.00, 0.00, 1000000.00, 2)
            if ok:
                category, ok = QInputDialog.getText(self, "Add Expense", 
                                                  "Category:", text="Food")
                if ok and category:
                    expense = Expense(QDate.currentDate(), item, amount, category, self.model)
                    self.model.addExpense(expense)
    
    def on_removeExpenseButton_clicked(self):
        proxy_index = self.ui.tableView.currentIndex()
        if proxy_index.isValid():
            source_index = self.proxy_model.mapToSource(proxy_index)
            self.model.removeExpense(source_index)
        else:
            QMessageBox.warning(self, "Remove Expense", "Please select an expense to remove.")
    
    def on_filterLineEdit_textChanged(self, text):
        column = self.ui.filterColumnComboBox.currentIndex() - 1  # -1 because first item is "All Columns"
        if column == -1:
            self.proxy_model.setFilterKeyColumn(-1)  # Search all columns
        else:
            self.proxy_model.setFilterKeyColumn(column)
        self.proxy_model.setFilterFixedString(text)
    
    def on_filterColumnComboBox_currentIndexChanged(self, index):
        self.on_filterLineEdit_textChanged(self.ui.filterLineEdit.text())
