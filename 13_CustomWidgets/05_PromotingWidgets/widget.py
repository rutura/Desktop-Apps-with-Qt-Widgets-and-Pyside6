from typing import Optional
from ui_widget import Ui_Widget
from PySide6.QtWidgets import QWidget

from PySide6.QtCore import QPoint, Qt
from indicator import Indicator
from watertank import WaterTank

from ui_widget import Ui_Widget

class Widget(QWidget):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        #Make the connections to the ui components 
        self.ui.waterTank.normal.connect(self.ui.indicator.activateNormal)
        self.ui.waterTank.warning.connect(self.ui.indicator.activateWarning)
        self.ui.waterTank.danger.connect(self.ui.indicator.activateDanger)