import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow

# from models import Base
from ui import Ui_MainWindow
from models import Base, Dealer, Order

engine = create_engine("sqlite:///database.db")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        # Establish a session with the database
        print("Connecting to the database...")
        self.session = Session()
        print("Connected database successfully")

        # Set the table model
        self.save_button.clicked.connect(self.save_data)

    def save_data(self):
        # Collect dealer data from UI fields
        dealer_name = self.dealer_combobox.currentText()
        account_number = self.account_number_textbox.text()

        # Create a new Dealer instance
        new_dealer = Dealer(dealer_name=dealer_name, account_number=account_number)

        # Collect order data from UI fields
        order_number = self.order_number_textbox.text()
        po_number = self.po_textbox.text()
        model_number = self.model_number_textbox.text()
        serial_number = self.serial_number_textbox.text()
        short_description = self.short_description_textbox.toPlainText()
        # For date and time, assuming they are QDateEdit and QTimeEdit respectively
        date = self.date_edit.date().toString("yyyy-MM-dd")
        time = self.time_edit.time().toString("HH:mm:ss")
        ordered_at = f"{date} {time}"
        # For warranty status, assuming radio buttons for Yes, No, N/A
        warranty_status = (
            "Yes"
            if self.radioButton.isChecked()
            else "No"
            if self.radioButton_2.isChecked()
            else "N/A"
        )
        caller = self.caller_textbox.text()
        phone = self.phone_textbox.text()

        # Create a new Order instance and associate it with the new dealer
        new_order = Order(
            dealer=new_dealer,
            order_number=order_number,
            po_number=po_number,
            model_number=model_number,
            serial_number=serial_number,
            short_description=short_description,
            ordered_at=ordered_at,
            warranty_status=warranty_status,
            caller=caller,
            phone=phone,
        )

        # Add the new instances to the session
        self.session.add(new_dealer)
        self.session.add(new_order)

        # Commit the transaction to save the new records to the database
        self.session.commit()

        print("Dealer and order information saved to the database")


app = QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec())
