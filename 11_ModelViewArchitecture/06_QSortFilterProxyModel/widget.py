from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QColor, QPixmap
from PySide6.QtCore import Slot, QModelIndex, QStringListModel, QSortFilterProxyModel, Qt
from ui_widget import Ui_Widget


class Widget(QWidget): 
    def __init__(self, parent = None):
        super().__init__(parent)

        # Connect to the ui form
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        # Get all available color names 
        self.color_list = QColor.colorNames()

        # Create a string list model with the color names
        self.model = QStringListModel(self.color_list,self)

        # Create the proxymodel
        self.proxy_model = QSortFilterProxyModel(self)
        self.proxy_model.setSourceModel(self.model)

        # Tell the list view to display the string list model
        self.ui.listView.setModel(self.proxy_model)

        # Connect the clicked signal to our slot
        self.ui.listView.clicked.connect(self.view_clicked)
        self.ui.lineEdit.textChanged.connect(self.line_edit_text_changed)


    @Slot(QModelIndex)
    def view_clicked(self,index):
        # Get the color name from the model
        color_name = self.model.data(index,Qt.DisplayRole)

        # Create a pixmap filled with the selected color
        pixmap = QPixmap(self.ui.label.size())
        pixmap.fill(QColor(color_name))

        # Set the pixmap to the label
        self.ui.label.setPixmap(pixmap)

        # Print all the colors
        # print("All colors", self.model.stringList())


    @Slot(str)
    def line_edit_text_changed(self,text):
        self.proxy_model.setFilterRegularExpression(text)

