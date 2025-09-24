import sys
from PySide6.QtWidgets import QApplication
from widget import Widget

def main():
    app = QApplication(sys.argv)
    w = Widget()
    w.show()
    return app.exec()

if __name__ == '__main__':
    sys.exit(main())
