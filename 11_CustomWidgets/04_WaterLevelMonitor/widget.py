from PySide6.QtWidgets import QWidget
from ui_widget import Ui_Widget
from indicator import Indicator
from watertank import WaterTank


class Widget(QWidget):
    """Main widget that combines the water tank and indicator widgets."""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        
        # Create custom widgets
        indicator = Indicator(self)
        tank = WaterTank(self)
        
        # Connect water tank signals to indicator slots
        tank.normal.connect(indicator.activateNormal)
        tank.warning.connect(indicator.activateWarning)
        tank.danger.connect(indicator.activateDanger)
        
        # Add the widgets to the layout
        self.ui.horizontalLayout.addWidget(tank)
        self.ui.horizontalLayout.addWidget(indicator)
