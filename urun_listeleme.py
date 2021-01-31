from PyQt5 import QtCore, QtGui, QtWidgets
from urunlistesi import Ui_MainWindow
import os
import sys
import mysql.connector
import datetime



class urunL(QtWidgets.QMainWindow):
    def __init__(self):
        super(urunL,self).__init__()
        self.uL = Ui_MainWindow()
        self.uL.setupUi(self)
        self.urundata()

        self.uL.lineEdit.textChanged.connect(self.urundata)
        self.uL.tableWidget.doubleClicked.connect(self.urunlist)
        self.uL.pushButton_2.clicked.connect(self.urunGnc)
        self.uL.pushButton.clicked.connect(self.urunsilme)


    def urundata(self):
        try :
            textbox = self.uL.lineEdit.text()
            if textbox == "":
                connection = mysql.connector.connect(host='127.0.0.1', user='root', password='mysql1234', database='stokotomasyon', charset='utf8')
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM urunlistesi")
                data = cursor.fetchall()
                column = len(data[0])

                self.uL.tableWidget.setColumnCount(column)
                self.uL.tableWidget.setRowCount(len(data))
                self.uL.tableWidget.setHorizontalHeaderLabels([i[0] for i in cursor.description])

                rows = 0
                rowIndex = 0
                for re in data :
                    if rows != len(data):
                        are = [{
                            "barkodno" : f"{re[0]}",
                            "kategori" : f"{re[1]}",
                            "marka" : f"{re[2]}",
                            "urunadı" : f"{re[3]}",
                            "miktari" : f"{re[4]}",
                            "alisfiyati" : f"{re[5]}",
                            "satisfiyati" : f"{re[6]}",
                            "tarih" : f"{re[7]}"
                        }]
    
                        rows+=1
                        for i in are :
                            self.uL.tableWidget.setItem(rowIndex,0,QtWidgets.QTableWidgetItem(i["barkodno"]))
                            self.uL.tableWidget.setItem(rowIndex,1,QtWidgets.QTableWidgetItem(i["kategori"]))
                            self.uL.tableWidget.setItem(rowIndex,2,QtWidgets.QTableWidgetItem(i["marka"]))
                            self.uL.tableWidget.setItem(rowIndex,3,QtWidgets.QTableWidgetItem(i["urunadı"]))
                            self.uL.tableWidget.setItem(rowIndex,4,QtWidgets.QTableWidgetItem(i["miktari"]))
                            self.uL.tableWidget.setItem(rowIndex,5,QtWidgets.QTableWidgetItem(i["alisfiyati"]))
                            self.uL.tableWidget.setItem(rowIndex,6,QtWidgets.QTableWidgetItem(i["satisfiyati"]))
                            self.uL.tableWidget.setItem(rowIndex,7,QtWidgets.QTableWidgetItem(i["tarih"]))
                            rowIndex+=1
            else :
                connection = mysql.connector.connect(host='127.0.0.1', user='root', password='mysql1234', database='stokotomasyon', charset='utf8')
                cursor = connection.cursor()
                cursor.execute(f"SELECT * FROM urunlistesi where barkodno LIKE '%{textbox}%'")
                data = cursor.fetchall()
                column = len(data[0])

                self.uL.tableWidget.setColumnCount(column)
                self.uL.tableWidget.setRowCount(len(data))
                self.uL.tableWidget.setHorizontalHeaderLabels([i[0] for i in cursor.description])

                rows = 0
                rowIndex = 0
                for re in data :
                    if rows != len(data):
                        are = [{
                            "barkodno" : f"{re[0]}",
                            "kategori" : f"{re[1]}",
                            "marka" : f"{re[2]}",
                            "urunadı" : f"{re[3]}",
                            "miktari" : f"{re[4]}",
                            "alisfiyati" : f"{re[5]}",
                            "satisfiyati" : f"{re[6]}",
                            "tarih" : f"{re[7]}"
                        }]
    
                        rows+=1
                        for i in are :
                            self.uL.tableWidget.setItem(rowIndex,0,QtWidgets.QTableWidgetItem(i["barkodno"]))
                            self.uL.tableWidget.setItem(rowIndex,1,QtWidgets.QTableWidgetItem(i["kategori"]))
                            self.uL.tableWidget.setItem(rowIndex,2,QtWidgets.QTableWidgetItem(i["marka"]))
                            self.uL.tableWidget.setItem(rowIndex,3,QtWidgets.QTableWidgetItem(i["urunadı"]))
                            self.uL.tableWidget.setItem(rowIndex,4,QtWidgets.QTableWidgetItem(i["miktari"]))
                            self.uL.tableWidget.setItem(rowIndex,5,QtWidgets.QTableWidgetItem(i["alisfiyati"]))
                            self.uL.tableWidget.setItem(rowIndex,6,QtWidgets.QTableWidgetItem(i["satisfiyati"]))
                            self.uL.tableWidget.setItem(rowIndex,7,QtWidgets.QTableWidgetItem(i["tarih"]))
                            rowIndex+=1

                connection.close()
        except Exception as err:
            print(str(err))

    def urunlist(self):
        try :
            global list
            self.loadcombo()
            a = self.uL.tableWidget.currentRow()
            xx = 0
            list=[]
            z = 0
            while z < 7 :
                if z == 7:
                    break
                else:
                    item = self.uL.tableWidget.item(a,xx)
                    list.append(item.text())
                    xx+=1
                z+=1
            print(list)
            self.uL.lineEdit_2.setText(list[0])
            self.uL.comboBox.setCurrentText(list[1])
            self.uL.comboBox_2.setCurrentText(list[2])
            self.uL.lineEdit_5.setText(list[3])
            self.uL.lineEdit_6.setText(list[4])
            self.uL.lineEdit_7.setText(list[5])
            self.uL.lineEdit_8.setText(list[6])

        except Exception as err:
            print(str(err))

    def loadcombo(self):
        self.uL.comboBox.clear()
        self.uL.comboBox_2.clear()
        connection = mysql.connector.connect(host='127.0.0.1',user='root',password='mysql1234',database='stokotomasyon')
        cursor = connection.cursor()

        cursor.execute("SELECT * From kategori_bilgileri")
        a = cursor.fetchall()
        for i in a :
            self.uL.comboBox.addItems(i)
        connection.close()

        connection = mysql.connector.connect(host='127.0.0.1',user='root',password='mysql1234',database='stokotomasyon')
        cursor = connection.cursor()

        cursor.execute("SELECT * From marka_bilgileri")
        a = cursor.fetchall()
        list = []
        for i in a :
            list.append(i[1])
        
        self.uL.comboBox_2.addItems(list)
        connection.close()

    def urunGnc(self):
        barkodno = self.uL.lineEdit_2.text()
        kategori = self.uL.comboBox.currentText()
        marka = self.uL.comboBox_2.currentText()
        urunadı = self.uL.lineEdit_5.text()
        miktar = self.uL.lineEdit_6.text()
        alısfiyati = self.uL.lineEdit_7.text()
        satisfiyati = self.uL.lineEdit_8.text()

        db = mysql.connector.connect(host='127.0.0.1', user='root', password='mysql1234', database='stokotomasyon', charset='utf8')
        cur = db.cursor()
        sql = 'UPDATE urunlistesi set barkodno=%s,kategori=%s,marka=%s,urunadı=%s,miktari=%s,alisfiyati=%s,satisfiyati=%s Where barkodno=%s'
        values = (barkodno,kategori,marka,urunadı,miktar,alısfiyati,satisfiyati,list[0])
        cur.execute(sql,values)
        result = QtWidgets.QMessageBox.information(self,"Onay Butonu","Güncellemeyi Onaylıyor musunuz ? ",QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        if result == QtWidgets.QMessageBox.Ok:
            db.commit()
            QtWidgets.QMessageBox.information(self,'Güncelleme Onayı','Ürün Güncellendi.')
            self.uL.lineEdit_2.clear()
            self.uL.lineEdit_5.clear()
            self.uL.lineEdit_6.clear()
            self.uL.lineEdit_7.clear()
            self.uL.lineEdit_8.clear()
            self.uL.comboBox_2.clear()
            self.uL.comboBox.clear()
            db.close()
            self.urundata()

    def urunsilme(self):
        sltablo = self.uL.tableWidget.currentRow()
        xx = 0
        liste = []
        z = 0
        while z < 7 :
            if z == 6 :
                break
            else:
                b = self.uL.tableWidget.item(sltablo,xx)
                liste.append(b.text())
                xx+=1
            z+=1
        result = QtWidgets.QMessageBox.information(self,"Onay Butonu","Ürünü Silmeyi Onaylıyor musunuz ? ",QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        if result == QtWidgets.QMessageBox.Ok:
            db = mysql.connector.connect(host='127.0.0.1', user='root', password='mysql1234', database='stokotomasyon', charset='utf8')
            cur = db.cursor()
            sql = 'DELETE From urunlistesi Where barkodno = %s'
            value = (liste[0],)
            cur.execute(sql,value)
            db.commit()
            db.close()
            self.urundata()







