from PySide6.QtWidgets import QWidget, QInputDialog, QMessageBox
from ui_widget import Ui_Widget
from personmodel import PersonModel
from person import Person

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        self.model = PersonModel(self)

        self.ui.listView.setModel(self.model)
        self.ui.tableView.setModel(self.model)
        self.ui.treeView.setModel(self.model)

        # Set the same selection model for all views
        self.ui.tableView.setSelectionModel(self.ui.listView.selectionModel())
        self.ui.treeView.setSelectionModel(self.ui.listView.selectionModel())

        # Connect buttons
        self.ui.add_person_button.clicked.connect(self.on_add_person_button_clicked)
        self.ui.remove_person_button.clicked.connect(self.on_remove_person_button_clicked)

    def on_add_person_button_clicked(self):
        name, ok = QInputDialog.getText(None, "Names", "Person name:", text="Type in name")

        if ok and name:
            age, ok = QInputDialog.getInt(None, "Person Age", "Age", value=20, minValue=15, maxValue=120)
            
            if ok:
                person = Person(names=name, favorite_color="blue", age=age, parent=self)
                self.model.addPerson(person)
        else:
            QMessageBox.information(None, "Failure", "Must specify name and age")

    def on_remove_person_button_clicked(self):
        index = self.ui.listView.currentIndex()
        self.model.removePerson(index)
