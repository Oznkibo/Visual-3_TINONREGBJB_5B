import sys
from PyQt6.QtWidgets import QApplication
from data_siswa import DataSiswaUI  # Menggunakan logika utama

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DataSiswaUI()
    window.show()
    sys.exit(app.exec())
