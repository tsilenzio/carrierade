import sys
import sqlite3

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow

from dist.MainWindow import Ui_MainWindow

print("Hello from main.py")


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        # Create a database connection
        self.conn = sqlite3.connect("database.db")
        print("Opened database successfully")


app = QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec())
