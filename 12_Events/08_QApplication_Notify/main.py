import sys
from widget import Widget
from application import Application

def main():
    app = Application(sys.argv)
    window = Widget()
    window.show()
    
    return app.exec()

if __name__ == "__main__":
    sys.exit(main())