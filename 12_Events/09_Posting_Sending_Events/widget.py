from typing import Optional
from PySide6.QtWidgets import QWidget, QApplication
from PySide6.QtCore import QPointF, Qt, QEvent, Slot
from PySide6.QtGui import QMouseEvent
from button import Button

from ui_widget import Ui_Widget

class Widget(QWidget):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)


        # Create an object of Button
        self.button1 = Button(self)
        self.button1.setText("I am the phoenix king")

        # Connect the button's clicked signal to a slot
        self.ui.button2.clicked.connect(self.on_button2_clicked)


    @Slot()
    def on_button2_clicked(self):
        """Create and post a synthetic mouse event to button1"""
        
        # Create a mouse press event
        mouse_event = QMouseEvent(
            QEvent.MouseButtonPress,  # Type
            QPointF(10, 10),          # Local position
            QPointF(10, 10),          # Screen position 
            Qt.LeftButton,            # Button
            Qt.LeftButton,            # Buttons
            Qt.NoModifier             # Modifiers
        )

        # Post the event to button1
        # QApplication.postEvent(self.button1, mouse_event)

        # Send the event through sendEvent
        if( QApplication.sendEvent(self.button1, mouse_event)):
            print("Event was accepted.")
        else:
            print("Event was ignored.")