from PySide6.QtCore import QAbstractTableModel, Qt, QModelIndex
from person import Person

class PersonModel(QAbstractTableModel):
    def __init__(self, parent = None):
        super().__init__(parent)

        # List to store person objects
        self.persons = []

        # Populate with initial data
        self.persons.append(Person("Jamie Lannister", "red", 33, 2))
        self.persons.append(Person("Marry Lane", "cyan", 26, 4 ))
        self.persons.append(Person("Steve Moors", "yellow", 44, 5))
        self.persons.append(Person("Victor Trunk", "dodgerblue", 30, 3))
        self.persons.append(Person("Ariel Geeny", "blue", 33, 2))
        self.persons.append(Person("Knut Vikran", "lightblue", 26, 4))


    def addPerson(self,person):
        row = len(self.persons)

        # Attempt to insert a row
        if (self.insertRows(row,1)):
            self.persons[row] = person

            # Emit the signal to inform interested parties that the model has changed
            startIndex = self.index(row,0)
            endIndex = self.index(row,2)

            self.dataChanged.emit(startIndex,endIndex)
            return True
        return False
    
    def addPersonDefault(self):
        person = Person("Added Person", "yellowgreen", 45, 1, self)
        self.addPerson(person)


    def addPersonWithDetails(self, names, age):
        person = Person(names, "yellowgreen", age, 1)
        self.addPerson(person)


    def removePerson(self,index):
        if not index.isValid() or index.row() >= len(self.persons):
            return False  
        return self.removeRows(index.row(),1) 

    def rowCount(self, parent = None):
        return len(self.persons)
    
    def columnCount(self, parent = None):
        return 4


    def data(self, index, role = Qt.DisplayRole):
        if not index.isValid() or index.row() < 0 or index.row() >= len(self.persons):
            return None

        person = self.persons[index.row()]
        
        if role == Qt.DisplayRole or role == Qt.EditRole:
            if index.column() == 0:
                return f"{person.names()}"
            if index.column() == 1:
                return f"{person.favoriteColor()}"
            if index.column() == 2:
                return f"{person.age()}"
            if index.column() == 3:
                return f"{person.socialScore()}"
        
        if role == Qt.ToolTipRole:
            return f"{person.names()} {index.row()}"
            
        return None
    
    def setData(self, index, value, role = Qt.EditRole):

        if not index.isValid:
            return False
        
        person = self.persons[index.row()]
        something_changed = False

        if role == Qt.EditRole:
            if index.column() == 0 and person.names() != value: 
                person.setNames(value)
                something_changed = True

            if index.column() == 1 and person.favoriteColor() != value: 
                person.setFavoriteColor(value)
                something_changed = True

            if index.column() == 2 and person.age() != value: 
                person.setAge(value)
                something_changed = True

            if index.column() == 3 and person.socialScore() != value: 
                person.setSocialScore(value)
                something_changed = True

        if something_changed:
            self.dataChanged.emit(index,index)
            return True
        
        return False


    def headerData(self, section, orientation, role = Qt.DisplayRole):
        if role != Qt.DisplayRole:
            return None 
        
        if orientation == Qt.Horizontal:
            if section == 0:
                return "Names"

            if section == 1:
                return "Favorite Color"

            if section == 2:
                return "Age"

            if section == 3:
                return "Social Score"
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

