import sys
from PySide6.QtWidgets import QApplication, QStyleFactory
from PySide6.QtGui import QPalette, QColor
from PySide6.QtCore import Qt
from widget import Widget


def main():
    app = QApplication(sys.argv)

    # Force Fusion style
    app.setStyle(QStyleFactory.create("Fusion"))

    # Set a light palette
    lightPalette = QPalette()
    lightPalette.setColor(QPalette.Window, QColor(245, 245, 245))
    lightPalette.setColor(QPalette.WindowText, Qt.black)
    lightPalette.setColor(QPalette.Base, Qt.white)
    lightPalette.setColor(QPalette.AlternateBase, QColor(233, 231, 227))
    lightPalette.setColor(QPalette.ToolTipBase, Qt.white)
    lightPalette.setColor(QPalette.ToolTipText, Qt.black)
    lightPalette.setColor(QPalette.Text, Qt.black)
    lightPalette.setColor(QPalette.Button, QColor(233, 231, 227))
    lightPalette.setColor(QPalette.ButtonText, Qt.black)
    lightPalette.setColor(QPalette.BrightText, Qt.red)
    lightPalette.setColor(QPalette.Highlight, QColor(76, 163, 224))
    lightPalette.setColor(QPalette.HighlightedText, Qt.white)

    app.setPalette(lightPalette)

    # Create and show the main widget
    w = Widget()
    w.show()

    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
