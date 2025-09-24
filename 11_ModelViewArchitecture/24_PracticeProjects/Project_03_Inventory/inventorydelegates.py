from PySide6.QtWidgets import QStyledItemDelegate, QComboBox, QFileDialog, QStyle
from PySide6.QtCore import Qt, QSize, QRect
from PySide6.QtGui import QPainter, QPen, QBrush, QColor, QPolygonF
from PySide6.QtCore import QPointF
import math

class ImageDelegate(QStyledItemDelegate):
    def __init__(self, parent=None):
        super().__init__(parent)

    def paint(self, painter, option, index):
        if option.state & QStyle.State_Selected:
            painter.fillRect(option.rect, option.palette.highlight())

        value = index.data(Qt.DecorationRole)
        if value and hasattr(value, 'isNull') and not value.isNull():
            painter.drawPixmap(option.rect, value)
        else:
            painter.drawText(option.rect, Qt.AlignCenter, "No Image")

    def editorEvent(self, event, model, option, index):
        if event.type() == event.Type.MouseButtonDblClick:
            fileName, _ = QFileDialog.getOpenFileName(None,
                "Select Image", "", "Images (*.png *.jpg *.jpeg)")
            if fileName:
                model.setData(index, fileName)
                return True
        return False

    def sizeHint(self, option, index):
        return QSize(64, 64)

class RatingDelegate(QStyledItemDelegate):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.MaxStars = 5
        self.StarSize = 20

    def paint(self, painter, option, index):
        if option.state & QStyle.State_Selected:
            painter.fillRect(option.rect, option.palette.highlight())

        rating = index.data(Qt.DisplayRole)
        if rating is not None:
            for i in range(self.MaxStars):
                starRect = QRect(
                    option.rect.x() + i * self.StarSize,
                    option.rect.y() + (option.rect.height() - self.StarSize) // 2,
                    self.StarSize,
                    self.StarSize
                )
                self.drawStar(painter, starRect, i < rating)

    def drawStar(self, painter, rect, filled):
        painter.save()
        painter.setRenderHint(QPainter.Antialiasing)

        # Calculate star points
        centerX = rect.center().x()
        centerY = rect.center().y()
        radius = min(rect.width(), rect.height()) / 2

        points = []
        for i in range(5):
            # Outer points
            angle = -math.pi / 2 + i * 2 * math.pi / 5
            points.append(QPointF(
                centerX + radius * math.cos(angle),
                centerY + radius * math.sin(angle)
            ))
            # Inner points
            angle += math.pi / 5
            innerRadius = radius * 0.4
            points.append(QPointF(
                centerX + innerRadius * math.cos(angle),
                centerY + innerRadius * math.sin(angle)
            ))

        starPath = QPolygonF(points)

        if filled:
            painter.setBrush(QBrush(QColor("#FFD700")))  # Gold color for filled stars
            pen = QPen(QColor("#DAA520"), 1)  # Darker gold for the border
        else:
            painter.setBrush(QBrush(Qt.white))
            pen = QPen(QColor("#CCCCCC"), 1)

        painter.setPen(pen)
        painter.drawPolygon(starPath)
        painter.restore()

    def editorEvent(self, event, model, option, index):
        if event.type() == event.Type.MouseButtonRelease:
            value = self.starAtPosition(event.position().toPoint(), option)
            if value >= 0:
                model.setData(index, value)
                return True
        return False

    def starAtPosition(self, pos, option):
        x = pos.x() - option.rect.x()
        if 0 <= x <= self.StarSize * self.MaxStars:
            return min(self.MaxStars, (x // self.StarSize) + 1)
        return -1

    def sizeHint(self, option, index):
        return QSize(self.StarSize * self.MaxStars, self.StarSize)

class SupplierDelegate(QStyledItemDelegate):
    def __init__(self, suppliers, parent=None):
        super().__init__(parent)
        self.supplierList = suppliers

    def createEditor(self, parent, option, index):
        editor = QComboBox(parent)
        editor.addItems(self.supplierList)
        return editor

    def setEditorData(self, editor, index):
        value = index.data(Qt.EditRole)
        if value:
            idx = editor.findText(value)
            if idx >= 0:
                editor.setCurrentIndex(idx)

    def setModelData(self, editor, model, index):
        model.setData(index, editor.currentText())

    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)

    def setSuppliers(self, suppliers):
        self.supplierList = suppliers
