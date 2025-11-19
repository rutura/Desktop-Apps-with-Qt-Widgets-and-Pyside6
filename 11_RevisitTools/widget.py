from PySide6.QtWidgets import QWidget
from ui_widget import Ui_Widget

class Widget(QWidget): 
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)