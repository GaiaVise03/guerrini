# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
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
    QPushButton, QSizePolicy, QStatusBar, QToolBar,
    QToolButton, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(958, 690)
        MainWindow.setStyleSheet(u"background-color: rgb(0, 0, 127);\n"
"background-color: rgb(85, 85, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Nome = QLabel(self.centralwidget)
        self.Nome.setObjectName(u"Nome")
        self.Nome.setGeometry(QRect(170, 120, 112, 16))
        self.Nome.setStyleSheet(u"font: 12pt \"MS Gothic\";\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.Cognome = QLabel(self.centralwidget)
        self.Cognome.setObjectName(u"Cognome")
        self.Cognome.setGeometry(QRect(170, 160, 126, 19))
        self.Cognome.setStyleSheet(u"font: 75 12pt \"MS Shell Dlg 2\";")
        self.Nome_2 = QLineEdit(self.centralwidget)
        self.Nome_2.setObjectName(u"Nome_2")
        self.Nome_2.setGeometry(QRect(340, 120, 113, 20))
        self.Nome_2.setMinimumSize(QSize(113, 0))
        self.Nome_2.setMaximumSize(QSize(113, 16777215))
        self.Nome_2.setStyleSheet(u"alternate-background-color: rgb(85, 170, 255);")
        self.Cognome_2 = QLineEdit(self.centralwidget)
        self.Cognome_2.setObjectName(u"Cognome_2")
        self.Cognome_2.setGeometry(QRect(340, 160, 113, 20))
        self.toolButton = QToolButton(self.centralwidget)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setGeometry(QRect(290, 210, 75, 23))
        self.n1 = QPushButton(self.centralwidget)
        self.n1.setObjectName(u"n1")
        self.n1.setGeometry(QRect(410, 480, 131, 23))
        self.n1.setStyleSheet(u"color: rgb(85, 170, 255);\n"
"background-color: rgb(85, 170, 255);")
        self.n2 = QPushButton(self.centralwidget)
        self.n2.setObjectName(u"n2")
        self.n2.setGeometry(QRect(370, 510, 131, 23))
        self.n2.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(160, 540, 71, 13))
        self.label.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(330, 520, 86, 13))
        self.label_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(560, 490, 28, 13))
        self.label_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.risultato = QLabel(self.centralwidget)
        self.risultato.setObjectName(u"risultato")
        self.risultato.setGeometry(QRect(220, 250, 231, 41))
        self.risultato.setStyleSheet(u"background-color: rgb(85, 0, 255);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Nome.setText(QCoreApplication.translate("MainWindow", u"Inserisci nome", None))
        self.Cognome.setText(QCoreApplication.translate("MainWindow", u"inserisci cognome", None))
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"INVIA", None))
        self.n1.setText("")
        self.n2.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u" Primo numero ", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u" Secondo numero ", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"totale", None))
        self.risultato.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

