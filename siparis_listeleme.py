from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui
from siparislist import Ui_MainWindow
import os
import sys
import mysql.connector


class SiparisL(QtWidgets.QMainWindow):
    def __init__(self):
        super(SiparisL, self).__init__()
        self.mk = Ui_MainWindow()
        self.mk.setupUi(self)
        self.siparisdata()

        self.mk.pushButton.clicked.connect(self.siparisSilme)
        self.mk.lineEdit.textChanged.connect(self.siparisdata)

    def siparisdata(self):
        try:
            textbox = self.mk.lineEdit.text()
            if textbox == "":
                db = mysql.connector.connect(
                    host='127.0.0.1', user='root', password='mysql1234', database='stokotomasyon', charset='utf8')
                cur = db.cursor()
                cur.execute("SELECT * FROM satislar")
                data = cur.fetchall()
                column = len(data[0])
                columCount = column-2
                self.mk.tableWidget.setRowCount(len(data))
                self.mk.tableWidget.setColumnCount(columCount)
                self.mk.tableWidget.setHorizontalHeaderLabels(("Id","Tc","Ad Soyad","Barkod No","Ürün Adı","Miktarı","Satış Fiyatı","Toplam Fiyatı"))

                rows = 0
                rowIndex = 0
                for re in data:
                    if rows != len(data):
                        are = [{
                            'idsatıslar': f'{re[0]}',
                            'tc': f'{re[1]}',
                            'adsoyad': f'{re[2]}',
                            'barkodno': f'{re[3]}',
                            'urunadi': f'{re[4]}',
                            'miktari': f'{re[5]}',
                            'satisfiyati': f'{re[6]}',
                            'toplamfiyati': f'{re[7]}'
                        }]

                        rows += 1

                        for i in are:
                            self.mk.tableWidget.setItem(
                                rowIndex, 0, QtWidgets.QTableWidgetItem(i['idsatıslar']))
                            self.mk.tableWidget.setItem(
                                rowIndex, 1, QtWidgets.QTableWidgetItem(i['tc']))
                            self.mk.tableWidget.setItem(
                                rowIndex, 2, QtWidgets.QTableWidgetItem(i['adsoyad']))
                            self.mk.tableWidget.setItem(
                                rowIndex, 3, QtWidgets.QTableWidgetItem(i['barkodno']))
                            self.mk.tableWidget.setItem(
                                rowIndex, 4, QtWidgets.QTableWidgetItem(i['urunadi']))
                            self.mk.tableWidget.setItem(
                                rowIndex, 5, QtWidgets.QTableWidgetItem(i['miktari']))
                            self.mk.tableWidget.setItem(
                                rowIndex, 6, QtWidgets.QTableWidgetItem(i['satisfiyati']))
                            self.mk.tableWidget.setItem(
                                rowIndex, 7, QtWidgets.QTableWidgetItem(i['toplamfiyati']))                            
                            rowIndex += 1
                db.close()
            else :
                db = mysql.connector.connect(host='127.0.0.1', user='root', password='mysql1234', database='stokotomasyon', charset='utf8')
                cur = db.cursor()
                cur.execute(f"SELECT * FROM satislar where tc LIKE '%{textbox}%'")
                data = cur.fetchall()
                column = len(data[0])

                columCount = column-2
                self.mk.tableWidget.setRowCount(len(data))
                self.mk.tableWidget.setColumnCount(columCount)
                self.mk.tableWidget.setHorizontalHeaderLabels(("Id","Tc","Ad Soyad","Barkod No","Ürün Adı","Miktarı","Satış Fiyatı","Toplam Fiyatı"))


                rows = 0
                rowIndex = 0
                for re in data:
                    if rows != len(data):
                        are = [{
                            'idsatıslar': f'{re[0]}',
                            'tc': f'{re[1]}',
                            'adsoyad': f'{re[2]}',
                            'barkodno': f'{re[3]}',
                            'urunadi': f'{re[4]}',
                            'miktari': f'{re[5]}',
                            'satisfiyati': f'{re[6]}',
                            'toplamfiyati': f'{re[7]}'
                        }]

                        rows += 1

                        for i in are:
                            self.mk.tableWidget.setItem(
                                rowIndex, 0, QtWidgets.QTableWidgetItem(i['idsatıslar']))
                            self.mk.tableWidget.setItem(
                                rowIndex, 1, QtWidgets.QTableWidgetItem(i['tc']))
                            self.mk.tableWidget.setItem(
                                rowIndex, 2, QtWidgets.QTableWidgetItem(i['adsoyad']))
                            self.mk.tableWidget.setItem(
                                rowIndex, 3, QtWidgets.QTableWidgetItem(i['barkodno']))
                            self.mk.tableWidget.setItem(
                                rowIndex, 4, QtWidgets.QTableWidgetItem(i['urunadi']))
                            self.mk.tableWidget.setItem(
                                rowIndex, 5, QtWidgets.QTableWidgetItem(i['miktari']))
                            self.mk.tableWidget.setItem(
                                rowIndex, 6, QtWidgets.QTableWidgetItem(i['satisfiyati']))
                            self.mk.tableWidget.setItem(
                                rowIndex, 7, QtWidgets.QTableWidgetItem(i['toplamfiyati']))                            
                            rowIndex += 1
                db.close()
        except Exception as err:
            print(str(err))

    def siparisSilme(self):
        try :
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
                z+=1
            result = QtWidgets.QMessageBox.information(self,"Onay Butonu","Müşteriyi Silmeyi Onaylıyor musunuz ? ",QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
            if result == QtWidgets.QMessageBox.Ok:
                db = mysql.connector.connect(host='127.0.0.1', user='root', password='mysql1234', database='stokotomasyon', charset='utf8')
                cur = db.cursor()
                cur.execute("Update urunlistesi set miktari=miktari+'"+liste[5]+"'where barkodno='"+liste[3]+"'")
                db.commit()
                sql = 'DELETE From satislar Where idsatıslar = %s'
                value = (liste[0],)
                cur.execute(sql,value)
                db.commit()
                db.close()
                self.mk.tableWidget.clear()
                self.siparisdata()
                QtWidgets.QMessageBox.information(self,'Sipariş Silinme','Sipariş İptal Edilmiştir.')
        except Exception :
            QtWidgets.QMessageBox.information(self,'Hata','Sipariş yok yada seçim yapmadınız.')
            self.siparisdata()




