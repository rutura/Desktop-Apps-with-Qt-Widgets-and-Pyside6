from typing import Optional
from PySide6.QtWidgets import QWidget, QMenu
from doubleclickablebutton import DoubleClickableButton

from ui_widget import Ui_Widget

class Widget(QWidget):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        # Create the double-clickable button
        self.button = DoubleClickableButton(self)
        self.button.setText("Double Clickable Button")

        # Connect the doubleClicked signal to our slot
        self.button.doubleClicked.connect(self.onButtonDoubleClicked)

        # Add the button to the layout
        self.ui.verticalLayout.addWidget(self.button)

    def onButtonDoubleClicked(self):
        print("Button double clicked")
    