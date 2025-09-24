from PySide6.QtCore import QDateTime
from PySide6.QtGui import QPixmap

class InventoryItem:
    def __init__(self):
        self.productName = ""
        self.quantity = 0
        self.supplier = ""
        self.imagePath = ""
        self.image = QPixmap()
        self.rating = 0  # 1-5 stars
        self.description = ""
        self.lastUpdated = QDateTime.currentDateTime()
