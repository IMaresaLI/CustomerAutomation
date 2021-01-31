from PyQt5 import QtWidgets
from PyQt5 import QtCore
from kategorimarka import Ui_Form
import os
import sys
import mysql.connector



class kateMarka(QtWidgets.QWidget):
    def __init__(self):
        super(kateMarka,self).__init__()
        self.km = Ui_Form()
        self.km.setupUi(self)

        self.km.pushButton_2.clicked.connect(self.activewinME)
        self.km.pushButton.clicked.connect(self.activewinKE)
        self.km.pushButton_3.clicked.connect(self.kE)
        self.km.pushButton_4.clicked.connect(self.markE)

    def activewinKE(self):
        kbtn = self.km.pushButton.isEnabled()
        if kbtn == True:
            self.km.label_2.setHidden(True)
            self.km.label_2.move(92,90)
            self.km.lineEdit.move(166,90)
            self.km.comboBox.setHidden(True)
            self.km.pushButton.setEnabled(False)
            self.km.pushButton_2.setEnabled(True)
            self.km.pushButton_4.setHidden(True)
            self.km.pushButton_3.setHidden(False)
            self.km.pushButton_3.move(100,140)

    def activewinME(self):
        kbtn = self.km.pushButton_2.isEnabled()
        if kbtn == True:
            self.km.label_2.setHidden(False)
            self.km.label_2.move(92,130)
            self.km.lineEdit.move(166,130)
            self.km.comboBox.setHidden(False)
            self.km.pushButton.setEnabled(True)
            self.km.pushButton_2.setEnabled(False)
            self.km.pushButton_4.setHidden(False)
            self.km.pushButton_4.move(100,180)
            self.km.pushButton_3.setHidden(True)
            self.km.comboBox.clear()
            connection = mysql.connector.connect(host='127.0.0.1',user='root',password='mysql1234',database='stokotomasyon')
            cursor = connection.cursor()
            sql = "Select * from kategori_bilgileri"
            cursor.execute(sql)
            item = cursor.fetchall()
            for i in item :
                self.km.comboBox.addItems(i)
            cursor.close()
    
    def kE(self):
        connection = mysql.connector.connect(host='127.0.0.1',user='root',password='mysql1234',database='stokotomasyon')
        cursor = connection.cursor()
        try:
            kateg = self.km.lineEdit.text()
            sql = "INSERT INTO kategori_bilgileri(kategori) VALUES (%s)"
            values = (kateg,)
            cursor.execute(sql,values)
            connection.commit()
            cursor.close()
            QtWidgets.QMessageBox.information(self,'Ekleme Onayı','Kategori Eklendi.')
            self.km.lineEdit.clear()
        except Exception :
            pass

    def markE(self):
        cbtext = self.km.comboBox.currentText()
        text = self.km.lineEdit.text()
        connection = mysql.connector.connect(host='127.0.0.1',user='root',password='mysql1234',database='stokotomasyon')
        cursor = connection.cursor()
        sql = "INSERT INTO marka_bilgileri(kategori,marka) VALUES (%s,%s)"
        values = (cbtext,text)
        cursor.execute(sql,values)
        connection.commit()
        cursor.close()
        QtWidgets.QMessageBox.information(self,'Ekleme Onayı','Marka Eklendi.')
        self.km.lineEdit.clear()












