from PySide6.QtCore import QObject, Signal, Property, QDate


class Expense(QObject):
    dateChanged = Signal(QDate)
    itemChanged = Signal(str)
    amountChanged = Signal(float)
    categoryChanged = Signal(str)

    def __init__(self, date=None, item="", amount=0.0, category="", parent=None):
        super().__init__(parent)
        self._date = date if date else QDate.currentDate()
        self._item = item
        self._amount = amount
        self._category = category

    def date(self):
        return self._date

    def item(self):
        return self._item

    def amount(self):
        return self._amount

    def category(self):
        return self._category

    def setDate(self, date):
        if self._date != date:
            self._date = date
            self.dateChanged.emit(self._date)

    def setItem(self, item):
        if self._item != item:
            self._item = item
            self.itemChanged.emit(self._item)

    def setAmount(self, amount):
        if self._amount != amount:
            self._amount = amount
            self.amountChanged.emit(self._amount)

    def setCategory(self, category):
        if self._category != category:
            self._category = category
            self.categoryChanged.emit(self._category)
