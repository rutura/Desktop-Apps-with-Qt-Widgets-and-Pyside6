from PySide6.QtCore import QAbstractListModel, Qt
from person import Person

class PersonModel(QAbstractListModel):
    def __init__(self, parent = None):
        super().__init__(parent)

        # List to store person objects
        self.persons = []

        # Populate with initial data
        self.persons.append(Person("Jamie Lannister", "red", 33))
        self.persons.append(Person("Marry Lane", "cyan", 26))
        self.persons.append(Person("Steve Moors", "yellow", 44))
        self.persons.append(Person("Victor Trunk", "dodgerblue", 30))
        self.persons.append(Person("Ariel Geeny", "blue", 33))
        self.persons.append(Person("Knut Vikran", "lightblue", 26))

    def rowCount(self, parent = None):
        return len(self.persons)


    def data(self, index, role = Qt.DisplayRole):
        if not index.isValid() or index.row() < 0 or index.row() >= len(self.persons):
            return None

        person = self.persons[index.row()]
        
        if role == Qt.DisplayRole or role == Qt.EditRole:
            return f"{person.names()}"
        
        if role == Qt.ToolTipRole:
            return f"{person.names()} {index.row()}"
            
        return None
    
    def setData(self, index, value, role = Qt.EditRole):

        if not index.isValid:
            return False
        
        person = self.persons[index.row()]
        something_changed = False

        if role == Qt.EditRole:
            if person.names() != value: 
                person.setNames(value)
                something_changed = True

        if something_changed:
            self.dataChanged.emit(index,index)
            return True
        
        return False


    def headerData(self, section, orientation, role = Qt.DisplayRole):
        if role != Qt.DisplayRole:
            return None 
        
        if orientation == Qt.Horizontal:
            return "Names"
        return f"Person {section}"


    def flags(self,index):
        if not index.isValid:
            return super().flags(index)
        return super().flags(index) | Qt.ItemIsEditable
