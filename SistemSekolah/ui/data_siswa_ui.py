# Form implementation generated from reading ui file 'ui/data_siswa.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(971, 626)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 40, 81, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 100, 81, 21))
        self.label_2.setObjectName("label_2")
        self.lineEdit_nama_siswa = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_nama_siswa.setGeometry(QtCore.QRect(100, 40, 113, 21))
        self.lineEdit_nama_siswa.setObjectName("lineEdit_nama_siswa")
        self.lineEdit_nis = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_nis.setGeometry(QtCore.QRect(100, 100, 113, 21))
        self.lineEdit_nis.setObjectName("lineEdit_nis")
        self.pushButton_simpan = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_simpan.setGeometry(QtCore.QRect(30, 320, 75, 24))
        self.pushButton_simpan.setObjectName("pushButton_simpan")
        self.pushButton_hapus = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_hapus.setGeometry(QtCore.QRect(230, 320, 75, 24))
        self.pushButton_hapus.setObjectName("pushButton_hapus")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 370, 711, 201))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 140, 81, 21))
        self.label_3.setObjectName("label_3")
        self.comboBoxI_jenis = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBoxI_jenis.setGeometry(QtCore.QRect(100, 140, 111, 22))
        self.comboBoxI_jenis.setObjectName("comboBoxI_jenis")
        self.comboBoxI_jenis.addItem("")
        self.comboBoxI_jenis.addItem("")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 180, 81, 21))
        self.label_4.setObjectName("label_4")
        self.comboBox_Agama = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox_Agama.setGeometry(QtCore.QRect(100, 180, 111, 22))
        self.comboBox_Agama.setObjectName("comboBox_Agama")
        self.comboBox_Agama.addItem("")
        self.comboBox_Agama.addItem("")
        self.comboBox_Agama.addItem("")
        self.comboBox_Agama.addItem("")
        self.comboBox_Agama.addItem("")
        self.pushButton_ubah = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_ubah.setGeometry(QtCore.QRect(130, 320, 75, 24))
        self.pushButton_ubah.setObjectName("pushButton_ubah")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(270, 40, 81, 21))
        self.label_5.setObjectName("label_5")
        self.dateEdit = QtWidgets.QDateEdit(parent=self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(390, 40, 110, 22))
        self.dateEdit.setObjectName("dateEdit")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(270, 100, 81, 21))
        self.label_6.setObjectName("label_6")
        self.lineEdit_alamat = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_alamat.setGeometry(QtCore.QRect(390, 100, 113, 21))
        self.lineEdit_alamat.setObjectName("lineEdit_alamat")
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(270, 140, 111, 21))
        self.label_7.setObjectName("label_7")
        self.lineEdit_NoHp = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_NoHp.setGeometry(QtCore.QRect(390, 140, 113, 21))
        self.lineEdit_NoHp.setObjectName("lineEdit_NoHp")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 971, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Nama Siswa"))
        self.label_2.setText(_translate("MainWindow", "NIS"))
        self.pushButton_simpan.setText(_translate("MainWindow", "Simpan"))
        self.pushButton_hapus.setText(_translate("MainWindow", "Hapus"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Nama Siswa"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "NIS"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Jenis Kelamin"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Tanggal Lahir"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Agama"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Alamat"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "No. HP"))
        self.label_3.setText(_translate("MainWindow", "Jenis Kelamin"))
        self.comboBoxI_jenis.setItemText(0, _translate("MainWindow", "Laki-Laki"))
        self.comboBoxI_jenis.setItemText(1, _translate("MainWindow", "Perempuan"))
        self.label_4.setText(_translate("MainWindow", "Agama"))
        self.comboBox_Agama.setItemText(0, _translate("MainWindow", "Islam"))
        self.comboBox_Agama.setItemText(1, _translate("MainWindow", "Katholik"))
        self.comboBox_Agama.setItemText(2, _translate("MainWindow", "Kristen"))
        self.comboBox_Agama.setItemText(3, _translate("MainWindow", "Hindu"))
        self.comboBox_Agama.setItemText(4, _translate("MainWindow", "Budha"))
        self.pushButton_ubah.setText(_translate("MainWindow", "Ubah"))
        self.label_5.setText(_translate("MainWindow", "Tanggal Lahir"))
        self.label_6.setText(_translate("MainWindow", "Alamat"))
        self.label_7.setText(_translate("MainWindow", "Nomor Handphone"))

    def populate_table(self):
        # Menambahkan data contoh ke dalam tabel
        data = [
            ["John Doe", "12345", "Laki-Laki", "2000-01-01", "Islam", "Alamat 1", "081234567890"],
            ["Jane Smith", "12346", "Perempuan", "2001-02-01", "Kristen", "Alamat 2", "082345678901"]
        ]

        self.tableWidget.setRowCount(len(data))  # Mengatur jumlah baris sesuai data
        for row_index, row_data in enumerate(data):
            for col_index, col_data in enumerate(row_data):
                item = QtWidgets.QTableWidgetItem(col_data)
                self.tableWidget.setItem(row_index, col_index, item)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
