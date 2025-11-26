from typing import Optional
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QObject, QEvent
from widget import Widget

class Application(QApplication):
    def __init__(self, argv):
        super().__init__(argv)

    def notify(self, receiver: QObject, event: QEvent) -> bool: 
        if (event.type() == QEvent.MouseButtonPress or event.type() == QEvent.MouseButtonDblClick) :
            print("Mouse click or double click event detected")
            print(f"Class Name: {receiver.metaObject().className()}")

            # Try and cast the receiver to a Widget 
            if isinstance(receiver, Widget):
                print("cast successful:", receiver)
            else:
                print("cast failed:", receiver)

            return True
        return super().notify(receiver, event)
