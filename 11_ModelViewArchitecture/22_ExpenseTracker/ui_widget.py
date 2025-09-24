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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTableView, QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(800, 600)
        self.verticalLayout = QVBoxLayout(Widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.filterLayout = QHBoxLayout()
        self.filterLayout.setObjectName(u"filterLayout")
        self.filterLabel = QLabel(Widget)
        self.filterLabel.setObjectName(u"filterLabel")

        self.filterLayout.addWidget(self.filterLabel)

        self.filterLineEdit = QLineEdit(Widget)
        self.filterLineEdit.setObjectName(u"filterLineEdit")

        self.filterLayout.addWidget(self.filterLineEdit)

        self.columnLabel = QLabel(Widget)
        self.columnLabel.setObjectName(u"columnLabel")

        self.filterLayout.addWidget(self.columnLabel)

        self.filterColumnComboBox = QComboBox(Widget)
        self.filterColumnComboBox.setObjectName(u"filterColumnComboBox")

        self.filterLayout.addWidget(self.filterColumnComboBox)


        self.verticalLayout.addLayout(self.filterLayout)

        self.tableView = QTableView(Widget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableView.setSortingEnabled(True)

        self.verticalLayout.addWidget(self.tableView)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.addExpenseButton = QPushButton(Widget)
        self.addExpenseButton.setObjectName(u"addExpenseButton")

        self.horizontalLayout.addWidget(self.addExpenseButton)

        self.removeExpenseButton = QPushButton(Widget)
        self.removeExpenseButton.setObjectName(u"removeExpenseButton")

        self.horizontalLayout.addWidget(self.removeExpenseButton)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Personal Budget Tracker", None))
        self.filterLabel.setText(QCoreApplication.translate("Widget", u"Filter:", None))
        self.filterLineEdit.setPlaceholderText(QCoreApplication.translate("Widget", u"Enter text to filter...", None))
        self.columnLabel.setText(QCoreApplication.translate("Widget", u"Column:", None))
        self.addExpenseButton.setText(QCoreApplication.translate("Widget", u"Add Expense", None))
        self.removeExpenseButton.setText(QCoreApplication.translate("Widget", u"Remove Expense", None))
    # retranslateUi

