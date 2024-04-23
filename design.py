# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_widget(object):
    def setupUi(self, widget):
        if not widget.objectName():
            widget.setObjectName(u"widget")
        widget.resize(300, 450)
        widget.setStyleSheet(u"background-color:black;")
        self.resultLabel = QLabel(widget)
        self.resultLabel.setObjectName(u"resultLabel")
        self.resultLabel.setEnabled(True)
        self.resultLabel.setGeometry(QRect(10, 60, 281, 51))
        font = QFont()
        font.setFamilies([u"Verdana"])
        font.setPointSize(35)
        font.setKerning(True)
        self.resultLabel.setFont(font)
        self.resultLabel.setStyleSheet(u"color:white;")
        self.resultLabel.setMidLineWidth(0)
        self.resultLabel.setWordWrap(True)
        self.sumLabel = QLabel(widget)
        self.sumLabel.setObjectName(u"sumLabel")
        self.sumLabel.setEnabled(True)
        self.sumLabel.setGeometry(QRect(10, 0, 280, 51))
        font1 = QFont()
        font1.setFamilies([u"Verdana"])
        font1.setPointSize(16)
        font1.setKerning(True)
        self.sumLabel.setFont(font1)
        self.sumLabel.setStyleSheet(u"color:white;")
        self.sumLabel.setMidLineWidth(0)
        self.gridLayoutWidget = QWidget(widget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 130, 281, 301))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_09 = QPushButton(self.gridLayoutWidget)
        self.pushButton_09.setObjectName(u"pushButton_09")
        font2 = QFont()
        font2.setFamilies([u"Verdana"])
        font2.setPointSize(17)
        self.pushButton_09.setFont(font2)
        self.pushButton_09.setStyleSheet(u"background-color: #2A322E;\n"
"color:white;\n"
"border-radius:50px;")

        self.gridLayout.addWidget(self.pushButton_09, 0, 2, 1, 1)

        self.pushButton_02 = QPushButton(self.gridLayoutWidget)
        self.pushButton_02.setObjectName(u"pushButton_02")
        self.pushButton_02.setFont(font2)
        self.pushButton_02.setStyleSheet(u"background-color: #2A322E;\n"
"color:white;\n"
"border-radius:50px;")

        self.gridLayout.addWidget(self.pushButton_02, 2, 1, 1, 1)

        self.pushButton_08 = QPushButton(self.gridLayoutWidget)
        self.pushButton_08.setObjectName(u"pushButton_08")
        self.pushButton_08.setFont(font2)
        self.pushButton_08.setStyleSheet(u"background-color: #2A322E;\n"
"color:white;\n"
"border-radius:50px;")

        self.gridLayout.addWidget(self.pushButton_08, 0, 1, 1, 1)

        self.pushButton_04 = QPushButton(self.gridLayoutWidget)
        self.pushButton_04.setObjectName(u"pushButton_04")
        self.pushButton_04.setFont(font2)
        self.pushButton_04.setStyleSheet(u"background-color: #2A322E;\n"
"color:white;\n"
"border-radius:50px;")

        self.gridLayout.addWidget(self.pushButton_04, 1, 0, 1, 1)

        self.pushButton_17 = QPushButton(self.gridLayoutWidget)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setFont(font2)
        self.pushButton_17.setStyleSheet(u"background-color: #2A322E;\n"
"color:white;\n"
"border-radius:50px;")

        self.gridLayout.addWidget(self.pushButton_17, 3, 2, 1, 1)

        self.pushButton_equals = QPushButton(self.gridLayoutWidget)
        self.pushButton_equals.setObjectName(u"pushButton_equals")
        self.pushButton_equals.setFont(font2)
        self.pushButton_equals.setStyleSheet(u"background-color: white;\n"
"color:black;\n"
"border-radius:50px;")

        self.gridLayout.addWidget(self.pushButton_equals, 4, 2, 1, 2)

        self.pushButton_addition = QPushButton(self.gridLayoutWidget)
        self.pushButton_addition.setObjectName(u"pushButton_addition")
        self.pushButton_addition.setFont(font2)
        self.pushButton_addition.setStyleSheet(u"background-color: #EEA10C;\n"
"color:white;\n"
"border-radius:50px;")

        self.gridLayout.addWidget(self.pushButton_addition, 0, 3, 1, 1)

        self.pushButton_division = QPushButton(self.gridLayoutWidget)
        self.pushButton_division.setObjectName(u"pushButton_division")
        self.pushButton_division.setFont(font2)
        self.pushButton_division.setStyleSheet(u"background-color: #EEA10C;\n"
"color:white;\n"
"border-radius:50px;")

        self.gridLayout.addWidget(self.pushButton_division, 3, 3, 1, 1)

        self.pushButton_16 = QPushButton(self.gridLayoutWidget)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setFont(font2)
        self.pushButton_16.setStyleSheet(u"background-color: #2A322E;\n"
"color:white;\n"
"border-radius:50px;")

        self.gridLayout.addWidget(self.pushButton_16, 3, 0, 1, 2)

        self.pushButton_05 = QPushButton(self.gridLayoutWidget)
        self.pushButton_05.setObjectName(u"pushButton_05")
        self.pushButton_05.setFont(font2)
        self.pushButton_05.setStyleSheet(u"background-color: #2A322E;\n"
"color:white;\n"
"border-radius:50px;")

        self.gridLayout.addWidget(self.pushButton_05, 1, 1, 1, 1)

        self.pushButton_01 = QPushButton(self.gridLayoutWidget)
        self.pushButton_01.setObjectName(u"pushButton_01")
        self.pushButton_01.setFont(font2)
        self.pushButton_01.setStyleSheet(u"background-color: #2A322E;\n"
"color:white;\n"
"border-radius:50px;")

        self.gridLayout.addWidget(self.pushButton_01, 2, 0, 1, 1)

        self.pushButton_multiplication = QPushButton(self.gridLayoutWidget)
        self.pushButton_multiplication.setObjectName(u"pushButton_multiplication")
        self.pushButton_multiplication.setFont(font2)
        self.pushButton_multiplication.setStyleSheet(u"background-color: #EEA10C;\n"
"color:white;\n"
"border-radius:50px;")

        self.gridLayout.addWidget(self.pushButton_multiplication, 2, 3, 1, 1)

        self.pushButton_cancel = QPushButton(self.gridLayoutWidget)
        self.pushButton_cancel.setObjectName(u"pushButton_cancel")
        self.pushButton_cancel.setFont(font2)
        self.pushButton_cancel.setStyleSheet(u"background-color: white;\n"
"color:black;\n"
"border-radius:50px;")

        self.gridLayout.addWidget(self.pushButton_cancel, 4, 0, 1, 2)

        self.pushButton_06 = QPushButton(self.gridLayoutWidget)
        self.pushButton_06.setObjectName(u"pushButton_06")
        self.pushButton_06.setFont(font2)
        self.pushButton_06.setStyleSheet(u"background-color: #2A322E;\n"
"color:white;\n"
"border-radius:50px;")

        self.gridLayout.addWidget(self.pushButton_06, 1, 2, 1, 1)

        self.pushButton_subtraction = QPushButton(self.gridLayoutWidget)
        self.pushButton_subtraction.setObjectName(u"pushButton_subtraction")
        self.pushButton_subtraction.setFont(font2)
        self.pushButton_subtraction.setStyleSheet(u"background-color: #EEA10C;\n"
"color:white;\n"
"border-radius:50px;")

        self.gridLayout.addWidget(self.pushButton_subtraction, 1, 3, 1, 1)

        self.pushButton_03 = QPushButton(self.gridLayoutWidget)
        self.pushButton_03.setObjectName(u"pushButton_03")
        self.pushButton_03.setFont(font2)
        self.pushButton_03.setStyleSheet(u"background-color: #2A322E;\n"
"color:white;\n"
"border-radius:50px;")

        self.gridLayout.addWidget(self.pushButton_03, 2, 2, 1, 1)

        self.pushButton_07 = QPushButton(self.gridLayoutWidget)
        self.pushButton_07.setObjectName(u"pushButton_07")
        self.pushButton_07.setFont(font2)
        self.pushButton_07.setStyleSheet(u"background-color: #2A322E;\n"
"color:white;\n"
"border-radius:50px;")

        self.gridLayout.addWidget(self.pushButton_07, 0, 0, 1, 1)


        self.retranslateUi(widget)

        QMetaObject.connectSlotsByName(widget)
    # setupUi

    def retranslateUi(self, widget):
        widget.setWindowTitle(QCoreApplication.translate("widget", u"Calculator", None))
        self.resultLabel.setText(QCoreApplication.translate("widget", u"0", None))
        self.sumLabel.setText(QCoreApplication.translate("widget", u"0", None))
        self.pushButton_09.setText(QCoreApplication.translate("widget", u"9", None))
        self.pushButton_02.setText(QCoreApplication.translate("widget", u"2", None))
        self.pushButton_08.setText(QCoreApplication.translate("widget", u"8", None))
        self.pushButton_04.setText(QCoreApplication.translate("widget", u"4", None))
        self.pushButton_17.setText(QCoreApplication.translate("widget", u".", None))
        self.pushButton_equals.setText(QCoreApplication.translate("widget", u"=", None))
        self.pushButton_addition.setText(QCoreApplication.translate("widget", u"+", None))
        self.pushButton_division.setText(QCoreApplication.translate("widget", u"/", None))
        self.pushButton_16.setText(QCoreApplication.translate("widget", u"0", None))
        self.pushButton_05.setText(QCoreApplication.translate("widget", u"5", None))
        self.pushButton_01.setText(QCoreApplication.translate("widget", u"1", None))
        self.pushButton_multiplication.setText(QCoreApplication.translate("widget", u"*", None))
        self.pushButton_cancel.setText(QCoreApplication.translate("widget", u"C", None))
        self.pushButton_06.setText(QCoreApplication.translate("widget", u"6", None))
        self.pushButton_subtraction.setText(QCoreApplication.translate("widget", u"-", None))
        self.pushButton_03.setText(QCoreApplication.translate("widget", u"3", None))
        self.pushButton_07.setText(QCoreApplication.translate("widget", u"7", None))
    # retranslateUi

