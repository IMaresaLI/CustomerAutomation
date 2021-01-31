from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui
from musterilist import Ui_MainWindow
import os
import sys
import mysql.connector


class Mek(QtWidgets.QMainWindow):
    def __init__(self):
        super(Mek, self).__init__()
        self.mk = Ui_MainWindow()
        self.mk.setupUi(self)
        self.musteridata()

        self.mk.tableWidget.doubleClicked.connect(self.musterilist)
        self.mk.pushButton_2.clicked.connect(self.musterignc)
        self.mk.pushButton.clicked.connect(self.musterisilme)
        self.mk.lineEdit.textChanged.connect(self.musteridata)

    def musteridata(self):
        try:
            textbox = self.mk.lineEdit.text()
            if textbox == "":
                db = mysql.connector.connect(
                    host='127.0.0.1', user='root', password='mysql1234', database='stokotomasyon', charset='utf8')
                cur = db.cursor()
                cur.execute("SELECT * FROM musteriler")
                data = cur.fetchall()
                column = len(data[0])

                self.mk.tableWidget.setRowCount(len(data))
                self.mk.tableWidget.setColumnCount(column)
                self.mk.tableWidget.setHorizontalHeaderLabels(
                    [i[0] for i in cur.description])

                rows = 0
                rowIndex = 0
                for re in data:
                    if rows != len(data):
                        are = [{
                            'idmusteriler': f'{re[0]}',
                            'tc': f'{re[1]}',
                            'adsoyad': f'{re[2]}',
                            'tel': f'{re[3]}',
                            'adres': f'{re[4]}',
                            'email': f'{re[5]}'
                        }]

                        rows += 1

                        for i in are:
                            self.mk.tableWidget.setItem(
                                rowIndex, 0, QtWidgets.QTableWidgetItem(i['idmusteriler']))
                            self.mk.tableWidget.setItem(
                                rowIndex, 1, QtWidgets.QTableWidgetItem(i['tc']))
                            self.mk.tableWidget.setItem(
                                rowIndex, 2, QtWidgets.QTableWidgetItem(i['adsoyad']))
                            self.mk.tableWidget.setItem(
                                rowIndex, 3, QtWidgets.QTableWidgetItem(i['tel']))
                            self.mk.tableWidget.setItem(
                                rowIndex, 4, QtWidgets.QTableWidgetItem(i['adres']))
                            self.mk.tableWidget.setItem(
                                rowIndex, 5, QtWidgets.QTableWidgetItem(i['email']))
                            rowIndex += 1
                db.close()
            else :
                db = mysql.connector.connect(host='127.0.0.1', user='root', password='mysql1234', database='stokotomasyon', charset='utf8')
                cur = db.cursor()
                cur.execute(f"SELECT * FROM musteriler where tc LIKE '%{textbox}%'")
                data = cur.fetchall()
                column = len(data)

                self.mk.tableWidget.setRowCount(len(data))
                self.mk.tableWidget.setColumnCount(len(cur.description))
                self.mk.tableWidget.setHorizontalHeaderLabels(
                    [i[0] for i in cur.description])

                rows = 0
                rowIndex = 0
                for re in data:
                    if rows != len(data):
                        are = [{
                            'idmusteriler': f'{re[0]}',
                            'tc': f'{re[1]}',
                            'adsoyad': f'{re[2]}',
                            'tel': f'{re[3]}',
                            'adres': f'{re[4]}',
                            'email': f'{re[5]}'
                        }]

                        rows += 1

                        for i in are:
                            self.mk.tableWidget.setItem(
                                rowIndex, 0, QtWidgets.QTableWidgetItem(i['idmusteriler']))
                            self.mk.tableWidget.setItem(
                                rowIndex, 1, QtWidgets.QTableWidgetItem(i['tc']))
                            self.mk.tableWidget.setItem(
                                rowIndex, 2, QtWidgets.QTableWidgetItem(i['adsoyad']))
                            self.mk.tableWidget.setItem(
                                rowIndex, 3, QtWidgets.QTableWidgetItem(i['tel']))
                            self.mk.tableWidget.setItem(
                                rowIndex, 4, QtWidgets.QTableWidgetItem(i['adres']))
                            self.mk.tableWidget.setItem(
                                rowIndex, 5, QtWidgets.QTableWidgetItem(i['email']))
                            rowIndex += 1
                db.close()

        except Exception as err:
            print(str(err))

    def musterilist(self):
        try:
            global list
            a = self.mk.tableWidget.currentRow()
            xx = 0
            list = []
            z = 0
            while z < 6:
                if z == 6:
                    break
                else :
                    b = self.mk.tableWidget.item(a,xx)
                    list.append(b.text())
                    xx += 1
                z+=1
            
            self.mk.lineEdit_2.setText(list[1])
            self.mk.lineEdit_3.setText(list[2])
            self.mk.lineEdit_4.setText(list[3])
            self.mk.lineEdit_5.setText(list[4])
            self.mk.lineEdit_6.setText(list[5])



        except Exception as err:
            print(str(err))

    def musterignc(self):
        tc = self.mk.lineEdit_2.text()
        ad = self.mk.lineEdit_3.text()
        tel = self.mk.lineEdit_4.text()
        adres = self.mk.lineEdit_5.text()
        email = self.mk.lineEdit_6.text()
        db = mysql.connector.connect(host='127.0.0.1', user='root', password='mysql1234', database='stokotomasyon', charset='utf8')
        cur = db.cursor()
        sql = 'UPDATE musteriler set tc=%s,adsoyad=%s,tel=%s,adres=%s,email=%s Where idmusteriler=%s'
        values = (tc,ad,tel,adres,email,list[0])
        cur.execute(sql,values)
        result = QtWidgets.QMessageBox.information(self,"Onay Butonu","Güncellemeyi Onaylıyor musunuz ? ",QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        if result == QtWidgets.QMessageBox.Ok:
            db.commit()
            QtWidgets.QMessageBox.information(self,'Güncelleme Onayı','Müşteri Güncellendi.')
            tc = self.mk.lineEdit_2.clear()
            ad = self.mk.lineEdit_3.clear()
            tel = self.mk.lineEdit_4.clear()
            adres = self.mk.lineEdit_5.clear()
            email = self.mk.lineEdit_6.clear()
            db.close()
            self.musteridata()

    def musterisilme(self):
        a = self.mk.tableWidget.currentRow()
        xx = 0
        liste = []
        z = 0
        while z < 6:
            if z == 6:
                break
            else :
                b = self.mk.tableWidget.item(a,xx)
                liste.append(b.text())
                xx += 1
                print(liste)
            z+=1
        result = QtWidgets.QMessageBox.information(self,"Onay Butonu","Müşteriyi Silmeyi Onaylıyor musunuz ? ",QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        if result == QtWidgets.QMessageBox.Ok:
            db = mysql.connector.connect(host='127.0.0.1', user='root', password='mysql1234', database='stokotomasyon', charset='utf8')
            cur = db.cursor()
            sql = 'DELETE From musteriler Where idmusteriler = %s'
            value = (liste[0],)
            cur.execute(sql,value)
            db.commit()
            db.close()
            self.musteridata()




