import os
from PySide6.QtCore import QAbstractItemModel, QModelIndex, Qt
from PySide6.QtCore import QFile, QIODevice, QTextStream
from person import Person

class PersonModel(QAbstractItemModel):
    def __init__(self, parent = None):
        super().__init__(parent)

        # Initialize the root person
        self.root_person = Person(["John Doe", "CEO"])

        # # Create the managers: in memory
        # manager1 = Person(["Jane Smith", "Manager"], self.root_person)
        # manager2 = Person(["Bob Johnson", "Manager"], self.root_person)

        # # Add managers to root
        # self.root_person.append_child(manager1)
        # self.root_person.append_child(manager2)

        # # Add employees under manager1
        # employee1 = Person(["Alice Brown", "Developer"], manager1)
        # employee2 = Person(["Tom Wilson", "Designer"], manager1)
        # manager1.append_child(employee1)
        # manager1.append_child(employee2)

        # # Add employees under manager2
        # employee3 = Person(["Charlie Davis", "Developer"], manager2)
        # employee4 = Person(["Eve Anderson", "Tester"], manager2)
        # manager2.append_child(employee3)
        # manager2.append_child(employee4)


        # Read the data from a file in the data/familytree.txt file starting from the location of the python file
        self.filename = "data/familytree.txt"
        self.read_file()


    def rowCount(self, parent = QModelIndex()):
        if parent.column() > 0:
            return 0
        parent_person = parent.internalPointer() if parent.isValid() else self.root_person
        return parent_person.child_count()


    def columnCount(self, parent = QModelIndex()):
        return 2
    
    def data(self, index, role = Qt.DisplayRole):

        if not index.isValid():
            return None
       
        if role in (Qt.DisplayRole, Qt.EditRole):
            person = index.internalPointer()
            return person.data(index.column())

        return None 
        
    

    def setData(self, index, value, role = Qt.EditRole):
        if role != Qt.EditRole:
            return False 
        
        person = index.internalPointer()
        result = person.set_data(index.column(),value)

        if result:
            self.dataChanged.emit(index,index, [role])
            self.write_file()

        return result
    
    def insertRows(self, position, rows, parent=QModelIndex()):
        """
        Insert rows at a specific position
        
        :param position: Position to insert rows
        :param rows: Number of rows to insert
        :param parent: Parent model index
        :return: True if successful
        """
        parent_person = self.get_person_from_index(parent)

        self.beginInsertRows(parent, position, position + rows - 1)
        success = parent_person.insert_children(position, rows, self.columnCount())
        self.endInsertRows()

        if success:
            self.write_file()  # Write changes to file

        return success
    

    def removeRows(self, position, rows, parent=QModelIndex()):
        """
        Remove rows at a specific position
        
        :param position: Position to start removing rows
        :param rows: Number of rows to remove
        :param parent: Parent model index
        :return: True if successful
        """
        parent_person = self.get_person_from_index(parent)

        self.beginRemoveRows(parent, position, position + rows - 1)
        success = parent_person.remove_children(position, rows)
        self.endRemoveRows()

        if success:
            self.write_file()  # Write changes to file

        return success

    

    def headerData(self, section, orientation, role = Qt.DisplayRole):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return "Name" if section == 0 else "Profession"
        return None
    
    def flags(self, index):
        if not index.isValid():
            return Qt.NoItemFlags
        return super().flags(index) | Qt.ItemIsEditable | Qt.ItemIsEnabled | Qt.ItemIsSelectable
    

    # Implement index and parent to make this a proper tree model.
    def index(self, row, column, parent = QModelIndex()):

        if not self.hasIndex(row,column,parent):
            return QModelIndex()
        
        if parent.isValid():
            parent_person = parent.internalPointer()
        else:
            parent_person = self.root_person

        child_person = parent_person.child(row)

        if child_person:
            return self.createIndex(row,column, child_person)
        else:
            return QModelIndex()
        

    def get_person_from_index(self, index):
        """
        Get Person object from a model index
        
        :param index: Model index
        :return: Person object
        """
        return index.internalPointer() if index.isValid() else self.root_person     



    def parent(self,childIndex):
        if not childIndex.isValid():
            return QModelIndex()
        
        child_person = childIndex.internalPointer()
        parent_person = child_person.parent_person()

        if parent_person == self.root_person:
            return QModelIndex()
        return self.createIndex(parent_person.row(), 0, parent_person)
    

    # Read data from the file
    def parse_line(self,line):
        """
        Parse a line into names and profession
        
        :param line: Line from the input file
        :return: Tuple of (names, profession)
        """
        parts = line.split('(')
        names = parts[0].strip()
        profession = parts[1].rstrip(')').strip()
        return names, profession
    

    def read_file(self):

        last_indentation = 0
        last_parent = self.root_person
        last_person = None

        # Use QFile for resource file
        file = QFile(self.filename)
        
        if file.open(QIODevice.ReadOnly | QIODevice.Text):
            text_stream = QTextStream(file)

            while not text_stream.atEnd():
                line = text_stream.readLine()
                current_indentation = line.count('\t')
                names, profession = self.parse_line(line.strip())

                diff_indent = current_indentation - last_indentation

                if diff_indent == 0:
                    # Sibling level
                    person = Person([names,profession], last_parent)
                    last_parent.append_child(person)
                    last_person = person

                elif diff_indent > 0:
                    # Nest a child
                    last_parent = last_person
                    person = Person([names,profession], last_parent)
                    last_parent.append_child(person)
                    last_person = person

                else:
                    # Move up the parent chain
                    iterations = - diff_indent
                    for _ in range(iterations):
                        last_parent = last_parent.parent_person()

                    person = Person([names,profession], last_parent)
                    last_parent.append_child(person)
                    last_person = person

                last_indentation = current_indentation
            file.close()

    # Write the changes back to the file
    def write_person(self, person, text_stream, level=0):
        """
        Write a person and their descendants to the text stream
        
        :param person: Person object to write
        :param text_stream: QTextStream to write to
        :param level: Current indentation level
        """
        if person == self.root_person:
            # Skip writing root but process its children at level 0
            for child_index in range(person.child_count()):
                self.write_person(person.child(child_index), text_stream, 0)
            return

        # Create indentation
        indentation = '\t' * level
        
        # Format the line: "Name (Profession)"
        line = f"{indentation}{person.data(0)} ({person.data(1)})"
        text_stream << line << '\n'
        
        # Write all children recursively with increased indentation
        for child_index in range(person.child_count()):
            self.write_person(person.child(child_index), text_stream, level + 1)

    def write_file(self):
        file = QFile(self.filename)

        if file.open(QIODevice.WriteOnly | QIODevice.Text):
            text_stream = QTextStream(file)
            # Start writing from root
            self.write_person(self.root_person,text_stream)
        

        
