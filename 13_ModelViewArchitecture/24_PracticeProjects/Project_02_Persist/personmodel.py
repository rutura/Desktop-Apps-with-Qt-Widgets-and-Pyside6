from PySide6.QtCore import QAbstractListModel, Qt, QModelIndex
from person import Person
import os

class PersonModel(QAbstractListModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.persons = []
        self.m_data_file_path = self.getDataFilePath()
        self.loadData()

    def addPerson(self, person=None, names=None, age=None):
        if person is None and names is not None and age is not None:
            person = Person(names=names, favorite_color="blue", age=age)
        elif person is None:
            return

        self.beginInsertRows(QModelIndex(), len(self.persons), len(self.persons))
        self.persons.append(person)
        self.endInsertRows()
        self.saveData()

    def removePerson(self, index):
        if not index.isValid():
            return
        
        self.beginRemoveRows(QModelIndex(), index.row(), index.row())
        del self.persons[index.row()]
        self.endRemoveRows()
        self.saveData()

    def rowCount(self, parent=QModelIndex()):
        return len(self.persons)

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return None
        
        if role == Qt.DisplayRole or role == Qt.EditRole:
            person = self.persons[index.row()]
            return person.names

        return None

    def setData(self, index, value, role=Qt.EditRole):
        if not index.isValid():
            return False

        if role == Qt.EditRole:
            person = self.persons[index.row()]
            if isinstance(value, str):
                name = value.split('-')[0].strip()
                person.setNames(name)
            self.saveData()
            self.dataChanged.emit(index, index, [role])
            return True
        return False

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return "Person"
        return None

    def flags(self, index):
        if not index.isValid():
            return Qt.NoItemFlags
        return Qt.ItemIsEditable | Qt.ItemIsEnabled | Qt.ItemIsSelectable

    def getDataFilePath(self):
        # Use the data folder in the project root
        return os.path.join(os.path.dirname(__file__), "data", "data.txt")

    def loadData(self):
        try:
            if not os.path.exists(self.m_data_file_path):
                return False

            with open(self.m_data_file_path, 'r') as file:
                for line in file:
                    if line.strip():  # Skip empty lines
                        names, favorite_color, age = line.strip().split('\t')
                        person = Person(
                            names=names,
                            favorite_color=favorite_color,
                            age=int(age)
                        )
                        self.persons.append(person)
            return True
        except Exception as e:
            print(f"Error loading data: {e}")
            return False

    def saveData(self):
        try:
            os.makedirs(os.path.dirname(self.m_data_file_path), exist_ok=True)
            with open(self.m_data_file_path, 'w') as file:
                for person in self.persons:
                    file.write(f"{person.names}\t{person.favoriteColor}\t{person.age}\n")
            return True
        except Exception as e:
            print(f"Error saving data: {e}")
            return False
