from typing import Optional
from PySide6.QtWidgets import QWidget, QMenu
from PySide6.QtCore import QPoint, Qt
from datetimewidget import DateTimeWidget


from ui_widget import Ui_Widget

class Widget(QWidget):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        # Create DateTimeWidget instance
        self.dateTimeWidget = DateTimeWidget(self) 

        # Add DateTimeWidget to the main layout
        self.ui.verticalLayout.addWidget(self.dateTimeWidget)