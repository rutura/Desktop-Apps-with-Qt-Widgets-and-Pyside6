from PySide6.QtWidgets import QWidget, QListWidgetItem 
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt, Slot
from ui_widget import Ui_Widget


class Widget(QWidget): 
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        # Define the fruit list
        self.fruitList = [
            "Apple", "Avocado", "Banana", "Blueberries", 
            "Cucumber", "EggFruit", "Fig", "Grape", 
            "Mango", "Pear", "Pineapple", "Watermellon"
        ]

        #Add the fruits to the list widget
        self.ui.listWidget.addItems(self.fruitList)

        #Set icons and some other data to each item in the list
        for i in range(self.ui.listWidget.count()):
            item = self.ui.listWidget.item(i)
            filename = f":/images/{self.fruitList[i].lower()}.png"
            item.setIcon(QIcon(filename))

        #Connect the button to the slot
        self.ui.readDataButton.clicked.connect(self.button_clicked)


    @Slot()
    def button_clicked(self):
        current_item = self.ui.listWidget.currentItem()
        if current_item:
            fruit = current_item.data(Qt.DisplayRole)
            print(f"Current fruit: {fruit}")

