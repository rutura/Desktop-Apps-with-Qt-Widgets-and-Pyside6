from typing import Optional
from PySide6.QtWidgets import QWidget
from childbutton import ChildButton
from childlineedit import ChildLineEdit
from PySide6.QtCore import Slot

from ui_widget import Ui_Widget

class Widget(QWidget):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        # Create an instance of ChildButton.
        button = ChildButton(self)
        button.setText("Child Button")
        button.clicked.connect(self.on_button_clicked)

        # Create an instance of ChildLineEdit.
        line_edit = ChildLineEdit(self)

        # Add Widgets to the layout 
        self.ui.verticalLayout.addWidget(button)
        self.ui.verticalLayout.addWidget(line_edit)
        
    @Slot()
    def on_button_clicked(self):
        print("Button clicked")