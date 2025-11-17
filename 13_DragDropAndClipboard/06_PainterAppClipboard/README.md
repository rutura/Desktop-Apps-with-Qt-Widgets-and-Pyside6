## Running the Application

1. Generate the UI Python file (if mainwindow.ui changes):
   ```
   pyside6-uic mainwindow.ui -o ui_mainwindow.py
   ```

2. Generate the resource Python file (if resources.qrc changes):
   ```
   pyside6-rcc resource.qrc -o resource_rc.py
   ```

3. Ensure PySide6 is installed:
   ```
   pip install PySide6
   ```

4. Run the application:
   ```
   python main.py
   ```