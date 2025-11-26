import sys
from PySide6.QtWidgets import QApplication
from widget import Widget
from filter import Filter

def main():
    app = QApplication(sys.argv)
    window = Widget()
    window.show()

    # Create an instance of the Filter and install it on the application
    event_filter = Filter(window)
    app.installEventFilter(event_filter)
    
    return app.exec()

if __name__ == "__main__":
    sys.exit(main())