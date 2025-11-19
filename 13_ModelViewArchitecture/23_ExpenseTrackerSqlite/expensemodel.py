from PySide6.QtCore import Qt, QModelIndex, QDate, QDir
from PySide6.QtSql import QSqlTableModel, QSqlDatabase, QSqlQuery, QSqlRecord
import os


class ExpenseModel(QSqlTableModel):
    def __init__(self, parent=None):
        # Create a new database connection
        db = QSqlDatabase.addDatabase("QSQLITE", "ExpenseConnection")
        super().__init__(parent, db)
        if not self.initialize_model():
            print("Failed to initialize database model")
            return

    def cleanup(self):
        """Clean up database resources"""
        if self.database().isOpen():
            self.database().close()
        connection_name = self.database().connectionName()
        QSqlDatabase.removeDatabase(connection_name)

    def __del__(self):
        self.cleanup()

    def initialize_model(self):
        # Create data directory if it doesn't exist
        data_dir = QDir.current()
        if not data_dir.exists("data"):
            if not data_dir.mkpath("data"):
                print("Failed to create data directory")
                return False

        # Set up the database path
        db_path = data_dir.absoluteFilePath("data/expenses.db")
        print(f"Using database at: {db_path}")

        # Set the database path
        self.database().setDatabaseName(db_path)

        # Try to open the database
        if not self.database().open():
            print(f"Failed to open database: {self.database().lastError().text()}")
            return False

        # Create table if it doesn't exist
        if not self.create_table():
            print(f"Failed to create table: {self.database().lastError().text()}")
            return False

        # Configure the model
        self.setTable("expenses")
        self.setEditStrategy(QSqlTableModel.OnFieldChange)

        # Load the data
        if not self.select():
            print(f"Failed to select data: {self.lastError().text()}")
            return False

        print(f"Successfully initialized database with {self.rowCount()} rows")
        return True

    def create_table(self):
        query = QSqlQuery(self.database())
        success = query.exec(
            """CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date DATE NOT NULL,
                item TEXT NOT NULL,
                amount REAL NOT NULL,
                category TEXT NOT NULL
            )"""
        )

        if not success:
            print(f"Create table error: {query.lastError().text()}")
        return success

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid() or (role != Qt.DisplayRole and role != Qt.EditRole):
            return super().data(index, role)

        value = super().data(index, role)
        
        if role == Qt.DisplayRole:
            if index.column() == 1:  # Date column
                # Convert string to QDate if needed
                if isinstance(value, str):
                    value = QDate.fromString(value, "yyyy-MM-dd")
                if isinstance(value, QDate):
                    return value.toString("dd-MM-yyyy")
                return value
            elif index.column() == 3:  # Amount column
                try:
                    return f"{float(value):.2f}"
                except (ValueError, TypeError):
                    return value
        elif role == Qt.EditRole and index.column() == 1:
            if isinstance(value, str):
                return QDate.fromString(value, "yyyy-MM-dd")
            return value
        
        return value

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role != Qt.DisplayRole:
            return None

        if orientation == Qt.Horizontal:
            if section == 0:
                return "ID"
            elif section == 1:
                return "Date"
            elif section == 2:
                return "Item"
            elif section == 3:
                return "Amount"
            elif section == 4:
                return "Category"

        return super().headerData(section, orientation, role)

    def addExpense(self, expense):
        """Add a new expense to the database"""
        record = QSqlRecord()  # Create a blank record
        # Add fields excluding the ID which is auto-generated
        record.append(self.record().field("date"))
        record.append(self.record().field("item"))
        record.append(self.record().field("amount"))
        record.append(self.record().field("category"))
        
        # Set the values for each field
        record.setValue("date", expense.date())
        record.setValue("item", expense.item())
        record.setValue("amount", expense.amount())
        record.setValue("category", expense.category())
        
        success = self.insertRecord(-1, record)
        if not success:
            print(f"Failed to add expense: {self.lastError().text()}")
            return False
        
        success = self.submitAll()
        if success:
            self.select()  # Refresh the view
            print(f"Added expense: {expense.date().toString('dd-MM-yyyy')} {expense.item()} {expense.amount()} {expense.category()}")
        else:
            print(f"Failed to submit changes: {self.lastError().text()}")
        
        return success

    def removeExpense(self, index):
        """Remove an expense from the database"""
        if not index.isValid():
            return False
            
        self.beginRemoveRows(QModelIndex(), index.row(), index.row())
        success = self.removeRow(index.row())
        if not success:
            print(f"Failed to remove expense: {self.lastError().text()}")
            self.endRemoveRows()
            return False
        
        success = self.submitAll()
        if success:
            self.select()  # Refresh the view
            
        self.endRemoveRows()
        return success

    def setData(self, index, value, role=Qt.EditRole):
        if not index.isValid() or role != Qt.EditRole:
            return False

        if index.column() == 1:  # Date
            if isinstance(value, str):
                value = QDate.fromString(value, "dd-MM-yyyy")
            if not isinstance(value, QDate) or not value.isValid():
                return False
        elif index.column() == 3:  # Amount
            try:
                amount = float(value)
                if amount < 0:
                    return False
                value = amount
            except (ValueError, TypeError):
                return False

        self.beginResetModel()  # Signal the view that data is changing
        
        # Submit changes to the database
        success = super().setData(index, value, role)
        
        # Save changes and refresh the model if initial update was successful
        if success:
            success = self.submitAll()
            if success:
                self.select()  # Refresh the view
                
        self.endResetModel()  # Signal the view that data change is complete
        if success:
            self.dataChanged.emit(index, index, [role])  # Emit dataChanged signal for the changed index
            
        return success

    def flags(self, index):
        if not index.isValid():
            return Qt.NoItemFlags

        return Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable
