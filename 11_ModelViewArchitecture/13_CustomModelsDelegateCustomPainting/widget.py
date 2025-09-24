from PySide6.QtWidgets import QWidget, QInputDialog, QMessageBox, QLineEdit, QHeaderView
from ui_widget import Ui_Widget   
from personmodel import PersonModel
from persondelegate import PersonDelegate
from person import Person

class Widget(QWidget): 
    def __init__(self, parent = None):
        super().__init__(parent)

        # Connect to the ui form
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        # Create the person model
        self.model = PersonModel(self)


        # Create the delegate
        self.person_delegate = PersonDelegate(self)

        # Set the model to the views
        self.ui.listView.setModel(self.model)
        self.ui.tableView.setModel(self.model)
        self.ui.treeView.setModel(self.model)

        # Make views respect row heights from the delegate
        self.ui.tableView.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)


        # Set the delegates
        self.ui.tableView.setItemDelegate(self.person_delegate)
        self.ui.treeView.setItemDelegate(self.person_delegate)

        # Share the selection model between views
        self.ui.tableView.setSelectionModel(self.ui.listView.selectionModel())
        self.ui.treeView.setSelectionModel(self.ui.listView.selectionModel())

        # Connect the buttons to the slots
        self.ui.addPersonButtton.clicked.connect(self.add_person)
        self.ui.removePersonButton.clicked.connect(self.remove_person)

    def add_person(self):
        # Get name from user
        name, ok = QInputDialog.getText(
            self, 
            "Names",
            "Person name:", 
            QLineEdit.Normal,
            "Type in name"
        )

        if ok and name:
            # Get age from user
            age, ok = QInputDialog.getInt(
                self,
                "Person Age",
                "Age",
                20,  # Default value
                15,  # Min value
                120  # Max value
            )

            if ok:
                # Create the person object and add it to the model
                person = Person(name,"blue", age,self)
                self.model.addPerson(person)

        else:
            QMessageBox.information(
                self,
                "Failure", 
                "Must specify name and age"
            )

    def remove_person(self):
        index = self.ui.listView.currentIndex()
        self.model.removePerson(index)
