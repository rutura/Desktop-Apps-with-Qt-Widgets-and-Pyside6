from typing import Optional
from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import QEvent

class Button(QPushButton):
    def __init__(self, parent: Optional[QPushButton] = None) -> None:
        super().__init__(parent)

    def event(self, event: QEvent) -> bool:
        if (event.type() == QEvent.MouseButtonPress or event.type() == QEvent.MouseButtonDblClick):
            print("Button was clicked or double-clicked.")
            # return True # Event has been handled
        return super().event(event)