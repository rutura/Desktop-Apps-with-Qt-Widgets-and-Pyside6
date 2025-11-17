from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt, Signal, QSize, QPoint
from PySide6.QtGui import QPainter, QMouseEvent, QPaintEvent, QPolygon, QBrush

class StarEditor(QWidget):

    # Define the sigbnal for when editing is finished
    editingFinished = Signal()

    def __init__(self, parent = None):
        super().__init__(parent)

        # Enable mouse tracking
        self.setMouseTracking(True)

        # Set up the polygon shape
        self.poly = QPolygon()
        self.poly << QPoint(0, 85) <<  QPoint(75, 75) \
                 << QPoint(100, 10) << QPoint(125, 75) \
                 << QPoint(200, 85) << QPoint(150, 125) \
                 << QPoint(160, 190) << QPoint(100, 150) \
                 << QPoint(40, 190) << QPoint(50, 125) \
                 << QPoint(0, 85)

        # Initialize the star rating as an integer
        self.starRating = 0

    def sizeHint(self):
        return QSize(100,50) # The recommended size for the widget 
    
    def getStarRating(self):
        return self.starRating
    
    def setStarRating(self, value):
        self.starRating = value
        self.update()  # Trigger a repaint


    def mouseReleaseEvent(self, event):
        self.editingFinished.emit()

    def mouseMoveEvent(self, event):
        # Convert the mouse x position to an integer rating 
        rating = int(event.position().x()//20)

        # Only update if the rating has changed and is valid
        if rating != self.starRating and rating < 6 and rating >= 0:
            self.starRating = rating
            self.update()  # Trigger a repaint

    def paintEvent(self, event):

        painter = QPainter(self)

        # Enable antialiasing for smoother drawing
        painter.setRenderHint(QPainter.RenderHint.Antialiasing,True)
        painter.setPen(Qt.PenStyle.NoPen)

        # Draw background
        painter.setBrush(QBrush(Qt.GlobalColor.green))
        painter.drawRect(self.rect())

        # Set the color of the stars
        painter.setBrush(QBrush(Qt.GlobalColor.yellow))

        # Move the painter for star drawing
        painter.translate(self.rect().x(), self.rect().y() + 10)
        painter.scale(0.1, 0.1)
        
        # Draw the stars based on the current rating (ensure integer)
        for i in range(int(self.starRating)):
            painter.drawPolygon(self.poly)
            painter.translate(220,0)

