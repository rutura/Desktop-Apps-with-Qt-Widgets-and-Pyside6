from PySide6.QtCore import QObject, QEvent
from PySide6.QtGui import QKeyEvent

class KeyboardFilter(QObject):
    def __init__(self, parent=None):
        super().__init__(parent)

    def eventFilter(self, watched, event):
        if event.type() == QEvent.KeyPress:
            key_event = event 
            numbers = "1234567890"
            if key_event.text() in numbers:
                print(f"Number key pressed: {key_event.text()}")
                return True
        # Call the base class method for other events
        return super().eventFilter(watched, event)