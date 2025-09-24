from PySide6.QtWidgets import QWidget, QListWidgetItem 
from ui_widget import Ui_Widget   
from personmodel import PersonModel



class Widget(QWidget): 
    def __init__(self, parent = None):
        super().__init__(parent)

        # Connect to the ui form
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        # Create the person model
        self.model = PersonModel(self)

        # Set the model to the views
        self.ui.listView.setModel(self.model)
        self.ui.tableView.setModel(self.model)
        self.ui.treeView.setModel(self.model)