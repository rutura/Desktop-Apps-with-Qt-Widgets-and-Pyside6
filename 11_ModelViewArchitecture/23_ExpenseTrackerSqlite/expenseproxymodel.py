from PySide6.QtCore import QSortFilterProxyModel, Qt, QModelIndex


class ExpenseProxyModel(QSortFilterProxyModel):
    def __init__(self, parent=None):
        super().__init__(parent)

    def lessThan(self, left, right):
        left_data = self.sourceModel().data(left, Qt.EditRole)
        right_data = self.sourceModel().data(right, Qt.EditRole)
        
        if left.column() == 1 or left.column() == 3:  # Date column (1) or Amount column (3)
            return left_data < right_data
        else:  # Item and Category columns - default string comparison
            return str(left_data).lower() < str(right_data).lower()

