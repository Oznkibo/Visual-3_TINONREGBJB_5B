from PyQt6.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem
from data_siswa_ui import Ui_MainWindow
from database import get_connection

class DataSiswaUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Hubungkan tombol dengan fungsi CRUD
        self.ui.pushButton_simpan.clicked.connect(self.simpan_data)
        self.ui.pushButton_hapus.clicked.connect(self.hapus_data)
        self.ui.pushButton_ubah.clicked.connect(self.ubah_data)

        # Muat data awal ke tabel
        self.load_data()

    def load_data(self):
        """Memuat data siswa dari database ke tabel."""
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT NIS, Nama_Siswa, Jenis_Kelamin, Tanggal_Lahir, Agama, Alamat, No_Hp FROM data_siswa")
            rows = cursor.fetchall()

            self.ui.tableWidget.setRowCount(len(rows))  # Menyesuaikan jumlah baris
            self.ui.tableWidget.setColumnCount(7)  # Sesuaikan jumlah kolom
            self.ui.tableWidget.setHorizontalHeaderLabels(["NIS", "Nama Siswa", "Jenis Kelamin", "Tanggal Lahir", "Agama", "Alamat", "No Hp"])

            for i, row in enumerate(rows):
                for j, value in enumerate(row):
                    self.ui.tableWidget.setItem(i, j, QTableWidgetItem(str(value)))

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Terjadi kesalahan saat memuat data: {str(e)}")
        finally:
            conn.close()

    def simpan_data(self):
        """Menyimpan data siswa ke database."""
        nis = self.ui.lineEdit_nis.text()
        nama = self.ui.lineEdit_nama_siswa.text()
        jenis_kelamin = self.ui.comboBoxI_jenis.currentText()
        agama = self.ui.comboBox_Agama.currentText()
        alamat = self.ui.lineEdit_alamat.text()
        no_hp = self.ui.lineEdit_NoHp.text()
        tanggal_lahir = self.ui.dateEdit.date().toString("yyyy-MM-dd")

        if not nis or not nama or not alamat or not no_hp:
            QMessageBox.warning(self, "Peringatan", "Semua data harus diisi!")
            return

        try:
            conn = get_connection()
            cursor = conn.cursor()

            # Cek apakah NIS sudah ada
            cursor.execute("SELECT COUNT(*) FROM data_siswa WHERE NIS = %s", (nis,))
            if cursor.fetchone()[0] > 0:
                QMessageBox.warning(self, "Peringatan", "NIS sudah terdaftar!")
                return

            query = """INSERT INTO data_siswa (NIS, Nama_Siswa, Jenis_Kelamin, Tanggal_Lahir, Agama, Alamat, No_Hp) 
                       VALUES (%s, %s, %s, %s, %s, %s, %s)"""
            cursor.execute(query, (nis, nama, jenis_kelamin, tanggal_lahir, agama, alamat, no_hp))
            conn.commit()
            QMessageBox.information(self, "Sukses", "Data berhasil disimpan!")
            self.load_data()  # Muat ulang data setelah penyimpanan
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))
        finally:
            conn.close()

    def hapus_data(self):
        """Menghapus data siswa berdasarkan NIS."""
        nis = self.ui.lineEdit_nis.text()

        if not nis:
            QMessageBox.warning(self, "Peringatan", "NIS harus diisi!")
            return

        try:
            conn = get_connection()
            cursor = conn.cursor()
            query = "DELETE FROM data_siswa WHERE NIS = %s"
            cursor.execute(query, (nis,))
            conn.commit()

            if cursor.rowcount > 0:
                QMessageBox.information(self, "Sukses", "Data berhasil dihapus!")
            else:
                QMessageBox.warning(self, "Gagal", "Data tidak ditemukan!")
            self.load_data()  # Muat ulang data setelah penghapusan
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))
        finally:
            conn.close()

    def ubah_data(self):
        """Mengubah data siswa berdasarkan NIS."""
        nis = self.ui.lineEdit_nis.text()
        nama = self.ui.lineEdit_nama_siswa.text()
        jenis_kelamin = self.ui.comboBoxI_jenis.currentText()
        agama = self.ui.comboBox_Agama.currentText()
        alamat = self.ui.lineEdit_alamat.text()
        no_hp = self.ui.lineEdit_NoHp.text()
        tanggal_lahir = self.ui.dateEdit.date().toString("yyyy-MM-dd")

        if not nis or not nama:
            QMessageBox.warning(self, "Peringatan", "NIS dan Nama harus diisi!")
            return

        try:
            conn = get_connection()
            cursor = conn.cursor()
            query = """UPDATE data_siswa 
                       SET Nama_Siswa = %s, Jenis_Kelamin = %s, Tanggal_Lahir = %s, Agama = %s, Alamat = %s, No_Hp = %s 
                       WHERE NIS = %s"""
            cursor.execute(query, (nama, jenis_kelamin, tanggal_lahir, agama, alamat, no_hp, nis))
            conn.commit()
            QMessageBox.information(self, "Sukses", "Data berhasil diubah!")
            self.load_data()  # Muat ulang data setelah perubahan
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))
        finally:
            conn.close()
