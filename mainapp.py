################################################
################################################
################################################
#########*******###*******####**********########
########**#####**#**#####**###**######**########
########**#####**#**#####**###**######**########
########**#####**#**#####**###**********########
########**#####**#**#####**###**################
########**#####**#**#####**###**################
########**######***######**###**################
########**###############**###**################
########**###############**###**################
################################################
########Copyright © Maresal Programming#########
################################################

from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui
from msf import Ui_MainWindow as w
import os 
import sys
from musteriekle import musteriEk
from musterilistele import Mek
from kategori_marka import kateMarka
from urun_ekleme import urunEkl
from urun_listeleme import urunL
import mysql.connector
import time
import datetime
from siparis_listeleme import SiparisL

class mse(QtWidgets.QMainWindow):
    def __init__(self):
        super(mse,self).__init__()
        self.ms = w()
        self.ms.setupUi(self)
        self.show()
        
        
        self.ms.pushButton.clicked.connect(self.musteriekleac)
        self.ms.pushButton_2.clicked.connect(self.musterilist)
        self.ms.pushButton_12.clicked.connect(self.ktgandMar)
        self.ms.pushButton_3.clicked.connect(self.urunekleme)
        self.ms.pushButton_4.clicked.connect(self.urunlist)
        self.ms.lineEdit.textChanged.connect(self.MIs)
        self.ms.lineEdit_4.textChanged.connect(self.UGs)
        self.ms.lineEdit_6.textChanged.connect(self.hesap)
        self.ms.pushButton_10.clicked.connect(self.sepeteekle)
        self.ms.pushButton_7.clicked.connect(self.sepetsil)
        self.ms.pushButton_8.clicked.connect(self.siparisiptal)
        self.ms.pushButton_9.clicked.connect(self.siparisonay)
        self.ms.pushButton_5.clicked.connect(self.siparislist)
    

    def musteriekleac(self):
        self.mte = musteriEk()
        self.mte.show()

    def musterilist(self):
        self.ml = Mek()
        self.ml.show()
    
    def ktgandMar(self):
        self.ktm = kateMarka()
        self.ktm.show()

    def urunekleme(self):
        self.ure = urunEkl()
        self.ure.show()
    
    def urunlist(self):
        self.ulist = urunL()
        self.ulist.show()

    def MIs(self):
        try :
            textm = self.ms.lineEdit.text()
            db = mysql.connector.connect(host='127.0.0.1', user='root', password='mysql1234', database='stokotomasyon', charset='utf8')
            cur = db.cursor()
            cur.execute(f"SELECT * FROM musteriler where tc LIKE '%{textm}%'")
            data = cur.fetchone()
            if textm == data[1]:
                self.ms.lineEdit_2.setText(data[2])
                self.ms.lineEdit_3.setText(data[3])
            else :
                self.ms.lineEdit_2.clear()
                self.ms.lineEdit_3.clear()
            cur.close()
            db.close()
        except Exception:
            pass
            
    def UGs(self):
        try :
            barkodNo = self.ms.lineEdit_4.text()
            db = mysql.connector.connect(host='127.0.0.1', user='root', password='mysql1234', database='stokotomasyon', charset='utf8')
            cur = db.cursor()
            cur.execute(f"SELECT * FROM urunlistesi where barkodno LIKE '%{barkodNo}%'")
            data = cur.fetchone()
            print(data[0],data[3],data[4],data[6])
            if barkodNo == str(data[0]):
                self.ms.lineEdit_5.setText(str(data[3]))
                self.ms.lineEdit_7.setText(str(data[6]))
                self.hesap()
            else :
                self.ms.lineEdit_5.clear()
                self.ms.lineEdit_6.clear()
                self.ms.lineEdit_7.clear()
                self.ms.lineEdit_8.clear()
            db.close()
        except Exception as err:
            print(str(err))

    def hesap(self):
        try:
            miktar = self.ms.lineEdit_6.text()
            aF = self.ms.lineEdit_7.text()
            hesap = float(miktar) * float(aF)
            self.ms.lineEdit_8.setText(str(hesap))
        except Exception as err :
            print(err)

    def sepeteekle(self):
        try :
            tc = self.ms.lineEdit.text()
            urunadi = self.ms.lineEdit_5.text()
            miktar = self.ms.lineEdit_6.text()
            satisF = self.ms.lineEdit_7.text()
            barkodNo = self.ms.lineEdit_4.text()
            adsoyad = self.ms.lineEdit_2.text()
            toplam = self.ms.lineEdit_8.text()
            
            if self.barkodkont() == None:
                connection = mysql.connector.connect(host='127.0.0.1',user='root',password='mysql1234',database='stokotomasyon')
                cursor = connection.cursor()
                sql = "INSERT INTO sepet(tc,adsoyad,barkodno,urunadi,miktari,satısfiyati,toplamfiyati) VALUES (%s,%s,%s,%s,%s,%s,%s)"
                values = (tc,adsoyad,barkodNo,urunadi,miktar,satisF,toplam)
                cursor.execute(sql,values)
                connection.commit()
                cursor.close()
                connection.close()
                self.loadsepet()
            else :
                connection = mysql.connector.connect(host='127.0.0.1',user='root',password='mysql1234',database='stokotomasyon')
                cursor = connection.cursor()
                cursor.execute(f"Update sepet set miktari=miktari+{miktar} where barkodno={barkodNo}")
                cursor.execute("Update sepet set toplamfiyati=miktari*satısfiyati where barkodno='"+barkodNo+"'")
                connection.commit()
                self.ms.tableWidget.clear()
                cursor.close()
                connection.close()
                self.loadsepet()

            self.ms.lineEdit_5.clear()
            self.ms.lineEdit_7.clear()
            self.ms.lineEdit_4.clear()
            self.ms.lineEdit_8.clear()
            self.ms.lineEdit_6.setText("1")
        except Exception as err :
            print(str(err))
        
    def loadsepet(self):
        try :
            tc = self.ms.lineEdit.text()
            db = mysql.connector.connect(
                host='127.0.0.1', user='root', password='mysql1234', database='stokotomasyon', charset='utf8')
            cur = db.cursor()
            cur.execute(f"SELECT * FROM sepet where tc LIKE '%{tc}%'")
            data = cur.fetchall()
            column = len(data[0])
            self.ms.tableWidget.setRowCount(len(data))
            self.ms.tableWidget.setColumnCount(column)
            self.ms.tableWidget.setHorizontalHeaderLabels(("TC","Ad Soyad","Barkod No","Ürün Adı","Miktar","Satış Fiyatı","Toplam"))

            rows = 0
            rowIndex = 0
            list = []
            for re in data:
                if rows != len(data):
                    are = [{
                        'tc': f'{re[0]}',
                        'adsoyad': f'{re[1]}',
                        'barkodno': f'{re[2]}',
                        'urunadi': f'{re[3]}',
                        'miktari': f'{re[4]}',
                        'satısfiyati': f'{re[5]}',
                        'toplam':f'{re[6]}'
                        }]

                    list.append(float(data[rows][6]))
                    rows += 1

                    for i in are:
                        self.ms.tableWidget.setItem(
                                rowIndex, 0, QtWidgets.QTableWidgetItem(i['tc']))
                        self.ms.tableWidget.setItem(
                                rowIndex, 1, QtWidgets.QTableWidgetItem(i['adsoyad']))
                        self.ms.tableWidget.setItem(
                                rowIndex, 2, QtWidgets.QTableWidgetItem(i['barkodno']))
                        self.ms.tableWidget.setItem(
                                rowIndex, 3, QtWidgets.QTableWidgetItem(i['urunadi']))
                        self.ms.tableWidget.setItem(
                                rowIndex, 4, QtWidgets.QTableWidgetItem(i['miktari']))
                        self.ms.tableWidget.setItem(
                                rowIndex, 5, QtWidgets.QTableWidgetItem(i['satısfiyati']))
                        self.ms.tableWidget.setItem(
                                rowIndex, 6, QtWidgets.QTableWidgetItem(i['toplam']))
                        rowIndex += 1
            self.ms.label_9.setText(f"Genel Toplam : {round(sum(list),2)} TL")
            print(list)
            db.close()
        except Exception as err:
            print(str(err))

    def barkodkont(self):
        try :
            br = self.ms.lineEdit_4.text()
            db = mysql.connector.connect(
                host='127.0.0.1', user='root', password='mysql1234', database='stokotomasyon', charset='utf8')
            cur = db.cursor()
            cur.execute(f"SELECT * FROM sepet where barkodno={br}")
            data = cur.fetchone()
            print(data)
            if data[2] == br :
                return True
            else :
                return False

                

            cur.close()
            db.close()
        except Exception :
            pass
            
    def sepetsil(self):
        try :
            a = self.ms.tableWidget.currentRow()
            xx = 0
            liste = []
            z = 0
            while z < 6:
                if z == 6:
                    break
                else :
                    b = self.ms.tableWidget.item(a,xx)
                    liste.append(b.text())
                    xx += 1
                z+=1
            result = QtWidgets.QMessageBox.information(self,"Onay Butonu","Sepetten Silinicek Onaylıyor musunuz ? ",QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
            if result == QtWidgets.QMessageBox.Ok:
                db = mysql.connector.connect(host='127.0.0.1', user='root', password='mysql1234', database='stokotomasyon', charset='utf8')
                cur = db.cursor()
                sql = 'DELETE From sepet Where barkodno = %s'
                value = (liste[2],)
                cur.execute(sql,value)
                db.commit()
                db.close()
                self.ms.tableWidget.removeRow(a)
            self.loadsepet()
        except Exception:
            pass

    def siparisiptal(self):
        tc = self.ms.lineEdit.text()
        result = QtWidgets.QMessageBox.information(self,"Onay Butonu","Sipariş iptal edilecek.Onaylıyor musunuz ? ",QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        if result == QtWidgets.QMessageBox.Ok:
            db = mysql.connector.connect(host='127.0.0.1', user='root', password='mysql1234', database='stokotomasyon', charset='utf8')
            cur = db.cursor()
            sql = 'DELETE From sepet Where tc = %s'
            value = (tc,)
            cur.execute(sql,value)
            db.commit()
            db.close()
            self.ms.tableWidget.clear()
            self.ms.label_9.setText("Genel Toplam :")

    def siparisonay(self):
        try:
            a = self.ms.tableWidget.rowCount()
            list = []
            bugun = datetime.datetime.now()
            result = QtWidgets.QMessageBox.information(self,"Onay Butonu","Sipariş Kaydedilecek.Onaylıyor musunuz ? ",QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
            if result == QtWidgets.QMessageBox.Ok:
                for row in range(a):
                    for col in range(7):
                        item = self.ms.tableWidget.item(row, col)
                        list.append(item.text())
                        col+=1
                    connection = mysql.connector.connect(host='127.0.0.1',user='root',password='mysql1234',database='stokotomasyon')
                    cursor = connection.cursor()
                    sql = "INSERT INTO satislar(tc,adsoyad,barkodno,urunadi,miktari,satısfiyati,toplamfiyati,tarih) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
                    values = (list[0],list[1],list[2],list[3],list[4],list[5],list[6],bugun)
                    cursor.execute(sql,values)
                    connection.commit()
                    cursor.execute("Update urunlistesi set miktari=miktari-'"+list[4]+"' where barkodno='"+list[2]+"'")
                    connection.commit()
                    cursor.close()
                    list.clear()
                    row+=1
                self.sepettemizle()
            QtWidgets.QMessageBox.information(self,'Sipariş Kaydı','Sipariş Kaydedildi.')
        except Exception as err:
            print(str(err))

    def sepettemizle(self):
        tc = self.ms.lineEdit.text()
        db = mysql.connector.connect(host='127.0.0.1', user='root', password='mysql1234', database='stokotomasyon', charset='utf8')
        cur = db.cursor()
        sql = 'DELETE From sepet Where tc = %s'
        value = (tc,)
        cur.execute(sql,value)
        db.commit()
        db.close()
        self.ms.tableWidget.clearMask()
        self.ms.tableWidget.clear()
        self.ms.label_9.setText("Genel Toplam :")
        self.ms.lineEdit.clear()
        self.ms.lineEdit_2.clear()
        self.ms.lineEdit_3.clear()

    def siparislist(self):
        self.sl = SiparisL()
        self.sl.show()












if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = mse()
    app.setStyle('Fusion')
    app.exit(app.exec_())


        
