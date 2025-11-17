from PySide6.QtCore import QAbstractListModel, Qt, QModelIndex, QByteArray
from person import Person

class PersonModel(QAbstractListModel):

    # Define the custom roles
    NamesRole = Qt.UserRole + 1
    FavoriteColorRole = Qt.UserRole + 2
    AgeRole = Qt.UserRole + 3


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


    def addPerson(self,person):
        row = len(self.persons)

        # Attempt to insert a row
        if (self.insertRows(row,1)):

            # self.persons[row] = person

            # Get the index of the last item in the list
            index = self.index(len(self.persons) -1)

            self.setData(index,person.names(), self.NamesRole)
            self.setData(index,person.favoriteColor(), self.FavoriteColorRole)
            self.setData(index,person.age(), self.AgeRole)

            # Emit the signal to inform interested parties that the model has changed
            modelIndex = self.index(row)
            self.dataChanged.emit(modelIndex,modelIndex)
            return True
        return False
    
    def addPersonDefault(self):
        person = Person("Added Person", "yellowgreen", 45, self)
        self.addPerson(person)


    def addPersonWithDetails(self, names, age):
        person = Person(names, "yellowgreen", age)
        self.addPerson(person)


    def removePerson(self,index):
        if not index.isValid() or index.row() >= len(self.persons):
            return False  
        return self.removeRows(index.row(),1) 

    def rowCount(self, parent = None):
        return len(self.persons)


    def data(self, index, role = Qt.DisplayRole):
        if not index.isValid() or index.row() < 0 or index.row() >= len(self.persons):
            return None

        person = self.persons[index.row()]
        
        if role == Qt.DisplayRole or role == Qt.EditRole or role == self.NamesRole:
            return f"{person.names()}"

        if role == self.FavoriteColorRole:
            return f"{person.favoriteColor()}"

        if role == self.AgeRole:
            return f"{person.age()}"
        
        if role == Qt.ToolTipRole:
            return f"{person.names()} {index.row()}"
            
        return None
    
    def setData(self, index, value, role = Qt.EditRole):

        if not index.isValid:
            return False
        
        person = self.persons[index.row()]
        something_changed = False

        if role == Qt.EditRole or role == self.NamesRole:
            if person.names() != value: 
                person.setNames(value)
                something_changed = True

        elif role == self.AgeRole:
            if person.age() != value:
                person.setAge(value)
                something_changed = True
        
        elif role == self.FavoriteColorRole:
            if person.favoriteColor() != value:
                person.setFavoriteColor(value)
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
    
    def insertRows(self, row, count, parent = QModelIndex()):
        self.beginInsertRows(QModelIndex(),row, row + count -1)

        # Add people to the list
        for i in range(count):
            self.persons.insert(row,Person())

        self.endInsertRows()
        return True

    def removeRows(self, row, count, parent = QModelIndex()):
        self.beginRemoveRows(QModelIndex(),row, row + count -1)

        # Remove people from the list
        for i in range(count):
            self.persons.pop(row)

        self.endRemoveRows()
        return True
    
    def roleNames(self):
        roles = {}
        roles[self.NamesRole] = QByteArray(b"names")
        roles[self.FavoriteColorRole] = QByteArray(b"favoritecolor")
        roles[self.AgeRole] = QByteArray(b"age")
        return roles

