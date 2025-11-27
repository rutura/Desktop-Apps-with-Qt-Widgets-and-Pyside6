from PySide6.QtWidgets import QWidget, QSizePolicy
from PySide6.QtCore import QTimer, QSize, Slot
from PySide6.QtGui import QPainter, QPen, QBrush, QColor, QLinearGradient, QRadialGradient
from PySide6.QtCore import Qt
import math

# Constants
LIGHT_WIDTH = 100
LIGHT_HEIGHT = 100
LIGHT_MARGIN = 5
LIGHT_SPACING = 110
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
        self.activateNormal()

        self.m_timer.setInterval(BLINK_INTERVAL)
        self.m_timer.timeout.connect(self.toggleLights)
        self.m_timer.start()

    def sizeHint(self):
        return QSize(FRAME_WIDTH, FRAME_HEIGHT + 20)  # Add some padding

    @Slot()
    def activateNormal(self):
        self.m_greenActive = True
        self.m_yellowActive = self.m_redActive = False

    @Slot()
    def activateWarning(self):
        self.m_yellowActive = True
        self.m_redActive = self.m_greenActive = False

    @Slot()
    def activateDanger(self):
        self.m_redActive = True
        self.m_yellowActive = self.m_greenActive = False

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Draw the frame with gradient and 3D effect
        frameGradient = QLinearGradient(0, 0, FRAME_WIDTH, FRAME_HEIGHT)
        frameGradient.setColorAt(0, QColor(150, 150, 150))
        frameGradient.setColorAt(0.5, QColor(120, 120, 120))
        frameGradient.setColorAt(1, QColor(90, 90, 90))

        painter.setBrush(QBrush(frameGradient))
        painter.setPen(QPen(QColor(60, 60, 60), PEN_WIDTH))
        painter.drawRoundedRect(0, 0, FRAME_WIDTH, FRAME_HEIGHT, 15, 15)

        # Draw inner frame shadow
        painter.setPen(QPen(QColor(40, 40, 40), 2))
        painter.setBrush(Qt.NoBrush)
        painter.drawRoundedRect(5, 5, FRAME_WIDTH - 10, FRAME_HEIGHT - 10, 10, 10)

        # Helper function to draw enhanced lights
        def drawEnhancedLight(yPos, isActive, activeColor):
            # Draw light housing with metallic effect
            painter.setPen(QPen(QColor(80, 80, 80), 2))
            painter.setBrush(QColor(40, 40, 40))
            painter.drawEllipse(LIGHT_MARGIN - 5, yPos - 5, LIGHT_WIDTH + 10, LIGHT_HEIGHT + 10)

            # Draw the light itself
            if isActive and self.m_lightsOn:
                # Create radial gradient for glowing effect
                lightGradient = QRadialGradient(
                    LIGHT_MARGIN + LIGHT_WIDTH // 2,
                    yPos + LIGHT_HEIGHT // 2,
                    LIGHT_WIDTH // 2
                )
                lightGradient.setColorAt(0, activeColor.lighter(150))
                lightGradient.setColorAt(0.3, activeColor)
                lightGradient.setColorAt(0.7, activeColor.darker(120))
                lightGradient.setColorAt(1, activeColor.darker(150))

                painter.setBrush(QBrush(lightGradient))
                painter.setPen(QPen(activeColor.darker(130), 2))
                painter.drawEllipse(LIGHT_MARGIN, yPos, LIGHT_WIDTH, LIGHT_HEIGHT)

                # Add highlight effect
                painter.setPen(Qt.NoPen)
                painter.setBrush(QColor(255, 255, 255, 80))
                painter.drawEllipse(LIGHT_MARGIN + 15, yPos + 15, 25, 25)

                # Add outer glow effect
                painter.setPen(QPen(activeColor.lighter(120), 4))
                painter.setBrush(Qt.NoBrush)
                painter.drawEllipse(LIGHT_MARGIN - 2, yPos - 2, LIGHT_WIDTH + 4, LIGHT_HEIGHT + 4)
            else:
                # Inactive light with subtle gradient
                inactiveGradient = QRadialGradient(
                    LIGHT_MARGIN + LIGHT_WIDTH // 2,
                    yPos + LIGHT_HEIGHT // 2,
                    LIGHT_WIDTH // 2
                )
                inactiveGradient.setColorAt(0, QColor(60, 60, 60))
                inactiveGradient.setColorAt(0.7, QColor(30, 30, 30))
                inactiveGradient.setColorAt(1, QColor(10, 10, 10))

                painter.setBrush(QBrush(inactiveGradient))
                painter.setPen(QPen(QColor(20, 20, 20), 2))
                painter.drawEllipse(LIGHT_MARGIN, yPos, LIGHT_WIDTH, LIGHT_HEIGHT)

        # Draw the three lights
        if self.m_redActive:
            drawEnhancedLight(LIGHT_MARGIN, True, QColor(255, 50, 50))
            drawEnhancedLight(LIGHT_SPACING, False, Qt.green)
            drawEnhancedLight(LIGHT_SPACING * 2, False, Qt.yellow)
        elif self.m_yellowActive:
            drawEnhancedLight(LIGHT_MARGIN, False, Qt.red)
            drawEnhancedLight(LIGHT_SPACING, False, Qt.green)
            drawEnhancedLight(LIGHT_SPACING * 2, True, QColor(255, 255, 50))
        elif self.m_greenActive:
            drawEnhancedLight(LIGHT_MARGIN, False, Qt.red)
            drawEnhancedLight(LIGHT_SPACING, True, QColor(50, 255, 50))
            drawEnhancedLight(LIGHT_SPACING * 2, False, Qt.yellow)

    def toggleLights(self):
        self.m_lightsOn = not self.m_lightsOn
        self.update()
