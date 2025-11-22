from parentlineedit import ParentLineEdit
from PySide6.QtGui import QKeyEvent
from PySide6.QtCore import Qt

class ChildLineEdit(ParentLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
    
    def keyPressEvent(self, event: QKeyEvent):
        print("ChildLineEdit keyPressEvent")
        print(f"ChildLineEdit Accepted: {event.isAccepted()}")

        if event.key() == Qt.Key_Delete: 
            print( "Pressed the Delete key")
            self.clear()
            event.accept()  # Mark the event as accepted
        else:
            event.ignore()  # Mark the event as ignored
            super().keyPressEvent(event)