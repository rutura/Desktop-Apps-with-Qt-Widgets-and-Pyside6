from PySide6.QtWidgets import QWidget, QTreeWidgetItem
from ui_widget import Ui_Widget


class Widget(QWidget): 
    def __init__(self, parent = None):
        super().__init__(parent)

        # Connect to the ui form
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        # Set the column count
        self.ui.treeWidget.setColumnCount(2)

        # Set column headers
        headers = ["Organization", "Description"]
        self.ui.treeWidget.setHeaderLabels(headers)

        # Add google root organization
        google_root = self.add_root_organization("Google Inc", "Headquarters")


        # Add the India branch
        google_india = self.add_child_organization(google_root, "Google India", "Google India Branch")
        self.add_child_organization(google_india, "Mumbai", "AI Research")
        self.add_child_organization(google_india, "Bangalore", "Sales")

        # Add the Ghana branch
        google_ghana= self.add_child_organization(google_root, "Google Ghana", "Google Ghana Branch")
        self.add_child_organization(google_ghana, "Akra", "AI")

    def add_root_organization(self, company, purpose):
        item = QTreeWidgetItem(self.ui.treeWidget)
        item.setText(0,company)
        item.setText(1,purpose)
        return item

    def add_child_organization(self, parent, branch, description):
        item = QTreeWidgetItem()
        item.setText(0,branch)
        item.setText(1,description)
        parent.addChild(item)
        return item