import sys
from PySide6.QtWidgets import QApplication
from widget import Widget

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Create and show the main widget
    widget = Widget()
    widget.show()  # This line was missing
    
    # Start the application event loop
    sys.exit(app.exec())
