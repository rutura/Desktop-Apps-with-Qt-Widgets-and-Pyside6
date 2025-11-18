from PySide6.QtWidgets import QWidget, QSizePolicy
from PySide6.QtCore import QSize, QTimer, Qt, Signal
from PySide6.QtGui import QPainter, QPen, QBrush


# Constants
TANK_LEFT = 10
TANK_TOP = 10
TANK_BOTTOM = 300
TANK_RIGHT = 300
TANK_WIDTH = 290
PEN_WIDTH = 3
UPDATE_INTERVAL = 1000
WATER_INCREMENT = 15
NORMAL_THRESHOLD = 210
WARNING_THRESHOLD = 239


class WaterTank(QWidget):
    """Custom widget that displays a water tank with animated water level."""
    
    # Signals
    normal = Signal()   # Emitted when water level is normal
    warning = Signal()  # Emitted when water level is high
    danger = Signal()   # Emitted when water level is critical
    
    # Class constants
    DEFAULT_WATER_HEIGHT = 50
    MIN_WATER_HEIGHT = 10
    WATER_HEIGHT_STEP = 10
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.m_waterHeight = self.DEFAULT_WATER_HEIGHT
        self.m_timer = QTimer(self)
        
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.m_timer.setInterval(UPDATE_INTERVAL)
        
        self.m_timer.timeout.connect(self.onTimerTimeout)
        self.m_timer.start()
    
    def onTimerTimeout(self):
        """Handle timer timeout to increase water level."""
        self.m_waterHeight += WATER_INCREMENT
        self.update()
        
        # Emit appropriate signal based on water level
        if self.m_waterHeight <= NORMAL_THRESHOLD:
            self.normal.emit()
        elif self.m_waterHeight <= WARNING_THRESHOLD:
            self.warning.emit()
        else:
            self.danger.emit()
    
    def sizeHint(self):
        """Return the preferred size of the widget."""
        return QSize(400, 400)
    
    def wheelEvent(self, event):
        """Handle mouse wheel events to control water level."""
        delta = event.angleDelta().y()
        
        if delta < 0 and self.m_waterHeight > self.MIN_WATER_HEIGHT:
            # Scroll down to decrease the water level
            self.m_waterHeight -= self.WATER_HEIGHT_STEP
            self.update()
            
            # Emit appropriate signal based on updated water level
            if self.m_waterHeight <= NORMAL_THRESHOLD:
                self.normal.emit()
            elif self.m_waterHeight <= WARNING_THRESHOLD:
                self.warning.emit()
            else:
                self.danger.emit()
    
    def paintEvent(self, event):
        """Paint the water tank and water level."""
        painter = QPainter(self)
        
        # Set up painter
        pen = QPen(Qt.yellow, PEN_WIDTH)
        painter.setPen(pen)
        
        # Draw the tank outline
        painter.drawLine(TANK_LEFT, TANK_TOP, TANK_LEFT, TANK_BOTTOM)      # Left
        painter.drawLine(TANK_LEFT, TANK_BOTTOM, TANK_RIGHT, TANK_BOTTOM)  # Bottom
        painter.drawLine(TANK_RIGHT, TANK_BOTTOM, TANK_RIGHT, TANK_TOP)    # Right
        
        # Draw the water
        painter.setBrush(QBrush(Qt.blue))
        painter.drawRect(TANK_LEFT, TANK_BOTTOM - self.m_waterHeight, TANK_WIDTH, self.m_waterHeight)
