from PySide6.QtWidgets import QWidget, QTableWidgetItem
from PySide6.QtCore import Qt
from ui_widget import Ui_Widget


class Widget(QWidget): 
    def __init__(self, parent = None):
        super().__init__(parent)

        # Connect to the ui form
        self.ui = Ui_Widget()
        self.ui.setupUi(self)


        # Initialize table data
        self.table = [
            ["Alice", "Smith", "29", "Engineer", "Single", "USA", "New York", "85"],
            ["Bob", "Brown", "34", "Doctor", "Married", "Canada", "Toronto", "92"],
            ["Charlie", "Davis", "41", "Artist", "Single", "UK", "London", "78"],
            ["Diana", "Evans", "25", "Designer", "Married", "Australia", "Sydney", "88"],
            ["Ethan", "Foster", "37", "Chef", "Single", "France", "Paris", "81"],
            ["Fiona", "Garcia", "30", "Nurse", "Married", "Spain", "Madrid", "90"],
            ["George", "Harris", "45", "Pilot", "Single", "Germany", "Berlin", "76"],
            ["Hannah", "Ibrahim", "28", "Scientist", "Married", "India", "Mumbai", "89"],
            ["Ian", "Jackson", "33", "Lawyer", "Single", "Japan", "Tokyo", "84"],
            ["Julia", "Kim", "26", "Teacher", "Married", "South Korea", "Seoul", "91"],
            ["Kevin", "Lopez", "39", "Farmer", "Single", "Mexico", "Mexico City", "80"],
            ["Laura", "Martinez", "31", "Photographer", "Married", "Italy", "Rome", "87"],
            ["Michael", "Nelson", "42", "Writer", "Single", "Brazil", "Rio", "75"],
            ["Nina", "O'Connor", "27", "Architect", "Married", "Ireland", "Dublin", "93"],
            ["Oscar", "Perez", "36", "Musician", "Single", "Argentina", "Buenos Aires", "82"],
            ["Paula", "Quinn", "32", "Engineer", "Married", "South Africa", "Cape Town", "86"],
            ["Quentin", "Reed", "40", "Doctor", "Single", "Russia", "Moscow", "79"],
            ["Rachel", "Smith", "24", "Student", "Single", "China", "Beijing", "88"],
            ["Steve", "Taylor", "38", "Entrepreneur", "Married", "USA", "San Francisco", "94"],
            ["Tina", "Upton", "29", "Scientist", "Single", "UK", "Manchester", "83"]
        ]

        # Set table headers
        labels = ["First Name", "Last Name", "Age", "Profession", "Marital Status", 
                  "Country", "City", "Social Score"]
        self.ui.tableWidget.setHorizontalHeaderLabels(labels)

        # Populate the table with data
        rows = len(self.table)
        columns = len(self.table[0])

        for row in range(rows):
            self.new_row()
            for col in range(columns):
                #Set text for each cell
                self.ui.tableWidget.item(row,col).setText(self.table[row][col])



    def new_row(self):
        row = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(row)

        first_item = None

        # Create items for each column in the new row
        for i in range(8):
            item = QTableWidgetItem()
            if i == 0: 
                first_item = item 

            # Right align text in table cells
            item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            self.ui.tableWidget.setItem(row,i,item)

        # Set first column in the row as current
        if first_item:
            self.ui.tableWidget.setCurrentItem(first_item)


