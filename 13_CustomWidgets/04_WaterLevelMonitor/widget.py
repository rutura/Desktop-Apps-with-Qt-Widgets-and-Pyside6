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

        # Create custom widgets  
        indicator = Indicator(self)
        tank = WaterTank(self)

        # Connect signals from the water tank to the indicator
        tank.normal.connect(indicator.activateNormal)
        tank.warning.connect(indicator.activateWarning)
        tank.danger.connect(indicator.activateDanger)

        # Add the widget to the layout
        self.ui.horizontalLayout.addWidget(tank)
        self.ui.horizontalLayout.addWidget(indicator)