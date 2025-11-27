from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Slot

# Import the compiled UI file (compile with: pyside6-uic widget.ui -o ui_widget.py)
from ui_widget import Ui_Widget


class Widget(QWidget):
    """Main widget that integrates the water tank and indicator"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        self.m_isSimulationRunning = False

        # Connect water tank signals to indicator slots
        self.ui.waterTank.normal.connect(self.ui.indicator.activateNormal)
        self.ui.waterTank.warning.connect(self.ui.indicator.activateWarning)
        self.ui.waterTank.danger.connect(self.ui.indicator.activateDanger)

        # Setup controls
        self.setupControls()

        # Connect control signals
        self.ui.resetButton.clicked.connect(self.onResetClicked)
        self.ui.startStopButton.clicked.connect(self.onStartStopClicked)
        self.ui.waterTank.waterLevelChanged.connect(self.onWaterLevelChanged)
        self.ui.waterLevelSlider.valueChanged.connect(self.ui.waterTank.setWaterLevel)
        self.ui.warningThreshold.valueChanged.connect(self.ui.waterTank.setWarningThreshold)
        self.ui.dangerThreshold.valueChanged.connect(self.ui.waterTank.setDangerThreshold)

    @Slot(int)
    def onWaterLevelChanged(self, level):
        """Handle water level changes"""
        self.ui.waterLevelSlider.blockSignals(True)
        self.ui.waterLevelSlider.setValue(level)
        self.ui.waterLevelSlider.blockSignals(False)
        self.ui.waterLevelDisplay.display(level)

    @Slot()
    def onResetClicked(self):
        """Handle reset button click"""
        self.ui.waterTank.resetWaterLevel()

    @Slot()
    def onStartStopClicked(self):
        """Handle start/stop button click"""
        self.m_isSimulationRunning = not self.m_isSimulationRunning
        if self.m_isSimulationRunning:
            self.ui.waterTank.startSimulation()
            self.ui.startStopButton.setText("Stop")
        else:
            self.ui.waterTank.stopSimulation()
            self.ui.startStopButton.setText("Start")

    def setupControls(self):
        """Setup initial control values"""
        # Setup water level slider
        self.ui.waterLevelSlider.setMinimum(self.ui.waterTank.MIN_WATER_HEIGHT)
        self.ui.waterLevelSlider.setMaximum(self.ui.waterTank.MAX_WATER_HEIGHT)
        self.ui.waterLevelSlider.setValue(self.ui.waterTank.waterLevel())

        # Setup threshold spinboxes
        self.ui.warningThreshold.setRange(
            self.ui.waterTank.MIN_WATER_HEIGHT,
            self.ui.waterTank.MAX_WATER_HEIGHT
        )
        self.ui.dangerThreshold.setRange(
            self.ui.waterTank.MIN_WATER_HEIGHT,
            self.ui.waterTank.MAX_WATER_HEIGHT
        )
        self.ui.warningThreshold.setValue(self.ui.waterTank.warningThreshold())
        self.ui.dangerThreshold.setValue(self.ui.waterTank.dangerThreshold())

        # Initial display value
        self.ui.waterLevelDisplay.display(self.ui.waterTank.waterLevel())
