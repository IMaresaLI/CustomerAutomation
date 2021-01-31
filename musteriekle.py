from PyQt5 import QtWidgets
from PyQt5 import QtCore
from musteriekleme import Ui_Form
import os
import sys
import mysql.connector



class musteriEk(QtWidgets.QWidget):
    def __init__(self):
        super(musteriEk,self).__init__()
        self.mke = Ui_Form()
        self.mke.setupUi(self)

        self.mke.pushButton.clicked.connect(self.musteriKayit)

    def musteriKayit(self):
        tc = self.mke.lineEdit.text()
        adsoyad = self.mke.lineEdit_2.text()
        tel = self.mke.lineEdit_3.text()
        adres = self.mke.lineEdit_4.text()
        email = self.mke.lineEdit_5.text()
        
        connection = mysql.connector.connect(host='127.0.0.1',user='root',password='mysql1234',database='stokotomasyon')
        cursor = connection.cursor()
        try:
            sql = "INSERT INTO musteriler(tc,adsoyad,tel,adres,email) VALUES (%s,%s,%s,%s,%s)"
            values = (tc,adsoyad,tel,adres,email)
            cursor.execute(sql,values)
            result = QtWidgets.QMessageBox.information(self,"Onay Butonu","Eklemeyi onaylıyor musunuz ? ",QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
            if result == QtWidgets.QMessageBox.Ok:
                connection.commit()
                cursor.close()
                QtWidgets.QMessageBox.information(self,'Ekleme Onayı','Müşteri Dataya Eklendi.')
                self.mke.lineEdit.clear()
                self.mke.lineEdit_2.clear()
                self.mke.lineEdit_3.clear()
                self.mke.lineEdit_4.clear()
                self.mke.lineEdit_5.clear()
        except Exception as err :
            print(err)
            QtWidgets.QMessageBox.information(self,'Hata','Tc No Kullanılıyor.')
            return



    