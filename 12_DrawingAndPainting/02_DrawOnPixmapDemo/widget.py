from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPixmap, QPainter, QPen, QFont, QBrush
from PySide6.QtCore import Qt, QSize
from ui_widget import Ui_Widget

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        
        # Set minimum and maximum size constraints
        self.setMinimumSize(400, 300)
        self.setMaximumWidth(800)
        self.resize(500, 400)
        
        # Prevent label from expanding widget
        self.ui.label.setScaledContents(False)
        
        # Initial draw
        self.drawPixmap()
    
    def drawPixmap(self):
        """Draw the pixmap based on current widget size"""
        # Create pixmap with size based on widget dimensions (with margin)
        width = self.width() - 20
        height = self.height() - 20
        
        mPix = QPixmap(width, height)
        mPix.fill(Qt.gray)
        
        # Configure pen, brush, and font
        pen = QPen()
        pen.setWidth(5)
        pen.setColor(Qt.white)
        
        mFont = QFont("Consolas", 20, QFont.Bold)
        
        # Create painter for the pixmap
        painter = QPainter(mPix)
        painter.setPen(pen)
        painter.setBrush(Qt.green)
        painter.setFont(mFont)
        
        # Draw a rectangle around the pixmap's border
        painter.drawRect(mPix.rect())
        
        # Change brush color and draw another rectangle
        painter.setBrush(Qt.blue)
        painter.drawRect(50, 50, 100, 100)
        
        # Draw some text
        painter.drawText(30, 120, "I'm loving Qt")
        
        # Print debug information about the painter's coordinate systems
        print(f"Painter window (logical): {painter.window()}")
        print(f"Painter viewPort (physical): {painter.viewport()}")
        
        # End painting
        painter.end()
        
        # Set the pixmap to the label
        self.ui.label.setPixmap(mPix)
    
    def resizeEvent(self, event):
        """Handle resize events to redraw the pixmap"""
        self.drawPixmap()
        super().resizeEvent(event)