from typing import Optional
from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QColor
from colorpicker import ColorPicker
from PySide6.QtCore import Slot

from ui_widget import Ui_Widget

class Widget(QWidget):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        # Create color picker and add it to the layout
        self.colorPicker = ColorPicker(self)
        self.colorPicker.colorChanged.connect(self.colorChanged)

        # Add the color picker to the designated layout
        self.ui.verticalLayout.addWidget(self.colorPicker)

    @Slot(QColor)
    def colorChanged(self, color):
        print(f"Color changed to: {color.name()}")