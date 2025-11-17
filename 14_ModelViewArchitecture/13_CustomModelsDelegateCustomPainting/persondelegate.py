from PySide6.QtWidgets import QStyledItemDelegate, QComboBox
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QColor, QPixmap, QIcon, QPainter, QBrush
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


    def paint(self, painter, option, index):
        if index.column() == 1:

            # Get the favorite color
            fav_color = index.data(Qt.DisplayRole)

            painter.save()

            # Set the brush to the favorite color
            painter.setBrush(QBrush(QColor(fav_color)))

            # Draw the background rectangle in fav_color
            adjust_amount = 3
            painter.drawRect(option.rect.adjusted(adjust_amount,adjust_amount,-adjust_amount,-adjust_amount))

            #  Calculate the text size
            text_size = option.fontMetrics.size(Qt.TextSingleLine, fav_color)

            # Set the brush to white for the inner rectangle
            painter.setBrush(QBrush(QColor(Qt.white)))

            # Calculate the adjustments for the inner rectangle
            width_adjust = (option.rect.width() - text_size.width()) // 2 - 3
            height_adjust = (option.rect.height() - text_size.height()) // 2 

            # Draw the white rectangle for the text background
            painter.drawRect(option.rect.adjusted(width_adjust,height_adjust,-width_adjust,-height_adjust))


            # Draw the color name text 
            painter.drawText(option.rect, fav_color, Qt.AlignHCenter | Qt.AlignVCenter)

            painter.restore()

        else:
            return super().paint(painter, option, index)
        
    def sizeHint(self, option, index):
        if index.column() == 1: 
            return QSize(100,35) # This a recommendation.
        else:
            return super().sizeHint(option, index)