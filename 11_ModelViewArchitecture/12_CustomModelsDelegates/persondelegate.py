from PySide6.QtWidgets import QStyledItemDelegate, QComboBox
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QColor, QPixmap, QIcon
from personmodel import PersonModel

class PersonDelegate(QStyledItemDelegate):

    def __init__(self, parent = None):
        super().__init__(parent)

    def createEditor(self, parent, option, index):

        # Create the editor for column 1
        if index.column() == 1:
            editor = QComboBox(parent)

            # Put in initial information: the list of colors that Qt knows about 
            for color in QColor.colorNames():
                pixmap = QPixmap(50,50)
                pixmap.fill(QColor(color))
                editor.addItem(QIcon(pixmap), color)
            return editor
        else:
            return super().createEditor(parent, option, index)
        

    def setEditorData(self, editor, index):
        if index.column() == 1: 
            combo = editor
            color_name = index.data(Qt.DisplayRole)
            color_index = QColor.colorNames().index(color_name)
            combo.setCurrentIndex(color_index)
        else:
            return super().setEditorData(editor, index)

    def setModelData(self, editor, model, index):
        if index.column() == 1:
            combo = editor
            model.setData(index, combo.currentText(), Qt.EditRole)
        else:
            return super().setModelData(editor, model, index)

    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)