from PySide6.QtCore import QSortFilterProxyModel, Qt, QModelIndex


class ExpenseProxyModel(QSortFilterProxyModel):
    def __init__(self, parent=None):
        super().__init__(parent)

    def lessThan(self, left, right):
        left_data = self.sourceModel().data(left, Qt.EditRole)
        right_data = self.sourceModel().data(right, Qt.EditRole)

        if left.column() == 0:  # Date column
            return left_data < right_data
        elif left.column() == 2:  # Amount column
            try:
                return float(left_data) < float(right_data)
            except (ValueError, TypeError):
                return False
        else:  # Item and Category columns - default string comparison
            return str(left_data).lower() < str(right_data).lower()
