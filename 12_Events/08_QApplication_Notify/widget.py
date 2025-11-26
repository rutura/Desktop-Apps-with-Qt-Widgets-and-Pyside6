from typing import Optional
from PySide6.QtWidgets import QWidget, QMenu
from PySide6.QtCore import QPoint, Qt
from PySide6.QtGui import (
    QMouseEvent, 
    QCloseEvent, 
    QContextMenuEvent,
    QEnterEvent,
    QKeyEvent,
    QWheelEvent,
    QResizeEvent,
    QPaintEvent
)

from ui_widget import Ui_Widget

class Widget(QWidget):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)