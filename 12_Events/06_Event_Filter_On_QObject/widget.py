from typing import Optional
from PySide6.QtWidgets import QWidget, QMenu
from PySide6.QtCore import QPoint, Qt
from PySide6.QtCore import Slot
from keyboardfilter import KeyboardFilter

from ui_widget import Ui_Widget

class Widget(QWidget):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        # Create an instance of KeyboardFilter
        self.filter = KeyboardFilter(self)

        # Install the event filter on the widget
        self.ui.lineEdit.installEventFilter(self.filter)

        # Connect the remove filter button
        self.ui.removeFilterButton.clicked.connect(self.on_removeFilterButton_clicked)

    @Slot()
    def on_removeFilterButton_clicked(self):
        self.ui.lineEdit.removeEventFilter(self.filter)