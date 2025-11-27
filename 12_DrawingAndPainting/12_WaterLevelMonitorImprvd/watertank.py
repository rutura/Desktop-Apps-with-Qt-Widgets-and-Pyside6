from PySide6.QtWidgets import QWidget, QSizePolicy
from PySide6.QtCore import QTimer, QSize, Slot, Signal, Property
from PySide6.QtGui import (QPainter, QPen, QBrush, QColor, QPainterPath,
                           QLinearGradient, QRadialGradient, QFont)
from PySide6.QtCore import Qt
import math

# Constants
TANK_LEFT = 10
TANK_TOP = 10
TANK_BOTTOM = 300
TANK_RIGHT = 300
TANK_WIDTH = 290
PEN_WIDTH = 3
UPDATE_INTERVAL = 1000
WATER_INCREMENT = 15


class WaterTank(QWidget):

    # Class constants
    MIN_WATER_HEIGHT = 10
    MAX_WATER_HEIGHT = 290
    DEFAULT_WATER_HEIGHT = 50
    WATER_HEIGHT_STEP = 10

    # Signals
    normal = Signal()  # Emitted when water level is normal
    warning = Signal()  # Emitted when water level is high
    danger = Signal()  # Emitted when water level is critical
    waterLevelChanged = Signal(int)
    warningThresholdChanged = Signal(int)
    dangerThresholdChanged = Signal(int)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.m_waterHeight = self.DEFAULT_WATER_HEIGHT
        self.m_warningThreshold = 210
        self.m_dangerThreshold = 239
        self.m_timer = QTimer(self)

        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)

        self.m_timer.setInterval(UPDATE_INTERVAL)
        self.m_timer.timeout.connect(self._onTimerTimeout)

    def sizeHint(self):
        return QSize(400, 400)

    def waterLevel(self):
        return self.m_waterHeight

    @Slot(int)
    def setWaterLevel(self, height):
        if height < self.MIN_WATER_HEIGHT:
            height = self.MIN_WATER_HEIGHT
        if height > self.MAX_WATER_HEIGHT:
            height = self.MAX_WATER_HEIGHT

        if self.m_waterHeight != height:
            self.m_waterHeight = height
            self.waterLevelChanged.emit(height)
            self.update()

            # Emit appropriate signal based on water level
            if self.m_waterHeight <= self.m_warningThreshold:
                self.normal.emit()
            elif self.m_waterHeight <= self.m_dangerThreshold:
                self.warning.emit()
            else:
                self.danger.emit()

    def warningThreshold(self):
        return self.m_warningThreshold

    @Slot(int)
    def setWarningThreshold(self, threshold):
        if (self.m_warningThreshold != threshold and
            threshold > self.MIN_WATER_HEIGHT and
            threshold < self.m_dangerThreshold):
            self.m_warningThreshold = threshold
            self.warningThresholdChanged.emit(threshold)
            # Re-evaluate current state
            self.setWaterLevel(self.m_waterHeight)
            # Force a redraw to show the new threshold line
            self.update()

    def dangerThreshold(self):
        return self.m_dangerThreshold

    @Slot(int)
    def setDangerThreshold(self, threshold):
        if (self.m_dangerThreshold != threshold and
            threshold > self.m_warningThreshold and
            threshold < self.MAX_WATER_HEIGHT):
            self.m_dangerThreshold = threshold
            self.dangerThresholdChanged.emit(threshold)
            # Re-evaluate current state
            self.setWaterLevel(self.m_waterHeight)
            # Force a redraw to show the new threshold line
            self.update()

    def startSimulation(self):
        self.m_timer.start()

    def stopSimulation(self):
        self.m_timer.stop()

    def resetWaterLevel(self):
        self.setWaterLevel(self.DEFAULT_WATER_HEIGHT)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Draw shadow effect first
        painter.setPen(Qt.NoPen)
        painter.setBrush(QColor(0, 0, 0, 50))
        painter.drawRect(TANK_LEFT + 5, TANK_TOP + 5, TANK_WIDTH, TANK_BOTTOM - TANK_TOP)

        # Draw tank background with beautiful gradient
        tankGradient = QLinearGradient(TANK_LEFT, TANK_TOP, TANK_RIGHT, TANK_BOTTOM)
        tankGradient.setColorAt(0, QColor(250, 250, 250))
        tankGradient.setColorAt(0.5, QColor(230, 230, 230))
        tankGradient.setColorAt(1, QColor(200, 200, 200))
        painter.setBrush(QBrush(tankGradient))
        painter.setPen(QPen(QColor(180, 180, 180), 1))
        painter.drawRect(TANK_LEFT, TANK_TOP, TANK_WIDTH, TANK_BOTTOM - TANK_TOP)

        # Draw metallic tank outline with 3D effect
        tankPen = QPen(QColor(60, 60, 60), PEN_WIDTH)
        painter.setPen(tankPen)
        painter.setBrush(Qt.NoBrush)

        # Draw main tank outline with rounded corners
        tankPath = QPainterPath()
        tankPath.moveTo(TANK_LEFT, TANK_TOP + 10)
        tankPath.quadTo(TANK_LEFT, TANK_TOP, TANK_LEFT + 10, TANK_TOP)
        tankPath.lineTo(TANK_RIGHT - 10, TANK_TOP)
        tankPath.quadTo(TANK_RIGHT, TANK_TOP, TANK_RIGHT, TANK_TOP + 10)
        tankPath.lineTo(TANK_RIGHT, TANK_BOTTOM)
        tankPath.lineTo(TANK_LEFT, TANK_BOTTOM)
        tankPath.closeSubpath()

        painter.setPen(QPen(QColor(80, 80, 80), PEN_WIDTH))
        painter.drawPath(tankPath)

        # Draw tank rivets for industrial look
        painter.setPen(Qt.NoPen)
        painter.setBrush(QColor(120, 120, 120))
        for i in range(6):
            rivetY = TANK_TOP + 30 + i * 40
            painter.drawEllipse(TANK_LEFT - 6, rivetY - 3, 6, 6)
            painter.drawEllipse(TANK_RIGHT + 2, rivetY - 3, 6, 6)

        # Draw water with enhanced gradient and animation effect
        if self.m_waterHeight > 0:
            waterGradient = QLinearGradient(TANK_LEFT, TANK_BOTTOM - self.m_waterHeight,
                                           TANK_LEFT, TANK_BOTTOM)

            # Dynamic water color based on level with more vibrant colors
            if self.m_waterHeight <= self.m_warningThreshold:
                waterColor = QColor(30, 144, 255)  # Bright blue
            elif self.m_waterHeight <= self.m_dangerThreshold:
                waterColor = QColor(255, 140, 0)  # Dark orange
            else:
                waterColor = QColor(220, 20, 60)  # Crimson red

            waterGradient.setColorAt(0, waterColor.lighter(130))
            waterGradient.setColorAt(0.3, waterColor)
            waterGradient.setColorAt(0.7, waterColor.darker(110))
            waterGradient.setColorAt(1, waterColor.darker(130))

            painter.setBrush(QBrush(waterGradient))
            painter.setPen(QPen(waterColor.darker(150), 1))

            # Create water shape with subtle curves
            waterPath = QPainterPath()
            waterPath.moveTo(TANK_LEFT + 1, TANK_BOTTOM)
            waterPath.lineTo(TANK_LEFT + 1, TANK_BOTTOM - self.m_waterHeight + 5)

            # Add wavy water surface
            surfaceY = TANK_BOTTOM - self.m_waterHeight
            x = TANK_LEFT + 1
            while x < TANK_RIGHT - 1:
                waveOffset = int(3 * math.sin((x - TANK_LEFT) * 0.1))
                waterPath.lineTo(x, surfaceY + waveOffset)
                x += 20

            waterPath.lineTo(TANK_RIGHT - 1, TANK_BOTTOM - self.m_waterHeight + 5)
            waterPath.lineTo(TANK_RIGHT - 1, TANK_BOTTOM)
            waterPath.closeSubpath()

            painter.drawPath(waterPath)

            # Add water reflections
            painter.setPen(QPen(waterColor.lighter(180), 2))
            for i in range(4):
                reflectY = surfaceY + 10 + i * 20
                if reflectY < TANK_BOTTOM - 10:
                    painter.drawLine(TANK_LEFT + 20, reflectY, TANK_LEFT + 80, reflectY)
                    painter.drawLine(TANK_RIGHT - 80, reflectY, TANK_RIGHT - 20, reflectY)

            # Add surface sparkle effect
            painter.setPen(QPen(Qt.white, 1))
            painter.setBrush(Qt.white)
            for i in range(8):
                sparkleX = TANK_LEFT + 30 + (i * 30)
                sparkleY = surfaceY + int(2 * math.sin(i * 0.5))
                painter.drawEllipse(sparkleX, sparkleY, 2, 2)

        # Enhanced level indicators with labels
        painter.setPen(QPen(Qt.darkGray, 2))
        painter.setBrush(Qt.NoBrush)

        # Warning threshold line with enhanced styling
        warningY = TANK_BOTTOM - self.m_warningThreshold
        painter.setPen(QPen(QColor(255, 165, 0), 3, Qt.DashLine))
        painter.drawLine(TANK_LEFT - 10, warningY, TANK_RIGHT + 10, warningY)

        # Warning label
        painter.setPen(QPen(QColor(255, 140, 0), 2))
        painter.setFont(QFont("Arial", 9, QFont.Bold))
        painter.drawText(TANK_RIGHT + 40, warningY + 5, "WARNING")

        # Danger threshold line with enhanced styling
        dangerY = TANK_BOTTOM - self.m_dangerThreshold
        painter.setPen(QPen(QColor(255, 0, 0), 3, Qt.DashLine))
        painter.drawLine(TANK_LEFT - 10, dangerY, TANK_RIGHT + 10, dangerY)

        # Danger label
        painter.setPen(QPen(QColor(220, 20, 60), 2))
        painter.setFont(QFont("Arial", 9, QFont.Bold))
        painter.drawText(TANK_RIGHT + 40, dangerY + 5, "DANGER")

        # Enhanced measurement scale
        painter.setPen(QPen(Qt.black, 1))
        painter.setFont(QFont("Arial", 8))
        for i in range(11):
            scaleY = TANK_BOTTOM - (i * (TANK_BOTTOM - TANK_TOP) // 10)
            painter.drawLine(TANK_RIGHT + 2, scaleY, TANK_RIGHT + 12, scaleY)
            painter.drawText(TANK_RIGHT + 16, scaleY + 3, f"{i * 10}%")

    def wheelEvent(self, event):
        delta = event.angleDelta().y()

        if delta < 0 and self.m_waterHeight > self.MIN_WATER_HEIGHT:
            # Scroll down to decrease water level
            self.setWaterLevel(self.m_waterHeight - self.WATER_HEIGHT_STEP)
        elif delta > 0:
            self.setWaterLevel(self.m_waterHeight + self.WATER_HEIGHT_STEP)

    def _onTimerTimeout(self):
        self.setWaterLevel(self.m_waterHeight + WATER_INCREMENT)
