# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QListView, QPushButton, QSizePolicy, QSpacerItem,
    QTableView, QTreeView, QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(1035, 461)
        self.verticalLayout = QVBoxLayout(Widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.label_2 = QLabel(Widget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(Widget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.listView = QListView(Widget)
        self.listView.setObjectName(u"listView")

        self.horizontalLayout_3.addWidget(self.listView)

        self.tableView = QTableView(Widget)
        self.tableView.setObjectName(u"tableView")

        self.horizontalLayout_3.addWidget(self.tableView)

        self.treeView = QTreeView(Widget)
        self.treeView.setObjectName(u"treeView")

        self.horizontalLayout_3.addWidget(self.treeView)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.addPersonButtton = QPushButton(Widget)
        self.addPersonButtton.setObjectName(u"addPersonButtton")

        self.horizontalLayout_2.addWidget(self.addPersonButtton)

        self.removePersonButton = QPushButton(Widget)
        self.removePersonButton.setObjectName(u"removePersonButton")

        self.horizontalLayout_2.addWidget(self.removePersonButton)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Custom Read Only List Model", None))
        self.label.setText(QCoreApplication.translate("Widget", u"ListView", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"Tableview", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"Treeview", None))
        self.addPersonButtton.setText(QCoreApplication.translate("Widget", u"Add Person", None))
        self.removePersonButton.setText(QCoreApplication.translate("Widget", u"Remove Person", None))
    # retranslateUi

