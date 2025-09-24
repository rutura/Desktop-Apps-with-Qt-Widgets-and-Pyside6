from PySide6.QtCore import Qt, QAbstractTableModel, QModelIndex
from PySide6.QtGui import QPixmap
import json
from inventoryitem import InventoryItem
from PySide6.QtCore import QDateTime
import os

class InventoryModel(QAbstractTableModel):
    # Column enum
    ProductName = 0
    Quantity = 1
    Supplier = 2
    ProductImage = 3
    Rating = 4
    ColumnCount = 5

    def __init__(self, parent=None):
        super().__init__(parent)
        self.items = []
        self.supplierList = []

    def rowCount(self, parent=QModelIndex()):
        if parent.isValid():
            return 0
        return len(self.items)

    def columnCount(self, parent=QModelIndex()):
        if parent.isValid():
            return 0
        return self.ColumnCount

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid() or index.row() >= len(self.items):
            return None

        item = self.items[index.row()]

        if role in (Qt.DisplayRole, Qt.EditRole):
            if index.column() == self.ProductName:
                return item.productName
            elif index.column() == self.Quantity:
                return item.quantity
            elif index.column() == self.Supplier:
                return item.supplier
            elif index.column() == self.ProductImage:
                return item.imagePath
            elif index.column() == self.Rating:
                return item.rating
        elif role == Qt.DecorationRole and index.column() == self.ProductImage:
            if not item.image.isNull():
                return item.image.scaled(64, 64, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        elif role == Qt.ToolTipRole:
            if index.column() == self.ProductName:
                return item.description
            elif index.column() == self.ProductImage:
                return "Double-click to change image"

        return None

    def setData(self, index, value, role=Qt.EditRole):
        if not index.isValid() or index.row() >= len(self.items):
            return False

        if role == Qt.EditRole:
            item = self.items[index.row()]
            changed = False

            if index.column() == self.ProductName:
                if (value != item.productName and value and 
                    self.isProductNameUnique(value, index.row())):
                    item.productName = value
                    changed = True
            elif index.column() == self.Quantity:
                item.quantity = int(value)
                changed = True
            elif index.column() == self.Supplier:
                item.supplier = value
                changed = True
            elif index.column() == self.ProductImage:
                item.imagePath = value
                if value:
                    item.image = QPixmap(value)
                else:
                    item.image = QPixmap()
                changed = True
            elif index.column() == self.Rating:
                item.rating = int(value)
                changed = True

            if changed:
                item.lastUpdated = QDateTime.currentDateTime()
                self.dataChanged.emit(index, index)
                return True

        return False

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role != Qt.DisplayRole or orientation != Qt.Horizontal:
            return None

        headers = {
            self.ProductName: "Product Name",
            self.Quantity: "Quantity",
            self.Supplier: "Supplier",
            self.ProductImage: "Image",
            self.Rating: "Rating"
        }
        return headers.get(section)

    def flags(self, index):
        if not index.isValid():
            return Qt.NoItemFlags

        return Qt.ItemIsEditable | Qt.ItemIsEnabled | Qt.ItemIsSelectable

    def addItem(self, item):
        if not item.productName or not self.isProductNameUnique(item.productName):
            return False

        self.beginInsertRows(QModelIndex(), len(self.items), len(self.items))
        self.items.append(item)
        self.endInsertRows()
        return True

    def removeItem(self, row):
        if row < 0 or row >= len(self.items):
            return False

        # Delete the image file if it exists
        if self.items[row].imagePath:
            try:
                os.remove(self.items[row].imagePath)
            except:
                pass  # Ignore file deletion errors

        self.beginRemoveRows(QModelIndex(), row, row)
        self.items.pop(row)
        self.endRemoveRows()
        return True

    def updateItem(self, row, item):
        if row < 0 or row >= len(self.items):
            return False

        if (item.productName != self.items[row].productName and
            not self.isProductNameUnique(item.productName, row)):
            return False

        self.items[row] = item
        self.dataChanged.emit(
            self.index(row, 0), 
            self.index(row, self.ColumnCount - 1)
        )
        return True

    def getItem(self, row):
        return self.items[row]

    def saveToFile(self, filename):
        try:
            items_data = []
            for item in self.items:
                item_dict = {
                    "productName": item.productName,
                    "quantity": item.quantity,
                    "supplier": item.supplier,
                    "imagePath": item.imagePath,
                    "rating": item.rating,
                    "description": item.description,
                    "lastUpdated": item.lastUpdated.toString(Qt.ISODate)
                }
                items_data.append(item_dict)

            with open(filename, 'w', encoding='utf-8') as f:
                json.dump({"items": items_data, "suppliers": self.supplierList}, f, indent=2)
            return True
        except:
            return False

    def loadFromFile(self, filename):
        try:
            if not os.path.exists(filename):
                return False

            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)

            self.beginResetModel()
            self.items.clear()

            for item_data in data.get("items", []):
                item = InventoryItem()
                item.productName = item_data["productName"]
                item.quantity = item_data["quantity"]
                item.supplier = item_data["supplier"]
                item.imagePath = item_data["imagePath"]
                if item.imagePath:
                    item.image = QPixmap(item.imagePath)
                item.rating = item_data["rating"]
                item.description = item_data["description"]
                item.lastUpdated = QDateTime.fromString(item_data["lastUpdated"], Qt.ISODate)
                self.items.append(item)

            self.supplierList = data.get("suppliers", [])
            self.endResetModel()
            return True
        except:
            return False

    def isProductNameUnique(self, name, excludeRow=-1):
        for i, item in enumerate(self.items):
            if i != excludeRow and item.productName == name:
                return False
        return True

    def setSupplierList(self, suppliers):
        self.supplierList = suppliers

    def getSupplierList(self):
        return self.supplierList
