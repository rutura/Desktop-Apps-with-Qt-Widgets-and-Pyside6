from PySide6.QtWidgets import (QWidget, QLabel, QTextEdit, QPushButton,
                               QVBoxLayout, QFormLayout, QFileDialog, QMessageBox)
from PySide6.QtCore import Signal, Qt, QDateTime
from PySide6.QtGui import QPixmap
import os
from inventoryitem import InventoryItem

class ProductDetailsWidget(QWidget):
    imageChanged = Signal(str)
    descriptionChanged = Signal(str)
    detailsChanged = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()
        self.currentImagePath = ""

    def setupUi(self):
        mainLayout = QVBoxLayout(self)
        
        # Image section
        self.imageLabel = QLabel(self)
        self.imageLabel.setMinimumSize(300, 300)
        self.imageLabel.setAlignment(Qt.AlignCenter)
        self.imageLabel.setStyleSheet("QLabel { background-color: #f0f0f0; border: 1px solid #ddd; }")
        mainLayout.addWidget(self.imageLabel)

        self.changeImageButton = QPushButton("Change Image", self)
        mainLayout.addWidget(self.changeImageButton)

        # Details section
        formLayout = QFormLayout()
        self.productNameLabel = QLabel(self)
        self.quantityLabel = QLabel(self)
        self.supplierLabel = QLabel(self)
        self.ratingLabel = QLabel(self)
        
        formLayout.addRow("Product:", self.productNameLabel)
        formLayout.addRow("Quantity:", self.quantityLabel)
        formLayout.addRow("Supplier:", self.supplierLabel)
        formLayout.addRow("Rating:", self.ratingLabel)

        mainLayout.addLayout(formLayout)

        # Description section
        mainLayout.addWidget(QLabel("Description:", self))
        self.descriptionEdit = QTextEdit(self)
        mainLayout.addWidget(self.descriptionEdit)

        # Connect signals
        self.changeImageButton.clicked.connect(self.onChangeImage)
        self.descriptionEdit.textChanged.connect(
            lambda: self.descriptionChanged.emit(self.descriptionEdit.toPlainText())
        )

    def setItem(self, item):
        self.productNameLabel.setText(item.productName)
        self.quantityLabel.setText(str(item.quantity))
        self.supplierLabel.setText(item.supplier)
        
        ratingText = "★" * item.rating + "☆" * (5 - item.rating)
        self.ratingLabel.setText(ratingText)
        
        if not item.image.isNull():
            scaled = item.image.scaled(300, 300, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.imageLabel.setPixmap(scaled)
        else:
            self.imageLabel.setText("No Image")
        
        self.currentImagePath = item.imagePath
        self.descriptionEdit.setText(item.description)

    def clearDetails(self):
        self.imageLabel.clear()
        self.imageLabel.setText("No Item Selected")
        self.productNameLabel.clear()
        self.quantityLabel.clear()
        self.supplierLabel.clear()
        self.ratingLabel.clear()
        self.descriptionEdit.clear()
        self.currentImagePath = ""

    def onChangeImage(self):
        fileName, _ = QFileDialog.getOpenFileName(
            self, "Select Image", "", "Images (*.png *.jpg *.jpeg)")
        
        if fileName:
            self.saveImageToDataFolder(fileName)

    def saveImageToDataFolder(self, sourcePath):
        dataDir = os.path.join(os.getcwd(), "data", "images")
        os.makedirs(dataDir, exist_ok=True)

        sourceFile = os.path.basename(sourcePath)
        newFileName = f"{QDateTime.currentDateTime().toString('yyyyMMddhhmmss')}_{sourceFile}"
        newPath = os.path.join(dataDir, newFileName)

        if os.path.exists(sourcePath):
            try:
                # Copy the file
                with open(sourcePath, 'rb') as src, open(newPath, 'wb') as dst:
                    dst.write(src.read())
                
                newImage = QPixmap(newPath)
                if not newImage.isNull():
                    scaled = newImage.scaled(300, 300, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                    self.imageLabel.setPixmap(scaled)
                    self.imageChanged.emit(newPath)
                else:
                    QMessageBox.warning(self, "Error", "Failed to load the new image.")
            except Exception as e:
                QMessageBox.warning(self, "Error", f"Failed to save image: {str(e)}")
        else:
            QMessageBox.warning(self, "Error", "Source image file not found.")
