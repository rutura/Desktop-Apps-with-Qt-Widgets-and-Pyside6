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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHBoxLayout,
    QLCDNumber, QLabel, QPushButton, QSizePolicy,
    QSlider, QSpinBox, QVBoxLayout, QWidget)

from indicator import Indicator
from watertank import WaterTank

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(752, 657)
        self.horizontalLayout_2 = QHBoxLayout(Widget)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.waterTank = WaterTank(Widget)
        self.waterTank.setObjectName(u"waterTank")

        self.horizontalLayout.addWidget(self.waterTank)

        self.indicator = Indicator(Widget)
        self.indicator.setObjectName(u"indicator")

        self.horizontalLayout.addWidget(self.indicator)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.controlsGroup = QGroupBox(Widget)
        self.controlsGroup.setObjectName(u"controlsGroup")
        self.gridLayout = QGridLayout(self.controlsGroup)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.controlsGroup)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.waterLevelSlider = QSlider(self.controlsGroup)
        self.waterLevelSlider.setObjectName(u"waterLevelSlider")
        self.waterLevelSlider.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout.addWidget(self.waterLevelSlider, 0, 1, 1, 1)

        self.waterLevelDisplay = QLCDNumber(self.controlsGroup)
        self.waterLevelDisplay.setObjectName(u"waterLevelDisplay")

        self.gridLayout.addWidget(self.waterLevelDisplay, 0, 2, 1, 1)

        self.label_2 = QLabel(self.controlsGroup)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.warningThreshold = QSpinBox(self.controlsGroup)
        self.warningThreshold.setObjectName(u"warningThreshold")

        self.gridLayout.addWidget(self.warningThreshold, 1, 1, 1, 1)

        self.label_3 = QLabel(self.controlsGroup)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.dangerThreshold = QSpinBox(self.controlsGroup)
        self.dangerThreshold.setObjectName(u"dangerThreshold")

        self.gridLayout.addWidget(self.dangerThreshold, 2, 1, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.resetButton = QPushButton(self.controlsGroup)
        self.resetButton.setObjectName(u"resetButton")

        self.horizontalLayout_3.addWidget(self.resetButton)

        self.startStopButton = QPushButton(self.controlsGroup)
        self.startStopButton.setObjectName(u"startStopButton")

        self.horizontalLayout_3.addWidget(self.startStopButton)


        self.gridLayout.addLayout(self.horizontalLayout_3, 3, 0, 1, 3)


        self.verticalLayout.addWidget(self.controlsGroup)


        self.horizontalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.controlsGroup.setTitle(QCoreApplication.translate("Widget", u"Controls", None))
        self.label.setText(QCoreApplication.translate("Widget", u"Water Level:", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"Warning Level:", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"Danger Level:", None))
        self.resetButton.setText(QCoreApplication.translate("Widget", u"Reset", None))
        self.startStopButton.setText(QCoreApplication.translate("Widget", u"Start/Stop", None))
    # retranslateUi

