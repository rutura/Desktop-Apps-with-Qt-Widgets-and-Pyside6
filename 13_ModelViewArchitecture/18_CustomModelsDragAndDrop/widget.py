from PySide6.QtWidgets import QWidget, QListWidgetItem 
from ui_widget import Ui_Widget
from personmodel import PersonModel


class Widget(QWidget): 
    def __init__(self, parent = None):
        super().__init__(parent)

        # Connect to the ui form
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        # Create the model
        model = PersonModel(self)

        # Configure list view
        self.ui.listView.setModel(model)
        self.ui.listView.setDragEnabled(True)
        self.ui.listView.setAcceptDrops(True)
        
        # Configure table view
        self.ui.tableView.setModel(model)
        self.ui.tableView.setDragEnabled(True)
        self.ui.tableView.setAcceptDrops(True)
        
        # Configure tree view
        self.ui.treeView.setModel(model)
        self.ui.treeView.setDragEnabled(True)
        self.ui.treeView.setAcceptDrops(True)