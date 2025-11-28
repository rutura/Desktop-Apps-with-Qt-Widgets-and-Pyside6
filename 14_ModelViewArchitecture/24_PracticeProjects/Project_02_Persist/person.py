from PySide6.QtCore import QObject, Signal, Property

class Person(QObject):
    namesChanged = Signal(str)
    favoriteColorChanged = Signal(str)
    ageChanged = Signal(int)

    def __init__(self, names="", favorite_color="", age=0, parent=None):
        super().__init__(parent)
        self._names = names
        self._favorite_color = favorite_color
        self._age = age

    def names(self):
        return self._names

    def setNames(self, names):
        if self._names != names:
            self._names = names
            self.namesChanged.emit(names)

    def favoriteColor(self):
        return self._favorite_color

    def setFavoriteColor(self, favorite_color):
        if self._favorite_color != favorite_color:
            self._favorite_color = favorite_color
            self.favoriteColorChanged.emit(favorite_color)

    def age(self):
        return self._age

    def setAge(self, age):
        if self._age != age:
            self._age = age
            self.ageChanged.emit(age)

    # Define Qt properties
    names = Property(str, names, setNames, notify=namesChanged)
    favoriteColor = Property(str, favoriteColor, setFavoriteColor, notify=favoriteColorChanged)
    age = Property(int, age, setAge, notify=ageChanged)
