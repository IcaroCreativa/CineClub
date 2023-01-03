# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerzXGMFl.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 194)
        Form.setStyleSheet(u"background-color: #607d8b;")
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(150, 70, 75, 24))
        self.pushButton.setStyleSheet(u"color: rgb(170, 0, 0);\n"
"background-color:#bdbdbd;")
        self.lineEdit2 = QLineEdit(Form)
        self.lineEdit2.setObjectName(u"lineEdit")
        self.lineEdit2.setGeometry(QRect(102, 110, 181, 31))
        self.lineEdit2.setStyleSheet(u"color: #424242;\n"
"font: 700 9pt \"Montserrat\";\n"
"background-color: white;")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Subventana", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Click", None))
        self.lineEdit2.setText(QCoreApplication.translate("Form", None))
    # retranslateUi

