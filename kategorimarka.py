# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kategorimarka.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(425, 232)
        Form.setStyleSheet("background-color: rgb(45, 45, 45);")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(70, 20, 110, 32))
        self.pushButton.setStyleSheet("#pushButton{\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 20, 110, 32))
        self.pushButton_2.setStyleSheet("#pushButton_2{\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(165, 90, 161, 32))
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox.setObjectName("comboBox")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(166, 90, 161, 31))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(92, 90, 72, 32))
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(92, 90, 72, 32))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(100, 140, 231, 23))
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(100, 140, 231, 23))
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.comboBox.setHidden(True)
        self.label_2.setHidden(True)
        self.pushButton_4.setHidden(True)
        self.pushButton.setEnabled(False)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Kategori/Marka Ekleme"))
        self.pushButton.setText(_translate("Form", "Kategori Ekle"))
        self.pushButton_2.setText(_translate("Form", "Marka Ekle"))
        self.label.setText(_translate("Form", "Kategori :"))
        self.label_2.setText(_translate("Form", "Marka :"))
        self.pushButton_3.setText(_translate("Form", "Ekle"))
        self.pushButton_4.setText(_translate("Form", "Ekle"))
