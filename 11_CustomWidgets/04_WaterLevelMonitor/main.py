import sys
from PySide6.QtWidgets import QApplication
from widget import Widget


def main():
    """Application entry point."""
    app = QApplication(sys.argv)
    w = Widget()
    w.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
