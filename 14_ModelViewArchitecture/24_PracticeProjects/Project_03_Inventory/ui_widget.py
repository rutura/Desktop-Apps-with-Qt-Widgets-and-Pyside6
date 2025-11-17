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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTableView, QVBoxLayout,
    QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(1200, 700)
        self.verticalLayout = QVBoxLayout(Widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.mainFrame = QFrame(Widget)
        self.mainFrame.setObjectName(u"mainFrame")
        self.mainFrameLayout = QVBoxLayout(self.mainFrame)
        self.mainFrameLayout.setObjectName(u"mainFrameLayout")
        self.searchLayout = QHBoxLayout()
        self.searchLayout.setObjectName(u"searchLayout")
        self.searchLabel = QLabel(self.mainFrame)
        self.searchLabel.setObjectName(u"searchLabel")

        self.searchLayout.addWidget(self.searchLabel)

        self.searchLineEdit = QLineEdit(self.mainFrame)
        self.searchLineEdit.setObjectName(u"searchLineEdit")

        self.searchLayout.addWidget(self.searchLineEdit)


        self.mainFrameLayout.addLayout(self.searchLayout)

        self.inventoryTableView = QTableView(self.mainFrame)
        self.inventoryTableView.setObjectName(u"inventoryTableView")
        self.inventoryTableView.setSelectionMode(QAbstractItemView.SingleSelection)
        self.inventoryTableView.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.mainFrameLayout.addWidget(self.inventoryTableView)

        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.setObjectName(u"buttonLayout")
        self.addButton = QPushButton(self.mainFrame)
        self.addButton.setObjectName(u"addButton")

        self.buttonLayout.addWidget(self.addButton)

        self.editButton = QPushButton(self.mainFrame)
        self.editButton.setObjectName(u"editButton")

        self.buttonLayout.addWidget(self.editButton)

        self.deleteButton = QPushButton(self.mainFrame)
        self.deleteButton.setObjectName(u"deleteButton")

        self.buttonLayout.addWidget(self.deleteButton)

        self.manageSuppliersButton = QPushButton(self.mainFrame)
        self.manageSuppliersButton.setObjectName(u"manageSuppliersButton")

        self.buttonLayout.addWidget(self.manageSuppliersButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.buttonLayout.addItem(self.horizontalSpacer)


        self.mainFrameLayout.addLayout(self.buttonLayout)


        self.verticalLayout.addWidget(self.mainFrame)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Inventory Management System", None))
        self.searchLabel.setText(QCoreApplication.translate("Widget", u"Search:", None))
        self.searchLineEdit.setPlaceholderText(QCoreApplication.translate("Widget", u"Enter search terms...", None))
        self.addButton.setText(QCoreApplication.translate("Widget", u"Add Item", None))
        self.editButton.setText(QCoreApplication.translate("Widget", u"Edit Item", None))
        self.deleteButton.setText(QCoreApplication.translate("Widget", u"Delete Item", None))
        self.manageSuppliersButton.setText(QCoreApplication.translate("Widget", u"Manage Suppliers", None))
    # retranslateUi

