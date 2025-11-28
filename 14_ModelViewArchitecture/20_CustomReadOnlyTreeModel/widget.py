from PySide6.QtWidgets import QWidget, QListWidgetItem 
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


        # Print the tree structure
        # self.print_tree_structure()


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

