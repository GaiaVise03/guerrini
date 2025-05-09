# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'provagui.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(657, 501)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btnWelcome = QPushButton(self.centralwidget)
        self.btnWelcome.setObjectName(u"btnWelcome")
        self.btnWelcome.setGeometry(QRect(70, 130, 151, 51))
        font = QFont()
        font.setFamilies([u"Arial Narrow"])
        font.setPointSize(10)
        self.btnWelcome.setFont(font)
        self.elNome = QLineEdit(self.centralwidget)
        self.elNome.setObjectName(u"elNome")
        self.elNome.setGeometry(QRect(70, 40, 180, 30))
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(11)
        self.elNome.setFont(font1)
        self.elCognome = QLineEdit(self.centralwidget)
        self.elCognome.setObjectName(u"elCognome")
        self.elCognome.setGeometry(QRect(70, 90, 180, 30))
        self.elCognome.setFont(font1)
        self.lblMsg = QLabel(self.centralwidget)
        self.lblMsg.setObjectName(u"lblMsg")
        self.lblMsg.setGeometry(QRect(60, 200, 401, 51))
        self.lblMsg.setAutoFillBackground(False)
        self.lblMsg.setStyleSheet(u"background-color:rgb(49, 42, 255);\n"
"\n"
"\n"
"font: 75 24pt \"MS Serif\";\n"
"\n"
"\n"
"\n"
"color:#ffff00;")
        self.elNum1 = QLineEdit(self.centralwidget)
        self.elNum1.setObjectName(u"elNum1")
        self.elNum1.setGeometry(QRect(280, 40, 180, 30))
        self.elNum1.setFont(font1)
        self.elNum2 = QLineEdit(self.centralwidget)
        self.elNum2.setObjectName(u"elNum2")
        self.elNum2.setGeometry(QRect(280, 80, 180, 30))
        self.elNum2.setFont(font1)
        self.btnPlus = QPushButton(self.centralwidget)
        self.btnPlus.setObjectName(u"btnPlus")
        self.btnPlus.setGeometry(QRect(280, 130, 151, 51))
        font2 = QFont()
        font2.setPointSize(16)
        self.btnPlus.setFont(font2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btnWelcome.setText(QCoreApplication.translate("MainWindow", u"visualizza messaggio", None))
        self.elNome.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ins nome", None))
        self.elCognome.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ins cognome", None))
        self.lblMsg.setText(QCoreApplication.translate("MainWindow", u"----", None))
        self.btnPlus.setText(QCoreApplication.translate("MainWindow", u"+", None))
    # retranslateUi

