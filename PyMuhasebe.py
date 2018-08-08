#!/usr/bin/python
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pr2.ui'
#
# Created: Fri Jul 20 09:57:06 2018
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import locale
import cx_Oracle
from datetime import datetime

bul=[]
productAmount = {}
salesAmount={}
locale.setlocale(locale.LC_ALL, 'Turkish_Turkey.1254')
# DB Connection
user='HR'
passw='Password'
host='localhost'
service='xe'
con = cx_Oracle.connect(user+'/'+passw+'@'+host+'/'+service,encoding="UTF-8", nencoding="UTF-8")
print 'oracle versiyon: ' + con.version
# DB Connection

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8


    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(599, 769)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setIconSize(QtCore.QSize(50, 35))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.urun_tab = QtGui.QWidget()
        self.urun_tab.setEnabled(True)
        self.urun_tab.setObjectName(_fromUtf8("urun_tab"))
        self.toolBox = QtGui.QToolBox(self.urun_tab)
        self.toolBox.setGeometry(QtCore.QRect(0, 0, 571, 691))
        self.toolBox.setObjectName(_fromUtf8("toolBox"))
        self.urun_kutusu = QtGui.QWidget()
        self.urun_kutusu.setGeometry(QtCore.QRect(0, 0, 571, 629))
        self.urun_kutusu.setObjectName(_fromUtf8("urun_kutusu"))
        self.urun_liste = QtGui.QTableWidget(self.urun_kutusu)
        self.urun_liste.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.urun_liste.setGeometry(QtCore.QRect(0, -10, 571, 651))
        self.urun_liste.setObjectName(_fromUtf8("urun_liste"))
        self.urun_liste.setColumnCount(5)
        self.urun_liste.setRowCount(500)
        self.toolBox.addItem(self.urun_kutusu, _fromUtf8(""))
        self.urun_ekle = QtGui.QWidget()
        self.urun_ekle.setGeometry(QtCore.QRect(0, 0, 571, 629))
        self.urun_ekle.setObjectName(_fromUtf8("urun_ekle"))
        self.gridLayoutWidget = QtGui.QWidget(self.urun_ekle)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 0, 491, 204))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.urun_adet = QtGui.QLineEdit(self.gridLayoutWidget)
        self.urun_adet.setObjectName(_fromUtf8("urun_adet"))
        self.gridLayout_2.addWidget(self.urun_adet, 6, 2, 1, 1)
        self.label_16 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.gridLayout_2.addWidget(self.label_16, 6, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 5, 0, 1, 1)
        self.label = QtGui.QLabel(self.gridLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.urun_alim_fiyat = QtGui.QLineEdit(self.gridLayoutWidget)
        self.urun_alim_fiyat.setReadOnly(True)
        self.urun_alim_fiyat.setObjectName(_fromUtf8("urun_alim_fiyat"))
        self.gridLayout_2.addWidget(self.urun_alim_fiyat, 5, 2, 1, 1)
        self.label_3 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
        self.urun_adi = QtGui.QComboBox(self.gridLayoutWidget)
        self.urun_adi.setObjectName(_fromUtf8("urun_adi"))
        self.urun_adi.currentIndexChanged.connect(self.productOnActivated)
        self.gridLayout_2.addWidget(self.urun_adi, 0, 2, 1, 1)
        self.urun_kaydet = QtGui.QPushButton(self.gridLayoutWidget)
        self.urun_kaydet.setObjectName(_fromUtf8("urun_kaydet"))
        self.urun_kaydet.clicked.connect(self.alimyap)  # Reassign Qlabel
        self.gridLayout_2.addWidget(self.urun_kaydet, 7, 2, 1, 1)
        self.urun_tedarikci = QtGui.QComboBox(self.gridLayoutWidget)
        self.urun_tedarikci.setObjectName(_fromUtf8("urun_tedarikci"))
        self.urun_tedarikci.currentIndexChanged.connect(self.supplierOnActivated)  # Reassign Qlabel
        self.gridLayout_2.addWidget(self.urun_tedarikci, 2, 2, 1, 1)
        self.toolBox.addItem(self.urun_ekle, _fromUtf8(""))
        self.tabWidget.addTab(self.urun_tab, _fromUtf8(""))
        self.musteri_tab = QtGui.QWidget()
        self.musteri_tab.setEnabled(True)
        self.musteri_tab.setObjectName(_fromUtf8("musteri_tab"))
        self.toolBox_2 = QtGui.QToolBox(self.musteri_tab)
        self.toolBox_2.setGeometry(QtCore.QRect(0, 0, 571, 691))
        self.toolBox_2.setObjectName(_fromUtf8("toolBox_2"))
        self.musteri_kutusu = QtGui.QWidget()
        self.musteri_kutusu.setGeometry(QtCore.QRect(0, 0, 571, 629))
        self.musteri_kutusu.setObjectName(_fromUtf8("musteri_kutusu"))
        self.musteri_liste = QtGui.QTableWidget(self.musteri_kutusu)
        self.musteri_liste.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.musteri_liste.setGeometry(QtCore.QRect(0, 0, 571, 631))
        self.musteri_liste.setObjectName(_fromUtf8("musteri_liste"))
        self.musteri_liste.setColumnCount(2)
        self.musteri_liste.setRowCount(500)
        self.toolBox_2.addItem(self.musteri_kutusu, _fromUtf8(""))
        self.musteri_ekle = QtGui.QWidget()
        self.musteri_ekle.setGeometry(QtCore.QRect(0, 0, 571, 629))
        self.musteri_ekle.setObjectName(_fromUtf8("musteri_ekle"))
        self.gridLayoutWidget_2 = QtGui.QWidget(self.musteri_ekle)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 0, 551, 150))
        self.gridLayoutWidget_2.setObjectName(_fromUtf8("gridLayoutWidget_2"))
        self.gridLayout_3 = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_3.setMargin(0)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_6 = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_3.addWidget(self.label_6, 1, 0, 1, 1)
        self.musteri_adi = QtGui.QLineEdit(self.gridLayoutWidget_2)
        self.musteri_adi.setObjectName(_fromUtf8("musteri_adi"))
        self.gridLayout_3.addWidget(self.musteri_adi, 0, 2, 1, 1)
        self.musteri_bolge = QtGui.QComboBox(self.gridLayoutWidget_2)
        self.musteri_bolge.setObjectName(_fromUtf8("musteri_bolge"))
        self.gridLayout_3.addWidget(self.musteri_bolge, 1, 2, 1, 1)
        self.label_5 = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_3.addWidget(self.label_5, 0, 0, 1, 1)
        self.musteri_kaydet = QtGui.QPushButton(self.gridLayoutWidget_2)
        self.musteri_kaydet.setObjectName(_fromUtf8("musteri_kaydet"))
        self.musteri_kaydet.clicked.connect(self.musteriekle)
        self.gridLayout_3.addWidget(self.musteri_kaydet, 2, 2, 1, 1)
        self.mesaj = QtGui.QLabel(self.gridLayoutWidget_2)
        self.mesaj.setObjectName(_fromUtf8("label"))
        self.gridLayout_3.addWidget(self.mesaj, 3, 2, 1, 1)
        self.toolBox_2.addItem(self.musteri_ekle, _fromUtf8(""))
        self.tabWidget.addTab(self.musteri_tab, _fromUtf8(""))
        self.satis_tab = QtGui.QWidget()
        self.satis_tab.setObjectName(_fromUtf8("satis_tab"))
        self.toolBox_5 = QtGui.QToolBox(self.satis_tab)
        self.toolBox_5.setGeometry(QtCore.QRect(0, 0, 571, 691))
        self.toolBox_5.setObjectName(_fromUtf8("toolBox_5"))
        self.satis_kutusu = QtGui.QWidget()
        self.satis_kutusu.setGeometry(QtCore.QRect(0, 0, 571, 629))
        self.satis_kutusu.setObjectName(_fromUtf8("satis_kutusu"))
        self.satis_liste = QtGui.QTableWidget(self.satis_kutusu)
        self.satis_liste.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.satis_liste.setGeometry(QtCore.QRect(0, 0, 571, 631))
        self.satis_liste.setObjectName(_fromUtf8("satis_liste"))
        self.satis_liste.setColumnCount(5)
        self.satis_liste.setRowCount(500)
        self.toolBox_5.addItem(self.satis_kutusu, _fromUtf8(""))
        self.satis_ekle = QtGui.QWidget()
        self.satis_ekle.setGeometry(QtCore.QRect(0, 0, 571, 629))
        self.satis_ekle.setObjectName(_fromUtf8("satis_ekle"))
        self.gridLayoutWidget_3 = QtGui.QWidget(self.satis_ekle)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 0, 541, 251))
        self.gridLayoutWidget_3.setObjectName(_fromUtf8("gridLayoutWidget_3"))
        self.gridLayout_4 = QtGui.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_4.setMargin(0)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.label_9 = QtGui.QLabel(self.gridLayoutWidget_3)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout_4.addWidget(self.label_9, 2, 0, 1, 1)
        self.label_11 = QtGui.QLabel(self.gridLayoutWidget_3)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout_4.addWidget(self.label_11, 4, 0, 1, 1)
        self.musteri_sec = QtGui.QComboBox(self.gridLayoutWidget_3)
        self.musteri_sec.setObjectName(_fromUtf8("musteri_sec"))
        self.gridLayout_4.addWidget(self.musteri_sec, 0, 2, 1, 1)
        self.label_10 = QtGui.QLabel(self.gridLayoutWidget_3)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_4.addWidget(self.label_10, 1, 0, 1, 1)
        self.label_8 = QtGui.QLabel(self.gridLayoutWidget_3)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_4.addWidget(self.label_8, 0, 0, 1, 1)
        self.satis_adet = QtGui.QLineEdit(self.gridLayoutWidget_3)
        self.satis_adet.setObjectName(_fromUtf8("satis_adet"))
        self.gridLayout_4.addWidget(self.satis_adet, 4, 2, 1, 1)
        self.satis_fiyat = QtGui.QLineEdit(self.gridLayoutWidget_3)
        self.satis_fiyat.setReadOnly(True)
        self.satis_fiyat.setObjectName(_fromUtf8("satis_fiyat"))
        self.gridLayout_4.addWidget(self.satis_fiyat, 2, 2, 1, 1)
        self.satis_kaydet = QtGui.QPushButton(self.gridLayoutWidget_3)
        self.satis_kaydet.setObjectName(_fromUtf8("satis_kaydet"))
        self.satis_kaydet.clicked.connect(self.satisyap)
        self.gridLayout_4.addWidget(self.satis_kaydet, 5, 2, 1, 1)
        self.satis_urunsec = QtGui.QComboBox(self.gridLayoutWidget_3)
        self.satis_urunsec.currentIndexChanged.connect(self.saleproductOnActivated)
        self.satis_urunsec.setObjectName(_fromUtf8("satis_urunsec"))
        self.gridLayout_4.addWidget(self.satis_urunsec, 1, 2, 1, 1)
        self.toolBox_5.addItem(self.satis_ekle, _fromUtf8(""))
        self.tabWidget.addTab(self.satis_tab, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.tedarikci_tab = QtGui.QWidget()
        self.tedarikci_tab.setObjectName(_fromUtf8("tedarikci_tab"))
        self.toolBox_3 = QtGui.QToolBox(self.tedarikci_tab)
        self.toolBox_3.setGeometry(QtCore.QRect(0, 0, 571, 691))
        self.toolBox_3.setObjectName(_fromUtf8("toolBox_3"))
        self.tedarikci_kutusu = QtGui.QWidget()
        self.tedarikci_kutusu.setGeometry(QtCore.QRect(0, 0, 571, 629))
        self.tedarikci_kutusu.setObjectName(_fromUtf8("tedarikci_kutusu"))
        self.tedarikciler_listesi = QtGui.QTableWidget(self.tedarikci_kutusu)
        self.tedarikciler_listesi.setGeometry(QtCore.QRect(0, 0, 571, 631))
        self.tedarikciler_listesi.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tedarikciler_listesi.setObjectName(_fromUtf8("tedarikciler_listesi"))
        self.tedarikciler_listesi.setColumnCount(1)
        self.tedarikciler_listesi.setRowCount(500)
        self.toolBox_3.addItem(self.tedarikci_kutusu, _fromUtf8(""))
        self.tedarikci_ekleme_kutusu = QtGui.QWidget()
        self.tedarikci_ekleme_kutusu.setGeometry(QtCore.QRect(0, 0, 98, 28))
        self.tedarikci_ekleme_kutusu.setObjectName(_fromUtf8("tedarikci_ekleme_kutusu"))
        self.gridLayoutWidget_4 = QtGui.QWidget(self.tedarikci_ekleme_kutusu)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(20, 20, 531, 151))
        self.gridLayoutWidget_4.setObjectName(_fromUtf8("gridLayoutWidget_4"))
        self.gridLayout_5 = QtGui.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_5.setMargin(0)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.lineEdit = QtGui.QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout_5.addWidget(self.lineEdit, 0, 2, 1, 1)
        self.label_12 = QtGui.QLabel(self.gridLayoutWidget_4)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout_5.addWidget(self.label_12, 0, 0, 1, 1)
        self.pushButton = QtGui.QPushButton(self.gridLayoutWidget_4)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.clicked.connect(dbAddSupplier)
        self.gridLayout_5.addWidget(self.pushButton, 2, 2, 1, 1)
        self.toolBox_3.addItem(self.tedarikci_ekleme_kutusu, _fromUtf8(""))
        self.tabWidget.addTab(self.tedarikci_tab, _fromUtf8(""))
        self.tarife = QtGui.QWidget()
        self.tarife.setObjectName(_fromUtf8("tarife"))
        self.toolBox_4 = QtGui.QToolBox(self.tarife)
        self.toolBox_4.setGeometry(QtCore.QRect(0, 0, 571, 691))
        self.toolBox_4.setObjectName(_fromUtf8("toolBox_4"))
        self.alim_tarife = QtGui.QWidget()
        self.alim_tarife.setGeometry(QtCore.QRect(0, 0, 98, 28))
        self.alim_tarife.setObjectName(_fromUtf8("alim_tarife"))
        self.alis_tarife_liste = QtGui.QTableWidget(self.alim_tarife)
        self.alis_tarife_liste.setGeometry(QtCore.QRect(0, 0, 571, 561))
        self.alis_tarife_liste.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.alis_tarife_liste.setObjectName(_fromUtf8("alis_tarife_liste"))
        self.alis_tarife_liste.setColumnCount(5)
        self.alis_tarife_liste.setRowCount(500)
        self.toolBox_4.addItem(self.alim_tarife, _fromUtf8(""))
        self.alim_tarife_ekle = QtGui.QWidget()
        self.alim_tarife_ekle.setGeometry(QtCore.QRect(0, 0, 98, 28))
        self.alim_tarife_ekle.setObjectName(_fromUtf8("alim_tarife_ekle"))
        self.gridLayoutWidget_5 = QtGui.QWidget(self.alim_tarife_ekle)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(20, 10, 521, 161))
        self.gridLayoutWidget_5.setObjectName(_fromUtf8("gridLayoutWidget_5"))
        self.gridLayout_6 = QtGui.QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_6.setMargin(0)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.alim_tarife_urun = QtGui.QComboBox(self.gridLayoutWidget_5)
        self.alim_tarife_urun.setObjectName(_fromUtf8("alim_tarife_urun"))
        self.alim_tarife_urun.currentIndexChanged.connect(self.productPriceOnActivated)
        self.gridLayout_6.addWidget(self.alim_tarife_urun, 0, 1, 1, 1)
        self.label_14 = QtGui.QLabel(self.gridLayoutWidget_5)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.gridLayout_6.addWidget(self.label_14, 0, 0, 1, 1)
        self.label_15 = QtGui.QLabel(self.gridLayoutWidget_5)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.gridLayout_6.addWidget(self.label_15, 2, 0, 1, 1)
        self.alim_tarife_fiyat = QtGui.QLineEdit(self.gridLayoutWidget_5)
        self.alim_tarife_fiyat.setObjectName(_fromUtf8("alim_tarife_fiyat"))
        self.gridLayout_6.addWidget(self.alim_tarife_fiyat, 2, 1, 1, 1)
        self.label_18 = QtGui.QLabel(self.gridLayoutWidget_5)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.gridLayout_6.addWidget(self.label_18, 1, 0, 1, 1)
        self.alim_tarife_tedarikci = QtGui.QComboBox(self.gridLayoutWidget_5)
        self.alim_tarife_tedarikci.setObjectName(_fromUtf8("alim_tarife_tedarikci"))
        self.alim_tarife_tedarikci.currentIndexChanged.connect(self.productPriceOld)
        self.gridLayout_6.addWidget(self.alim_tarife_tedarikci, 1, 1, 1, 1)
        self.alim_tarife_kaydet = QtGui.QPushButton(self.gridLayoutWidget_5)
        self.alim_tarife_kaydet.setObjectName(_fromUtf8("alim_tarife_kaydet"))
        self.alim_tarife_kaydet.clicked.connect(dbAddPurchasesPrices)
        self.gridLayout_6.addWidget(self.alim_tarife_kaydet, 3, 1, 1, 1)
        self.eski_tarife_liste = QtGui.QTableWidget(self.alim_tarife_ekle)
        self.eski_tarife_liste.setGeometry(QtCore.QRect(20, 180, 521, 381))
        self.eski_tarife_liste.setObjectName(_fromUtf8("eski_tarife_liste"))
        self.eski_tarife_liste.setColumnCount(5)
        self.eski_tarife_liste.setRowCount(500)
        self.toolBox_4.addItem(self.alim_tarife_ekle, _fromUtf8(""))
        self.satis_tarife = QtGui.QWidget()
        self.satis_tarife.setGeometry(QtCore.QRect(0, 0, 98, 28))
        self.satis_tarife.setObjectName(_fromUtf8("satis_tarife"))
        self.satis_tarife_liste = QtGui.QTableWidget(self.satis_tarife)
        self.satis_tarife_liste.setGeometry(QtCore.QRect(0, 0, 571, 571))
        self.satis_tarife_liste.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.satis_tarife_liste.setObjectName(_fromUtf8("satis_tarife_liste"))
        self.satis_tarife_liste.setColumnCount(4)
        self.satis_tarife_liste.setRowCount(500)
        self.toolBox_4.addItem(self.satis_tarife, _fromUtf8(""))
        self.satis_tarife_ekle = QtGui.QWidget()
        self.satis_tarife_ekle.setGeometry(QtCore.QRect(0, 0, 98, 28))
        self.satis_tarife_ekle.setObjectName(_fromUtf8("satis_tarife_ekle"))
        self.gridLayoutWidget_6 = QtGui.QWidget(self.satis_tarife_ekle)
        self.gridLayoutWidget_6.setGeometry(QtCore.QRect(10, 0, 541, 171))
        self.gridLayoutWidget_6.setObjectName(_fromUtf8("gridLayoutWidget_6"))
        self.gridLayout_7 = QtGui.QGridLayout(self.gridLayoutWidget_6)
        self.gridLayout_7.setMargin(0)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.satis_tarife_urunsec = QtGui.QComboBox(self.gridLayoutWidget_6)
        self.satis_tarife_urunsec.setObjectName(_fromUtf8("satis_tarife_urunsec"))
        self.satis_tarife_urunsec.currentIndexChanged.connect(self.productPriceOldSale)
        self.gridLayout_7.addWidget(self.satis_tarife_urunsec, 0, 1, 1, 1)
        self.label_19 = QtGui.QLabel(self.gridLayoutWidget_6)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.gridLayout_7.addWidget(self.label_19, 0, 0, 1, 1)
        self.satis_tarife_fiyat = QtGui.QLineEdit(self.gridLayoutWidget_6)
        self.satis_tarife_fiyat.setObjectName(_fromUtf8("satis_tarife_fiyat"))
        self.gridLayout_7.addWidget(self.satis_tarife_fiyat, 1, 1, 1, 1)
        self.label_20 = QtGui.QLabel(self.gridLayoutWidget_6)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.gridLayout_7.addWidget(self.label_20, 1, 0, 1, 1)
        self.satis_tarife_kaydet = QtGui.QPushButton(self.gridLayoutWidget_6)
        self.satis_tarife_kaydet.setObjectName(_fromUtf8("satis_tarife_kaydet"))
        self.satis_tarife_kaydet.clicked.connect(dbAddSalesPrices)
        self.gridLayout_7.addWidget(self.satis_tarife_kaydet, 2, 1, 1, 1)
        self.eski_tarife_liste_satis = QtGui.QTableWidget(self.satis_tarife_ekle)
        self.eski_tarife_liste_satis.setGeometry(QtCore.QRect(30, 180, 511, 371))
        self.eski_tarife_liste_satis.setObjectName(_fromUtf8("eski_tarife_liste_satis"))
        self.eski_tarife_liste_satis.setColumnCount(4)
        self.eski_tarife_liste_satis.setRowCount(500)
        self.toolBox_4.addItem(self.satis_tarife_ekle, _fromUtf8(""))
        self.tabWidget.addTab(self.tarife, _fromUtf8(""))
        self.tedarikci_urun = QtGui.QWidget()
        self.tedarikci_urun.setObjectName(_fromUtf8("tedarikci_urun"))
        self.gridLayoutWidget_7 = QtGui.QWidget(self.tedarikci_urun)
        self.gridLayoutWidget_7.setGeometry(QtCore.QRect(30, 20, 491, 201))
        self.gridLayoutWidget_7.setObjectName(_fromUtf8("gridLayoutWidget_7"))
        self.gridLayout_8 = QtGui.QGridLayout(self.gridLayoutWidget_7)
        self.gridLayout_8.setMargin(0)
        self.gridLayout_8.setVerticalSpacing(5)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.label_22 = QtGui.QLabel(self.gridLayoutWidget_7)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.gridLayout_8.addWidget(self.label_22, 1, 0, 1, 1)
        self.label_21 = QtGui.QLabel(self.gridLayoutWidget_7)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.gridLayout_8.addWidget(self.label_21, 0, 0, 1, 1)
        self.tedarik_urun_urunsec = QtGui.QComboBox(self.gridLayoutWidget_7)
        self.tedarik_urun_urunsec.setObjectName(_fromUtf8("tedarik_urun_urunsec"))
        self.gridLayout_8.addWidget(self.tedarik_urun_urunsec, 0, 2, 1, 1)
        self.tedarik_urun_tedariksec = QtGui.QComboBox(self.gridLayoutWidget_7)
        self.tedarik_urun_tedariksec.setObjectName(_fromUtf8("tedarik_urun_tedariksec"))
        self.gridLayout_8.addWidget(self.tedarik_urun_tedariksec, 1, 2, 1, 1)
        self.tedarik_urun_kaydet = QtGui.QPushButton(self.gridLayoutWidget_7)
        self.tedarik_urun_kaydet.setObjectName(_fromUtf8("tedarik_urun_kaydet"))
        self.tedarik_urun_kaydet.clicked.connect(dbAddProduct_supplier)
        self.gridLayout_8.addWidget(self.tedarik_urun_kaydet, 2, 2, 1, 1)
        self.tabWidget.addTab(self.tedarikci_urun, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.toolBox_yeni = QtGui.QToolBox(self.tab_2)
        self.toolBox_yeni.setGeometry(QtCore.QRect(0, 0, 571, 691))
        self.toolBox_yeni.setObjectName(_fromUtf8("toolBox_yeni"))
        self.yeni_urun = QtGui.QWidget()
        self.yeni_urun.setGeometry(QtCore.QRect(0, 0, 98, 28))
        self.yeni_urun.setObjectName(_fromUtf8("yeni_urun"))
        self.yeni_urun_listesi_2 = QtGui.QTableWidget(self.yeni_urun)
        self.yeni_urun_listesi_2.setGeometry(QtCore.QRect(0, 0, 571, 631))
        self.yeni_urun_listesi_2.setObjectName(_fromUtf8("yeni_urun_listesi_2"))
        self.yeni_urun_listesi_2.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.yeni_urun_listesi_2.setColumnCount(2)
        self.yeni_urun_listesi_2.setRowCount(500)
        self.toolBox_yeni.addItem(self.yeni_urun, _fromUtf8(""))
        self.yeni_urun_ekle = QtGui.QWidget()
        self.yeni_urun_ekle.setGeometry(QtCore.QRect(0, 0, 571, 629))
        self.yeni_urun_ekle.setObjectName(_fromUtf8("yeni_urun_ekle"))
        self.gridLayoutWidget = QtGui.QWidget(self.yeni_urun_ekle)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 10, 521, 171))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout_urun = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_urun.setMargin(0)
        self.gridLayout_urun.setObjectName(_fromUtf8("gridLayout_urun"))
        self.label_urun = QtGui.QLabel(self.gridLayoutWidget)
        self.label_urun.setObjectName(_fromUtf8("label_urun"))
        self.gridLayout_urun.addWidget(self.label_urun, 0, 0, 1, 1)
        self.yeni_urun_adi = QtGui.QLineEdit(self.gridLayoutWidget)
        self.yeni_urun_adi.setObjectName(_fromUtf8("yeni_urun_adi"))
        self.gridLayout_urun.addWidget(self.yeni_urun_adi, 0, 1, 1, 1)
        self.yeni_urun_kaydet = QtGui.QPushButton(self.gridLayoutWidget)
        self.yeni_urun_kaydet.setObjectName(_fromUtf8("yeni_urun_kaydet"))
        self.gridLayout_urun.addWidget(self.yeni_urun_kaydet, 1, 1, 1, 1)
        self.toolBox_yeni.addItem(self.yeni_urun_ekle, _fromUtf8(""))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.toolBox.setCurrentIndex(0)
        self.toolBox_2.setCurrentIndex(0)
        self.toolBox_5.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.psupliste = []
        self.idliste = []
        self.pnameliste=[]
        self.regionid = {}
        self.afiyatlist=[]
        self.aurunlist=[]
        self.atedarikci=[]
        self.sfiyatlist = []
        self.surunlist = []
        self.scustomerlist=[]
        self.scustid=[]
        self.supplist=[]
        self.allproduct=[]
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("PyMuhasebe", "PyMuhasebe", None))
        self.tabWidget.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.urun_kutusu), _translate("MainWindow", "Alımlar", None))
        self.label_16.setText(_translate("MainWindow", "Adet", None))
        self.label_2.setText(_translate("MainWindow", "Alım Fiyatı", None))
        self.label.setText(_translate("MainWindow", "Ürün Adı", None))
        self.label_3.setText(_translate("MainWindow", "Tedarikçi", None))
        self.urun_kaydet.setText(_translate("MainWindow", "Kaydet", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.urun_ekle), _translate("MainWindow", "Yeni Alım Ekle", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.urun_tab), _translate("MainWindow", "Alımlar", None))
        self.toolBox_2.setItemText(self.toolBox_2.indexOf(self.musteri_kutusu),
                                   _translate("MainWindow", "Müşteriler", None))
        self.label_6.setText(_translate("MainWindow", "Müşteri Bölgesi", None))
        self.label_5.setText(_translate("MainWindow", "Müşteri Ad Soyad", None))
        self.musteri_kaydet.setText(_translate("MainWindow", "Kaydet", None))
        self.toolBox_2.setItemText(self.toolBox_2.indexOf(self.musteri_ekle),
                                   _translate("MainWindow", "Yeni Müşteri Ekle", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.musteri_tab),
                                  _translate("MainWindow", "Müşteriler", None))
        self.toolBox_5.setItemText(self.toolBox_5.indexOf(self.satis_kutusu),
                                   _translate("MainWindow", "Satışlar", None))
        self.label_9.setText(_translate("MainWindow", "Satış Fiyatı", None))
        self.label_11.setText(_translate("MainWindow", "Adet", None))
        self.label_10.setText(_translate("MainWindow", "Ürünler", None))
        self.label_8.setText(_translate("MainWindow", "Müşteri", None))
        self.satis_kaydet.setText(_translate("MainWindow", "Kaydet", None))
        self.toolBox_5.setItemText(self.toolBox_5.indexOf(self.satis_ekle),
                                   _translate("MainWindow", "Yeni Satış Oluştur", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.satis_tab), _translate("MainWindow", "Satışlar", None))
        self.toolBox_3.setItemText(self.toolBox_3.indexOf(self.tedarikci_kutusu),
                                   _translate("MainWindow", "Tedarikçiler", None))
        self.label_12.setText(_translate("MainWindow", "Tedarikçi Adı", None))
        self.pushButton.setText(_translate("MainWindow", "Ekle", None))
        self.toolBox_3.setItemText(self.toolBox_3.indexOf(self.tedarikci_ekleme_kutusu),
                                   _translate("MainWindow", "Tedarikçi Ekle", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tedarikci_tab), _translate("MainWindow", "Tedarikciler", None))
        self.toolBox_4.setItemText(self.toolBox_4.indexOf(self.alim_tarife),
                                   _translate("MainWindow", "Alım Tarifeleri", None))
        self.label_14.setText(_translate("MainWindow", "Ürün Seç", None))
        self.label_15.setText(_translate("MainWindow", "Fiyat", None))
        self.label_18.setText(_translate("MainWindow", "Tedarikci Seç", None))
        self.alim_tarife_kaydet.setText(_translate("MainWindow", "Ekle", None))
        self.toolBox_4.setItemText(self.toolBox_4.indexOf(self.alim_tarife_ekle),
                                   _translate("MainWindow", "Alım Tarifesi Ekle", None))
        self.toolBox_4.setItemText(self.toolBox_4.indexOf(self.satis_tarife),
                                   _translate("MainWindow", "Satış Tarifeleri", None))
        self.label_19.setText(_translate("MainWindow", "Ürün Seç", None))
        self.label_20.setText(_translate("MainWindow", "Fiyat", None))
        self.satis_tarife_kaydet.setText(_translate("MainWindow", "Ekle", None))
        self.toolBox_4.setItemText(self.toolBox_4.indexOf(self.satis_tarife_ekle),
                                   _translate("MainWindow", "Satış Tarifesi Ekle", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tarife), _translate("MainWindow", "Tarifeler", None))
        self.label_22.setText(_translate("MainWindow", "Tedarikci Seç", None))
        self.label_21.setText(_translate("MainWindow", "Ürün Seç", None))
        self.tedarik_urun_kaydet.setText(_translate("MainWindow", "Bağla", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tedarikci_urun), _translate("MainWindow", "Tedarikci-Ürün", None))
        self.toolBox_yeni.setItemText(self.toolBox_yeni.indexOf(self.yeni_urun), _translate("MainWindow", "Ürünler", None))
        self.label_urun.setText(_translate("MainWindow", "Ürün Adı", None))
        self.yeni_urun_kaydet.setText(_translate("MainWindow", "Ekle", None))
        self.yeni_urun_kaydet.clicked.connect(dbAddProduct)
        self.toolBox_yeni.setItemText(self.toolBox_yeni.indexOf(self.yeni_urun_ekle), _translate("MainWindow", "Ürün Ekle", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Ürün", None))
    def arayuz(self):
        self.urun_liste.setHorizontalHeaderLabels(_fromUtf8(QtCore.QString("Urun Adi;Tarih;Fiyat;Adet;Tedarikci")).split(";"))
        self.musteri_liste.setHorizontalHeaderLabels(_fromUtf8(QtCore.QString("Müşteri Adi;Bölge")).split(";"))
        self.satis_liste.setHorizontalHeaderLabels(_fromUtf8(QtCore.QString("Müşteri Adi;Tarih;Ürün;Fiyat;Adet")).split(";"))
        self.tedarikciler_listesi.setHorizontalHeaderLabels(_fromUtf8(QtCore.QString("Tedarikci Adı")).split(";"))
        self.alis_tarife_liste.setHorizontalHeaderLabels(_fromUtf8(QtCore.QString("Ürün Adi;Tedarikci;Fiyat;Başlangıç;Bitiş")).split(";"))
        self.eski_tarife_liste.setHorizontalHeaderLabels(_fromUtf8(QtCore.QString("Ürün Adi;Tedarikci;Fiyat;Başlangıç;Bitiş")).split(";"))
        self.satis_tarife_liste.setHorizontalHeaderLabels(_fromUtf8(QtCore.QString("Ürün Adi;Fiyat;Başlangıç;Bitiş")).split(";"))
        self.eski_tarife_liste_satis.setHorizontalHeaderLabels( _fromUtf8(QtCore.QString("Ürün Adi;Fiyat;Başlangıç;Bitiş")).split(";"))
        self.yeni_urun_listesi_2.setHorizontalHeaderLabels(_fromUtf8(QtCore.QString("Ürün Adi;Stok")).split(";"))
        self.dbSupplierlist()
    def dbProductData(self, name, supplier, date, price, amount, row):
        datelist = date.split(' ')
        self.urun_liste.setItem(row, 0, QtGui.QTableWidgetItem(name))
        self.urun_liste.setItem(row, 1, QtGui.QTableWidgetItem(datelist[0]))
        self.urun_liste.setItem(row, 2, QtGui.QTableWidgetItem(price+".00 TL"))
        self.urun_liste.setItem(row, 3, QtGui.QTableWidgetItem(amount))
        self.urun_liste.setItem(row, 4, QtGui.QTableWidgetItem(supplier))
        bool=True
        for i in productAmount.keys():
            if i==unicode(name).encode('utf-8'):
                bool=False
                item=productAmount[unicode(name).encode('utf-8')]
                item+=int(amount)
                productAmount[unicode(name).encode('utf-8')]=item
        else:
            if bool:
                productAmount[unicode(name).encode('utf-8')]=int(amount)

    def dbCustomerData(self, name, region, row):
        self.musteri_liste.setItem(row, 0, QtGui.QTableWidgetItem(_fromUtf8(name)))
        self.musteri_liste.setItem(row, 1, QtGui.QTableWidgetItem(region))

    def dbSalesData(self, cname, csurname, date, price, amount, product, row):
        datelist = date.split(' ')
        self.satis_liste.setItem(row, 0, QtGui.QTableWidgetItem(cname+" "+csurname))
        self.satis_liste.setItem(row, 1, QtGui.QTableWidgetItem(datelist[0]))
        self.satis_liste.setItem(row, 2, QtGui.QTableWidgetItem(product))
        self.satis_liste.setItem(row, 3, QtGui.QTableWidgetItem(str(price)+".00 TL"))
        self.satis_liste.setItem(row, 4, QtGui.QTableWidgetItem(str(amount)))
        bool = True
        for i in salesAmount.keys():
            if i == unicode(product).encode('utf-8'):
                bool = False
                item = salesAmount[unicode(product).encode('utf-8')]
                item += int(amount)
                salesAmount[unicode(product).encode('utf-8')] = item
        else:
            if bool:
                salesAmount[unicode(product).encode('utf-8')] = int(amount)


    def uruntedarikci(self,id,supplier,name):
        self.psupliste.append(supplier)
        self.idliste.append(id)
        self.pnameliste.append(name)

    def dbProduct(self,item):
        liste=[]
        liste.append(item)
        self.urun_adi.addItems(liste)
        self.satis_urunsec.addItems(liste)
    def dbCustomers(self, item, id):
        liste = []
        liste.append(item)
        if item!=_fromUtf8("Müşteri Seçin"):
            self.scustomerlist.append(item)
            self.scustid.append(id)
        self.musteri_sec.addItems(liste)
    def dbRegions(self, id, item):
        if id>0:
            self.regionid[unicode(item).encode('utf-8')]=id
        liste=[]
        liste.append(item)
        self.musteri_bolge.addItems(liste)

    def dbSuppliers(self, item):
        liste = []
        liste.append(item)
        self.supplist.append(item)
    def dbPurchasesPrices(self,urun,tedarikci,fiyat,basla,bitis,row):
        self.alis_tarife_liste.setItem(row,0,QtGui.QTableWidgetItem(urun))
        self.alis_tarife_liste.setItem(row, 1, QtGui.QTableWidgetItem(tedarikci))
        self.alis_tarife_liste.setItem(row,2,QtGui.QTableWidgetItem(str(fiyat)))
        self.alis_tarife_liste.setItem(row,3,QtGui.QTableWidgetItem(str(basla)))
        self.alis_tarife_liste.setItem(row,4,QtGui.QTableWidgetItem(str(bitis)))
    def dbAddPricesProduct(self):
        self.alim_tarife_urun.addItems(self.allproduct)
        self.satis_tarife_urunsec.addItems(self.allproduct)
    def dbSalesPrices(self,urun,fiyat,basla,bitis,row):
        self.satis_tarife_liste.setItem(row, 0, QtGui.QTableWidgetItem(urun))
        self.satis_tarife_liste.setItem(row, 1, QtGui.QTableWidgetItem(str(fiyat)))
        self.satis_tarife_liste.setItem(row, 2, QtGui.QTableWidgetItem(str(basla)))
        self.satis_tarife_liste.setItem(row, 3, QtGui.QTableWidgetItem(str(bitis)))
    def alimfiyat(self,product,price,end,supplier):
        if end==None:
            self.atedarikci.append(supplier)
            self.aurunlist.append(product)
            self.afiyatlist.append(price)
    def satisfiyat(self,product,price,end):
        if end==None:
            self.surunlist.append(product)
            self.sfiyatlist.append(price)

    @QtCore.pyqtSlot()
    def supplierOnActivated(self):
        for pr in range(len(self.aurunlist)):
            if unicode(self.atedarikci[pr]).encode('utf-8') == unicode(self.urun_tedarikci.currentText()).encode('utf-8') and unicode(self.aurunlist[pr]).encode('utf-8') ==unicode(self.urun_adi.currentText()).encode('utf-8'):
                self.urun_alim_fiyat.setText(str(self.afiyatlist[pr])+".00 TL")
                break
            else:
                self.urun_alim_fiyat.setText("")

    def saleproductOnActivated(self, index):
        for pr in range(len(self.surunlist)):
            if unicode(self.surunlist[pr]).encode('utf-8') == unicode(self.satis_urunsec.currentText()).encode('utf-8'):
                self.satis_fiyat.setText(self.sfiyatlist[pr]+".00 TL")
                break
            else:
                self.satis_fiyat.setText("")

    def productOnActivated(self):
        text=unicode(self.urun_adi.currentText()).encode('utf-8')
        self.urun_tedarikci.clear()
        self.urun_alim_fiyat.setText("")
        for itm in range(len(self.pnameliste)):
            if unicode(self.pnameliste[itm]).encode('utf-8')==text:
                self.urun_tedarikci.addItem(self.psupliste[itm])

    def productPriceOnActivated(self):
        text=unicode(self.alim_tarife_urun.currentText()).encode('utf-8')
        self.alim_tarife_tedarikci.clear()
        for itm in range(len(self.pnameliste)):
            if unicode(self.pnameliste[itm]).encode('utf-8')==text:
                self.alim_tarife_tedarikci.addItem(self.psupliste[itm])

    def productPriceOld(self):
        row=0
        cur = con.cursor()
        cur.execute('select * from view_purchases_prices')
        for result in cur:
            if unicode(self.alim_tarife_urun.currentText()).encode('utf-8')==unicode(result[1]).encode('utf-8') and unicode(self.alim_tarife_tedarikci.currentText()).encode('utf-8')==unicode(result[4]).encode('utf-8'):
                self.eski_tarife_liste.setItem(row, 0, QtGui.QTableWidgetItem(result[1]))
                self.eski_tarife_liste.setItem(row, 1, QtGui.QTableWidgetItem(result[4]))
                self.eski_tarife_liste.setItem(row, 2, QtGui.QTableWidgetItem(str(result[2])))
                self.eski_tarife_liste.setItem(row, 3, QtGui.QTableWidgetItem(str(result[10])))
                self.eski_tarife_liste.setItem(row, 4, QtGui.QTableWidgetItem(str(result[3])))
                row+=1
            else:
                if row==0:
                    self.eski_tarife_liste.clear()

    def productPriceOldSale(self):
        row=0
        cur = con.cursor()
        cur.execute('select * from view_sales_prices')
        for result in cur:
            if unicode(self.satis_tarife_urunsec.currentText()).encode('utf-8')==unicode(result[1]).encode('utf-8'):
                self.eski_tarife_liste_satis.setItem(row, 0, QtGui.QTableWidgetItem(result[1]))
                self.eski_tarife_liste_satis.setItem(row, 1, QtGui.QTableWidgetItem(str(result[2])))
                self.eski_tarife_liste_satis.setItem(row, 2, QtGui.QTableWidgetItem(str(result[6])))
                self.eski_tarife_liste_satis.setItem(row, 3, QtGui.QTableWidgetItem(str(result[3])))
                row+=1
            else:
                if row==0:
                    self.eski_tarife_liste_satis.clear()

    def musteriekle(self):
        if unicode(self.musteri_adi.text()).encode('utf-8')!="" and self.musteri_bolge.currentIndex()>0 :
            dbAddCustomer(self.regionid[str(unicode(self.musteri_bolge.currentText()).encode('utf-8'))])
        else:
            popupmsg("Sanırım Bir Hata Var!")
    def satisyap(self):
        if unicode(self.satis_urunsec.currentText()).encode('utf-8')!="" and unicode(self.musteri_sec.currentText()).encode('utf-8')!="" and int(self.satis_adet.text())>0:
            for i in range(len(self.pnameliste)):
                for j in range(len(self.scustomerlist)):
                    if unicode(self.scustomerlist[j]).encode('utf-8')==unicode(self.musteri_sec.currentText()).encode('utf-8') and unicode(self.pnameliste[i]).encode('utf-8') ==unicode(self.satis_urunsec.currentText()).encode('utf-8'):
                        try:
                            if int(self.satis_adet.text())<productAmount[unicode(self.satis_urunsec.currentText()).encode('utf-8')]:
                                dbAddSale(self.idliste[i],self.satis_adet.text())
                            else:
                                popupmsg("Stok yeterli değil!")
                        except ValueError:
                            continue

    def alimyap(self):
        if unicode(self.urun_adi.currentText()).encode('utf-8')!="" and unicode(self.urun_tedarikci.currentText()).encode('utf-8')!="" and str(self.urun_alim_fiyat.text())!="" and int(self.urun_adet.text())>0:
            for i in range(len(self.pnameliste)):
                for j in range(len(self.psupliste)):
                    if unicode(self.psupliste[j]).encode('utf-8')==unicode(self.urun_tedarikci.currentText()).encode('utf-8') and unicode(self.pnameliste[i]).encode('utf-8')==unicode(self.urun_adi.currentText()).encode('utf-8'):
                        dbAddPurchase(self.idliste[i],self.urun_adet.text())
    def dbSupplierlist(self):
        row=0
        for i in self.supplist:
            self.tedarikciler_listesi.setItem(row, 0, QtGui.QTableWidgetItem(i))
            row += 1
    def tedarik_urun_bagla(self):
        self.tedarik_urun_urunsec.addItems(self.allproduct)
        self.tedarik_urun_tedariksec.addItems(self.supplist)
    def productlist(self,urun,row):
        self.yeni_urun_listesi_2.setItem(row,0,QtGui.QTableWidgetItem(urun))
        adet=0
        for i in productAmount.keys():
            if i==unicode(urun).encode('utf-8'):
                adet=int(productAmount[unicode(urun).encode('utf-8')])
                self.yeni_urun_listesi_2.setItem(row, 1, QtGui.QTableWidgetItem(str(adet)))
                break
            else:
                self.yeni_urun_listesi_2.setItem(row, 1, QtGui.QTableWidgetItem("0"))
def dbData():
    ui.musteri_sec.clear()
    productAmount.clear()
    salesAmount.clear()
    ui.urun_adi.clear()
    ui.satis_urunsec.clear()
    ui.urun_tedarikci.clear()
    ui.musteri_bolge.clear()
    ui.alim_tarife_urun.clear()
    ui.satis_tarife_urunsec.clear()
    ui.yeni_urun_listesi_2.clear()
    del ui.psupliste[:]
    del ui.pnameliste[:]
    del ui.idliste[:]
    del ui.supplist[:]
    del ui.allproduct[:]
    del ui.surunlist[:]
    del ui.sfiyatlist[:]
    del ui.atedarikci[:]
    del ui.aurunlist[:]
    del ui.afiyatlist[:]
    ui.tedarik_urun_urunsec.clear()
    ui.tedarik_urun_tedariksec.clear()
    data = {
        1: 'select * from view_purchases',
        2: 'select * from view_customers',
        3: 'select * from view_sales',
        4: 'select * from view_suppliers',
        5: 'select * from view_sales_prices',
        6: 'select * from view_regions',
        7: 'select * from view_purchases_prices',
        8: 'select * from view_product_supplier',
        9: 'select * from view_product'}
    cur = con.cursor()
    productPrices={}
    for i in data:
        r = 0
        cur.execute(data[i])
        for result in cur:
            if i == 1:
                productAmount[unicode(result[0]).encode('utf-8')]=0
                ui.dbProductData(result[1], result[5], str(result[4]), str(result[2]), str(result[3]), r)
                productPrices[result[1]]=result[2]
            if i == 2:
                ui.dbCustomerData(result[0]+" "+result[2], result[1], r)
                if r == 0:
                    ui.dbCustomers(_fromUtf8("Müşteri Seçin"),str(0))
                ui.dbCustomers(_fromUtf8(result[0]+" "+result[2]),str(result[5]))
            if i == 3:
                ui.dbSalesData(result[0],result[10], str(result[1]), result[2], result[3], result[4], r)
            if i == 4:
                ui.dbSuppliers(result[0])
            if i == 5:
                ui.dbSalesPrices(result[1], result[2], result[6], result[3], r)
                ui.satisfiyat(result[1], str(result[2]), result[3])
                if r == 0:
                    for k in salesAmount.keys():
                        item = salesAmount[k]
                        padet = productAmount[k]
                        padet -= item
                        productAmount[k] = padet
            if i == 6:
                if r == 0:
                    ui.dbRegions(0,_fromUtf8("Bölge Seçin"))
                ui.dbRegions(result[0],result[1])
            if i == 7:
                ui.alimfiyat(result[1],result[2],result[3],result[4])
                ui.dbPurchasesPrices(result[1], result[4], result[2], result[10], result[3], r)

            if i == 8:
                ui.uruntedarikci(result[2],result[1],result[0])
            if i == 9:
                if r == 0:
                    ui.dbProduct(_fromUtf8("Ürün Seçin"))
                ui.dbProduct(result[0])
                ui.allproduct.append(result[0])
                ui.productlist(result[0], r)
            r += 1
    ui.tedarik_urun_bagla()
    ui.dbAddPricesProduct()
    ui.arayuz()

def dbAddCustomer(region):
    cur = con.cursor()
    strname=unicode(ui.musteri_adi.text()).encode('utf-8')
    for i in ui.scustomerlist:
        if i==strname:
            popupmsg("Musteri Zaten Mevcut!")
            break
    else:
        ayir=strname.rfind(" ")
        surname=strname[ayir+1:]
        strname=strname[:ayir]
        cur.callproc('SP_ADD_CUSTOMER', (strname ,surname,region))
    ui.toolBox_2.setCurrentIndex(0)
    dbData()

def dbAddSale(urun,adet):
    cur = con.cursor()
    cur.execute('select * from view_sales_prices ')
    musteri2=0
    urun2=0
    for result in cur:
        if int(result[0]) == int(urun):
            urun2 = int(result[4])
        for i in range(len(ui.scustomerlist)):
            if unicode(ui.scustomerlist[i]).encode('utf-8')==unicode(ui.musteri_sec.currentText()).encode('utf-8'):
                musteri2=int(ui.scustid[i])
    cur.callproc('SP_ADD_SALE', (int(musteri2), int(urun2), datetime.now(), int(adet)))
    ui.toolBox_5.setCurrentIndex(0)
    dbData()

def dbAddPurchase(urun,adet):
    cur = con.cursor()
    cur.execute('select * from view_add_purchases')
    urun2=urun
    for result in cur:
        if int(result[0]) == int(urun) and unicode(result[5]).encode('utf-8')== unicode(ui.urun_tedarikci.currentText()).encode('utf-8'):
            urun2 = result[2]
    cur.callproc('SP_ADD_PURCHASES', (int(urun2), datetime.now(), int(adet)))
    ui.toolBox.setCurrentIndex(0)
    dbData()

def dbAddProduct_supplier():
    kontrol=True
    tedarikci=0
    urun=0
    cur = con.cursor()
    cur.execute('select * from view_product_supplier')
    for result in cur:
        if unicode(result[1]).encode('utf-8')==unicode(ui.tedarik_urun_tedariksec.currentText()).encode('utf-8') and unicode(result[0]).encode('utf-8')==unicode(ui.tedarik_urun_urunsec.currentText()).encode('utf-8'):
            popupmsg("Hata!")
            kontrol=False
    cur.execute('select * from view_suppliers')
    for result in cur:
        if unicode(result[0]).encode('utf-8')==unicode(ui.tedarik_urun_tedariksec.currentText()).encode('utf-8'):
            tedarikci = result[1]
    cur.execute('select * from view_product')
    for result in cur:
        if unicode(result[0]).encode('utf-8')==unicode(ui.tedarik_urun_urunsec.currentText()).encode('utf-8'):
            urun=result[1]
    if kontrol:
        cur.callproc('SP_ADD_PRODUCT_SUPPLIER', (int(urun), int(tedarikci)))
        popupmsg("Eklendi!")
    dbData()

def dbAddSupplier():
    cur = con.cursor()
    cur.execute('select * from view_suppliers')
    idno=1
    for result in cur:
        if result[1]>idno:
            idno=result[1]
        if unicode(result[0]).encode('utf-8')==unicode(ui.lineEdit.text()).encode('utf-8'):
            popupmsg("Tedarikci Zaten Mevcut!")
            break
    else:
        ad=unicode(ui.lineEdit.text()).encode('utf-8')
        cur.callproc('SP_ADD_SUPPLIER', (idno+1,ad))
    ui.toolBox_3.setCurrentIndex(0)
    dbData()

def dbAddPurchasesPrices():
    cur = con.cursor()
    cur.execute('select * from view_add_purchases_prices')
    for result in cur:
        if unicode(result[0]).encode('utf-8')==unicode(ui.alim_tarife_urun.currentText()).encode('utf-8')and unicode(result[2]).encode('utf-8')==unicode(ui.alim_tarife_tedarikci.currentText()).encode('utf-8'):
            urunid=result[1]
    fiyat=int(ui.alim_tarife_fiyat.text())
    tarih=datetime.now()
    cur.callproc('SP_ADD_PURCHASES_PRICES', (urunid, fiyat, tarih))
    dbData()
    ui.toolBox_4.setCurrentIndex(0)


def dbAddSalesPrices():
    urunid=""
    cur = con.cursor()
    cur.execute('select * from view_product')
    for result in cur:
        if unicode(result[0]).encode('utf-8')==unicode(ui.satis_tarife_urunsec.currentText()).encode('utf-8'):
            urunid=result[1]
    fiyat=int(ui.satis_tarife_fiyat.text())
    tarih=datetime.now()
    cur.callproc('SP_ADD_SALES_PRICES', (urunid,fiyat,tarih))
    ui.toolBox_4.setCurrentIndex(2)
    dbData()

def dbAddProduct():
    if ui.yeni_urun_adi!=None:
        cur = con.cursor()
        cur.execute('select * from view_product')
        idno=1
        kontrol=True
        ad = unicode(ui.yeni_urun_adi.text()).encode('utf-8')
        for result in cur:
            if result[1]>idno:
                idno=result[1]
            if unicode(result[0]).encode('utf-8')==ad:
                kontrol=False
                popupmsg("Ürün Mevcut!")
        if kontrol:
            cur.callproc('SP_ADD_PRODUCT', (idno + 1, ad))
            ui.toolBox_yeni.setCurrentIndex(0)
            dbData()


def popupmsg(msg):
    import Tkinter

    window = Tkinter.Tk()

    def close_window():
        window.destroy()

    frame = Tkinter.Frame(window)
    window.geometry('200x70+850+400')
    frame.pack()
    button = Tkinter.Button(frame, text=msg, command=close_window,borderwidth=0)
    button.pack()

    window.mainloop()

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    dbData()
    MainWindow.show()
    sys.exit(app.exec_())
    cur.close()
    con.close()
