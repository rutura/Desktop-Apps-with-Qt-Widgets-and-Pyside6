from PySide6.QtWidgets import QWidget, QSizePolicy
from PySide6.QtCore import QSize, QTimer, Qt
from PySide6.QtGui import QPainter, QPen, QBrush, QColor

# Constants
LIGHT_WIDTH = 100
LIGHT_HEIGHT = 100
LIGHT_MARGIN = 10
LIGHT_SPACING = 115
FRAME_WIDTH = 120
FRAME_HEIGHT = 330
PEN_WIDTH = 3
BLINK_INTERVAL = 300

class Indicator(QWidget):
    
    def __init__(self, parent=None):
        super().__init__(parent)
                
        self.m_greenActive = False
        self.m_redActive = False
        self.m_yellowActive = False
        self.m_lightsOn = True
        self.m_timer = QTimer(self)
        
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.activateDanger()
        
        self.m_timer.setInterval(BLINK_INTERVAL)
        self.m_timer.timeout.connect(self.toggleLights)
        self.m_timer.start()

    def sizeHint(self):
        """Return the preferred size of the widget."""
        return QSize(FRAME_WIDTH, FRAME_HEIGHT + 20)
    
    def activateNormal(self):
        """Activates the green light."""
        self.m_greenActive = True
        self.m_yellowActive = False
        self.m_redActive = False
    
    def activateWarning(self):
        """Activates the yellow light."""
        self.m_yellowActive = True
        self.m_redActive = False
        self.m_greenActive = False
    
    def activateDanger(self):
        """Activates the red light."""
        self.m_redActive = True
        self.m_yellowActive = False
        self.m_greenActive = False


    def paintEvent(self, event):
        """Paint the indicator with its frame and lights."""
        painter = QPainter(self)
        pen = QPen(Qt.black, PEN_WIDTH)
        painter.setPen(pen)
        painter.setBrush(QBrush(Qt.gray))

        # Draw the frame
        painter.drawRect(0, 0, FRAME_WIDTH, FRAME_HEIGHT)