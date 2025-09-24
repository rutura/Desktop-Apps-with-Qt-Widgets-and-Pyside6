from PySide6.QtCore import QAbstractTableModel, Qt, QModelIndex, QDate
from expense import Expense
import os

class ExpenseModel(QAbstractTableModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._expenses = []
        self._headers = ["Date", "Item", "Amount", "Category"]
        self.loadExpenses()


    def rowCount(self, parent=QModelIndex()):
        return len(self._expenses)

    def columnCount(self, parent=QModelIndex()):
        return len(self._headers)
    

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid() or index.row() >= len(self._expenses):
            return None

        expense = self._expenses[index.row()]
        col = index.column()

        if role == Qt.DisplayRole:
            if col == 0:
                return expense.date().toString("dd-MM-yyyy")
            elif col == 1:
                return expense.item()
            elif col == 2:
                return f"{expense.amount():.2f}"
            elif col == 3:
                return expense.category()
        elif role == Qt.EditRole:
            if col == 0:
                return expense.date()
            elif col == 1:
                return expense.item()
            elif col == 2:
                return expense.amount()
            elif col == 3:
                return expense.category()

        return None
    

    def setData(self, index, value, role=Qt.EditRole):
        if not index.isValid() or role != Qt.EditRole:
            return False

        expense = self._expenses[index.row()]
        col = index.column()
        changed = False

        if col == 0 and isinstance(value, (QDate, str)):
            date = value if isinstance(value, QDate) else QDate.fromString(value, "dd-MM-yyyy")
            if date.isValid():
                expense.setDate(date)
                changed = True
        elif col == 1 and value:
            expense.setItem(value)
            changed = True
        elif col == 2:
            amount = float(value)
            if amount >= 0:
                expense.setAmount(amount)
                changed = True
        elif col == 3 and value:
            expense.setCategory(value)
            changed = True

        if changed:
            self.dataChanged.emit(index, index, [role])
            self.saveExpenses()
            return True

        return False
    
    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self._headers[section] if section < len(self._headers) else None
        return None
    
    def flags(self, index):
        return Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable if index.isValid() else Qt.NoItemFlags
    

    def addExpense(self, expense):
        row = len(self._expenses)
        self.beginInsertRows(QModelIndex(), row, row)
        self._expenses.append(expense)
        self.endInsertRows()
        self.saveExpenses()

    def removeExpense(self, index):
        if index.isValid():
            self.beginRemoveRows(QModelIndex(), index.row(), index.row())
            del self._expenses[index.row()]
            self.endRemoveRows()
            self.saveExpenses()



    def saveExpenses(self):
        os.makedirs("data", exist_ok=True)
        file_path = os.path.join("data", "expenses.txt")
        
        with open(file_path, "w") as file:
            for expense in self._expenses:
                file.write(f"{expense.date().toString('dd-MM-yyyy')}\t"
                          f"{expense.item()}\t"
                          f"{expense.amount():.2f}\t"
                          f"{expense.category()}\n")
                

    def loadExpenses(self):
        file_path = os.path.join("data", "expenses.txt")
        if not os.path.exists(file_path):
            return

        self.beginResetModel()
        self._expenses.clear()

        with open(file_path, "r") as file:
            for line in file:
                fields = line.strip().split('\t')
                if len(fields) >= 4:
                    date = QDate.fromString(fields[0], "dd-MM-yyyy")
                    amount = float(fields[2])
                    if date.isValid() and amount >= 0:
                        expense = Expense(date, fields[1], amount, fields[3], self)
                        self._expenses.append(expense)

        self.endResetModel()