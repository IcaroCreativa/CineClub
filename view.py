# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'viewdDjWPM.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6 import QtWidgets
from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore
from pathlib import Path
# from keyboard import KeyboardWidget

def absPath(file):
    return str(Path(__file__).parent.absolute()/file)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(327, 387)
        icon = QIcon()
        file_window_icon=absPath("assets/logo.png")
        icon.addFile(file_window_icon, QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout.addWidget(self.lineEdit)

        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setSelectionMode(QtWidgets.QListWidget.ExtendedSelection)# permite de selectionnar varios elementos de la lista

        self.verticalLayout.addWidget(self.listWidget)

        self.pushButton_add = QPushButton(self.centralwidget)
        self.pushButton_add.setObjectName(u"pushButton_add")
        icon = QIcon()
        
        icon.addFile(file_window_icon, QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_add.setIcon(icon)

        self.verticalLayout.addWidget(self.pushButton_add)

        self.pushButton_delete = QPushButton(self.centralwidget)
        self.pushButton_delete.setObjectName(u"pushButton_delete")
        icon1 = QIcon()
        file_pushbutton_delete_icon=absPath("assets/delete.png")
        icon1.addFile(file_pushbutton_delete_icon, QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_delete.setIcon(icon1)
        
       
        
        self.pushButton_new_screen=QPushButton("ventana")
        self.verticalLayout.addWidget(self.pushButton_delete)
        self.verticalLayout.addWidget(self.pushButton_new_screen)
        

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"CINECLUB", None))
        self.pushButton_add.setText(QCoreApplication.translate("MainWindow", u"Ajouter un film", None))
        self.pushButton_delete.setText(QCoreApplication.translate("MainWindow", u"Suprimer le(s) film(s)", None))
    # retranslateUi

