from PyQt5 import QtWidgets
from PyQt5 import QtCore
from urunekleme import Ui_Form
import os
import sys
import mysql.connector
import datetime


class urunEkl(QtWidgets.QWidget):
    def __init__(self):
        super(urunEkl,self).__init__()
        self.uE = Ui_Form()
        self.uE.setupUi(self)
        self.loadcombo()

        self.uE.pushButton.clicked.connect(self.yeniurun)
        self.uE.lineEdit_2.textChanged.connect(self.urunguncelgt)
        self.uE.pushButton_2.clicked.connect(self.urunguncelle)

    def loadcombo(self):
        connection = mysql.connector.connect(host='127.0.0.1',user='root',password='mysql1234',database='stokotomasyon')
        cursor = connection.cursor()

        cursor.execute("SELECT * From kategori_bilgileri")
        a = cursor.fetchall()
        for i in a :
            self.uE.comboBox.addItems(i)
            self.uE.comboBox_3.addItems(i)
        connection.close()

        connection = mysql.connector.connect(host='127.0.0.1',user='root',password='mysql1234',database='stokotomasyon')
        cursor = connection.cursor()

        cursor.execute("SELECT * From marka_bilgileri")
        a = cursor.fetchall()
        list = []
        for i in a :
            list.append(i[1])
        
        self.uE.comboBox_2.addItems(list)
        self.uE.comboBox_4.addItems(list)
        connection.close()

    def yeniurun(self):
        barkodNo = self.uE.lineEdit.text()
        kategori = self.uE.comboBox.currentText()
        marka = self.uE.comboBox_2.currentText()
        urunadı = self.uE.lineEdit_4.text()
        miktar = self.uE.lineEdit_5.text()
        alısF = self.uE.lineEdit_7.text()
        satısF = self.uE.lineEdit_6.text()
        bugun = datetime.datetime.now()
        try:
            connection = mysql.connector.connect(host='127.0.0.1',user='root',password='mysql1234',database='stokotomasyon')
            cursor = connection.cursor()
            sql = "INSERT INTO urunlistesi(barkodno,kategori,marka,urunadı,miktari,alisfiyati,satisfiyati,tarih) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
            values = (barkodNo,kategori,marka,urunadı,miktar,alısF,satısF,bugun)
            cursor.execute(sql,values)
            result = QtWidgets.QMessageBox.information(self,"Onay Butonu","Eklemeyi onaylıyor musunuz ? ",QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
            if result == QtWidgets.QMessageBox.Ok:
                connection.commit()
                cursor.close()
                QtWidgets.QMessageBox.information(self,'Ekleme Onayı','Ürün Dataya Eklendi.')
                self.uE.lineEdit.clear()
                self.uE.lineEdit_4.clear()
                self.uE.lineEdit_5.clear()
                self.uE.lineEdit_6.clear()
                self.uE.lineEdit_7.clear()
        except Exception as err:
            print(str(err))

    def urunguncelgt(self):
        try :
            barkodno = self.uE.lineEdit_2.text()
            db = mysql.connector.connect(host='127.0.0.1', user='root', password='mysql1234', database='stokotomasyon', charset='utf8')
            cur = db.cursor()
            sql = "SELECT * FROM urunlistesi where barkodno=%s"
            value = (barkodno,)
            cur.execute(sql,value)
            data = cur.fetchone()
            self.uE.comboBox_3.setCurrentText(data[1])
            self.uE.comboBox_4.setCurrentText(data[2])
            self.uE.lineEdit_10.setText(data[3])
            self.uE.lineEdit_8.setText(str(data[4]))
            self.uE.lineEdit_11.setText(str(data[5]))
            self.uE.lineEdit_9.setText(str(data[6]))
            global gg
            gg = data[7]
            db.close()
        except Exception as err:
            print(str(err))

    def urunguncelle(self):
        try :
            brno = self.uE.lineEdit_2.text()
            categry = self.uE.comboBox_3.currentText()
            marka = self.uE.comboBox_4.currentText()
            urunadı = self.uE.lineEdit_10.text()
            miktar = self.uE.lineEdit_8.text()
            alısF = self.uE.lineEdit_11.text()
            satısF = self.uE.lineEdit_9.text()

            db = mysql.connector.connect(host='127.0.0.1', user='root', password='mysql1234', database='stokotomasyon', charset='utf8')
            cur = db.cursor()
            sql = "UPDATE urunlistesi set barkodno=%s,kategori=%s,marka=%s,urunadı=%s,miktari=%s,alisfiyati=%s,satisfiyati=%s,tarih=%s Where barkodno = %s "
            values = (brno,categry,marka,urunadı,miktar,alısF,satısF,gg,brno)
            cur.execute(sql,values)
            result = QtWidgets.QMessageBox.information(self,"Onay Butonu","Güncellemeyi onaylıyor musunuz ? ",QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
            if result == QtWidgets.QMessageBox.Ok:
                db.commit()
                db.close()
                QtWidgets.QMessageBox.information(self,'Güncelleme Onayı','Ürün Güncellendi.')
                brno = self.uE.lineEdit_2.clear()
                urunadı = self.uE.lineEdit_10.clear()
                miktar = self.uE.lineEdit_8.clear()
                alısF = self.uE.lineEdit_11.clear()
                satısF = self.uE.lineEdit_9.clear()
        except Exception as err :
            print(str(err))



