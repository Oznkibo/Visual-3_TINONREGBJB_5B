from PyQt6.QtWidgets import QMainWindow
from PyQt6.uic import load_ui, loadUi


class formDua(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('form2.ui',self)