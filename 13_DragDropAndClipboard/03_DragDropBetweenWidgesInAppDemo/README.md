## Running the Application

1. Generate the resource Python file:
   ```
   pyside6-rcc resources.qrc -o resource_rc.py
   ```

2. Generate the UI Python file (if widget.ui changes):
   ```
   pyside6-uic widget.ui -o ui_widget.py
   ```

3. Ensure PySide6 is installed:
   ```
   pip install PySide6
   ```

4. Run the application:
   ```
   python main.py
   ```