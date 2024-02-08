import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow

# from models import Base
from ui.MainWindow import Ui_MainWindow
from models import Base

engine = create_engine("sqlite:///database.db")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.session = Session()

        # Create a database connection
        # self.conn = sqlite3.connect("database.db")
        print("Opened database successfully")


app = QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec())
