from PySide6.QtWidgets import QWidget, QListWidgetItem 
from PySide6.QtCore import QModelIndex, QItemSelectionModel, Qt
from ui_widget import Ui_Widget
from person import Person
from personmodel import PersonModel

class Widget(QWidget): 
    def __init__(self, parent = None):
        super().__init__(parent)

        # Connect to the ui form
        self.ui = Ui_Widget()
        self.ui.setupUi(self)


        # Create and set the model
        self.person_model = PersonModel(self)
        self.ui.treeView.setModel(self.person_model)


        # Connect the buttons to the respective slots
        self.ui.addRowButton.clicked.connect(self.add_row)
        self.ui.removeRowButton.clicked.connect(self.remove_row)
        self.ui.addChildButton.clicked.connect(self.add_child)


        # Print the tree structure
        # self.print_tree_structure()


    # Slots to add and remove rows
    def add_row(self):
        index = self.ui.treeView.selectionModel().currentIndex()
        model = self.ui.treeView.model()

        if model.insertRow(index.row() + 1, index.parent()):
            for column in range(model.columnCount(index.parent())):
                child_index = model.index(index.row() + 1, column, index.parent())
                model.setData(child_index, "[Empy Cell]", Qt.EditRole)


    def remove_row(self):
        index = self.ui.treeView.selectionModel().currentIndex()
        model = self.ui.treeView.model()
        model.removeRow(index.row(), index.parent())


    def add_child(self):
        index = self.ui.treeView.selectionModel().currentIndex()
        model = self.ui.treeView.model()

        # Ensure there are columns
        if model.columnCount(index) == 0:
            if not model.insertColumn(0, index):
                return

        if model.insertRow(0, index):
            for column in range(model.columnCount(index)):
                child_index = model.index( 0, column, index)
                model.setData(child_index, "[Empy Cell]", Qt.EditRole)

            # Set the new child as the current index
            selection_model = self.ui.treeView.selectionModel()
            selection_model.setCurrentIndex(
                model.index(0, 0, index), QItemSelectionModel.ClearAndSelect)

    def print_tree_structure(self):

        # Initialize the root person
        root_person = Person(["John Doe", "CEO"])

        # Create the managers
        manager1 = Person(["Jane Smith", "Manager"], root_person)
        manager2 = Person(["Bob Johnson", "Manager"], root_person)

        # Add managers to root
        root_person.append_child(manager1)
        root_person.append_child(manager2)

        # Add employees under manager1
        employee1 = Person(["Alice Brown", "Developer"], manager1)
        employee2 = Person(["Tom Wilson", "Designer"], manager1)
        manager1.append_child(employee1)
        manager1.append_child(employee2)

        # Add employees under manager2
        employee3 = Person(["Charlie Davis", "Developer"], manager2)
        employee4 = Person(["Eve Anderson", "Tester"], manager2)
        manager2.append_child(employee3)
        manager2.append_child(employee4)

        # Show the tree structure
        root_person.print_tree()

