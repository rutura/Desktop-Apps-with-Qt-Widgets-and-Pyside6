## Running the Application

1. Generate the UI Python file (if widget.ui changes):
   ```
   pyside6-uic widget.ui -o ui_widget.py
   ```
2. Compile the resource file (if resource.qrc changes):
   ```
   pyside6-rcc resource.qrc -o resource_rc.py
   ```

3. Run the application:
   ```
   python main.py
   ```