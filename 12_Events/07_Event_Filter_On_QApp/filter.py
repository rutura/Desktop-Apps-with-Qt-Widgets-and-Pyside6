from PySide6.QtCore import QObject, QEvent

class Filter(QObject):
    def __init__(self, parent=None):
        super().__init__(parent)


    def eventFilter(self, watched: QObject, event: QEvent) -> bool:
        if (event.type() == QEvent.MouseButtonPress or 
            event.type() == QEvent.MouseButtonDblClick):
            print("Mouse button pressed or double-clicked.")
            # return True  # Event handled, no need to propagate further
            return False  # Event not fully handled, propagate further
        return super().eventFilter(watched, event)