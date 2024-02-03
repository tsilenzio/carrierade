# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPlainTextEdit, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QStatusBar,
    QTimeEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(551, 574)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.date_label = QLabel(self.centralwidget)
        self.date_label.setObjectName(u"date_label")
        self.date_label.setMinimumSize(QSize(250, 0))
        self.date_label.setMaximumSize(QSize(16777215, 20))

        self.gridLayout.addWidget(self.date_label, 0, 0, 1, 1)

        self.model_number_textbox = QLineEdit(self.centralwidget)
        self.model_number_textbox.setObjectName(u"model_number_textbox")
        self.model_number_textbox.setMinimumSize(QSize(250, 0))

        self.gridLayout.addWidget(self.model_number_textbox, 7, 0, 1, 1)

        self.warranty_label = QLabel(self.centralwidget)
        self.warranty_label.setObjectName(u"warranty_label")
        self.warranty_label.setMinimumSize(QSize(250, 0))
        self.warranty_label.setMaximumSize(QSize(16777215, 20))

        self.gridLayout.addWidget(self.warranty_label, 6, 1, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(0, 0, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.reset_button = QPushButton(self.centralwidget)
        self.reset_button.setObjectName(u"reset_button")
        self.reset_button.setMinimumSize(QSize(100, 0))
        self.reset_button.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout.addWidget(self.reset_button)

        self.save_button = QPushButton(self.centralwidget)
        self.save_button.setObjectName(u"save_button")
        self.save_button.setMinimumSize(QSize(100, 0))
        self.save_button.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout.addWidget(self.save_button)


        self.gridLayout.addLayout(self.horizontalLayout, 14, 1, 1, 1)

        self.model_line_edit = QLabel(self.centralwidget)
        self.model_line_edit.setObjectName(u"model_line_edit")
        self.model_line_edit.setMinimumSize(QSize(250, 0))
        self.model_line_edit.setMaximumSize(QSize(16777215, 20))

        self.gridLayout.addWidget(self.model_line_edit, 6, 0, 1, 1)

        self.order_number_label = QLabel(self.centralwidget)
        self.order_number_label.setObjectName(u"order_number_label")
        self.order_number_label.setMinimumSize(QSize(250, 0))

        self.gridLayout.addWidget(self.order_number_label, 12, 1, 1, 1)

        self.po_label = QLabel(self.centralwidget)
        self.po_label.setObjectName(u"po_label")
        self.po_label.setMinimumSize(QSize(250, 0))
        self.po_label.setMaximumSize(QSize(16777215, 20))

        self.gridLayout.addWidget(self.po_label, 12, 0, 1, 1)

        self.dealer_label = QLabel(self.centralwidget)
        self.dealer_label.setObjectName(u"dealer_label")
        self.dealer_label.setMinimumSize(QSize(250, 0))
        self.dealer_label.setMaximumSize(QSize(16777215, 20))

        self.gridLayout.addWidget(self.dealer_label, 2, 0, 1, 1)

        self.account_label = QLabel(self.centralwidget)
        self.account_label.setObjectName(u"account_label")
        self.account_label.setMinimumSize(QSize(250, 0))
        self.account_label.setMaximumSize(QSize(16777215, 20))

        self.gridLayout.addWidget(self.account_label, 2, 1, 1, 1)

        self.caller_label = QLabel(self.centralwidget)
        self.caller_label.setObjectName(u"caller_label")
        self.caller_label.setMinimumSize(QSize(250, 0))
        self.caller_label.setMaximumSize(QSize(16777215, 20))

        self.gridLayout.addWidget(self.caller_label, 4, 0, 1, 1)

        self.description_label = QLabel(self.centralwidget)
        self.description_label.setObjectName(u"description_label")
        self.description_label.setMinimumSize(QSize(250, 0))
        self.description_label.setMaximumSize(QSize(16777215, 20))

        self.gridLayout.addWidget(self.description_label, 10, 0, 1, 1)

        self.serial_number_label = QLabel(self.centralwidget)
        self.serial_number_label.setObjectName(u"serial_number_label")
        self.serial_number_label.setMinimumSize(QSize(250, 0))
        self.serial_number_label.setMaximumSize(QSize(16777215, 20))

        self.gridLayout.addWidget(self.serial_number_label, 8, 0, 1, 1)

        self.serial_number_textbox = QLineEdit(self.centralwidget)
        self.serial_number_textbox.setObjectName(u"serial_number_textbox")
        self.serial_number_textbox.setMinimumSize(QSize(250, 0))

        self.gridLayout.addWidget(self.serial_number_textbox, 9, 0, 1, 1)

        self.po_textbox = QLineEdit(self.centralwidget)
        self.po_textbox.setObjectName(u"po_textbox")
        self.po_textbox.setMinimumSize(QSize(250, 0))

        self.gridLayout.addWidget(self.po_textbox, 13, 0, 1, 1)

        self.phone_textbox = QLineEdit(self.centralwidget)
        self.phone_textbox.setObjectName(u"phone_textbox")
        self.phone_textbox.setMinimumSize(QSize(250, 0))

        self.gridLayout.addWidget(self.phone_textbox, 5, 1, 1, 1)

        self.time_edit = QTimeEdit(self.centralwidget)
        self.time_edit.setObjectName(u"time_edit")
        self.time_edit.setMinimumSize(QSize(250, 0))

        self.gridLayout.addWidget(self.time_edit, 1, 1, 1, 1)

        self.time_label = QLabel(self.centralwidget)
        self.time_label.setObjectName(u"time_label")
        self.time_label.setMinimumSize(QSize(250, 0))
        self.time_label.setMaximumSize(QSize(16777215, 20))

        self.gridLayout.addWidget(self.time_label, 0, 1, 1, 1)

        self.date_edit = QDateEdit(self.centralwidget)
        self.date_edit.setObjectName(u"date_edit")
        self.date_edit.setMinimumSize(QSize(250, 0))
        self.date_edit.setDateTime(QDateTime(QDate(2024, 1, 1), QTime(17, 0, 0)))

        self.gridLayout.addWidget(self.date_edit, 1, 0, 1, 1)

        self.account_number_textbox = QLineEdit(self.centralwidget)
        self.account_number_textbox.setObjectName(u"account_number_textbox")
        self.account_number_textbox.setMinimumSize(QSize(250, 0))

        self.gridLayout.addWidget(self.account_number_textbox, 3, 1, 1, 1)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(250, 0))
        self.groupBox.setFocusPolicy(Qt.StrongFocus)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(12)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, -1, -1, -1)
        self.radioButton = QRadioButton(self.groupBox)
        self.radioButton.setObjectName(u"radioButton")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton.sizePolicy().hasHeightForWidth())
        self.radioButton.setSizePolicy(sizePolicy)
        self.radioButton.setMinimumSize(QSize(240, 0))
        self.radioButton.setFocusPolicy(Qt.StrongFocus)

        self.verticalLayout.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.groupBox)
        self.radioButton_2.setObjectName(u"radioButton_2")
        sizePolicy.setHeightForWidth(self.radioButton_2.sizePolicy().hasHeightForWidth())
        self.radioButton_2.setSizePolicy(sizePolicy)
        self.radioButton_2.setMinimumSize(QSize(240, 0))
        self.radioButton_2.setFocusPolicy(Qt.StrongFocus)

        self.verticalLayout.addWidget(self.radioButton_2)

        self.radioButton_3 = QRadioButton(self.groupBox)
        self.radioButton_3.setObjectName(u"radioButton_3")
        sizePolicy.setHeightForWidth(self.radioButton_3.sizePolicy().hasHeightForWidth())
        self.radioButton_3.setSizePolicy(sizePolicy)
        self.radioButton_3.setMinimumSize(QSize(240, 0))
        self.radioButton_3.setFocusPolicy(Qt.StrongFocus)
        self.radioButton_3.setChecked(True)

        self.verticalLayout.addWidget(self.radioButton_3)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.gridLayout.addWidget(self.groupBox, 7, 1, 4, 1)

        self.dealer_combobox = QComboBox(self.centralwidget)
        self.dealer_combobox.setObjectName(u"dealer_combobox")
        self.dealer_combobox.setMinimumSize(QSize(250, 0))
        self.dealer_combobox.setEditable(True)
        self.dealer_combobox.setInsertPolicy(QComboBox.InsertAlphabetically)

        self.gridLayout.addWidget(self.dealer_combobox, 3, 0, 1, 1)

        self.order_number_textbox = QLineEdit(self.centralwidget)
        self.order_number_textbox.setObjectName(u"order_number_textbox")
        self.order_number_textbox.setMinimumSize(QSize(250, 0))

        self.gridLayout.addWidget(self.order_number_textbox, 13, 1, 1, 1)

        self.caller_textbox = QLineEdit(self.centralwidget)
        self.caller_textbox.setObjectName(u"caller_textbox")
        self.caller_textbox.setMinimumSize(QSize(250, 0))

        self.gridLayout.addWidget(self.caller_textbox, 5, 0, 1, 1)

        self.phone_label = QLabel(self.centralwidget)
        self.phone_label.setObjectName(u"phone_label")
        self.phone_label.setMinimumSize(QSize(250, 0))
        self.phone_label.setMaximumSize(QSize(16777215, 20))

        self.gridLayout.addWidget(self.phone_label, 4, 1, 1, 1)

        self.short_description_textbox = QPlainTextEdit(self.centralwidget)
        self.short_description_textbox.setObjectName(u"short_description_textbox")
        self.short_description_textbox.setMinimumSize(QSize(250, 0))
        palette = QPalette()
        brush = QBrush(QColor(33, 33, 33, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        self.short_description_textbox.setPalette(palette)
        self.short_description_textbox.setTabChangesFocus(True)

        self.gridLayout.addWidget(self.short_description_textbox, 11, 0, 1, 2)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 551, 24))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.date_edit, self.time_edit)
        QWidget.setTabOrder(self.time_edit, self.dealer_combobox)
        QWidget.setTabOrder(self.dealer_combobox, self.account_number_textbox)
        QWidget.setTabOrder(self.account_number_textbox, self.caller_textbox)
        QWidget.setTabOrder(self.caller_textbox, self.phone_textbox)
        QWidget.setTabOrder(self.phone_textbox, self.model_number_textbox)
        QWidget.setTabOrder(self.model_number_textbox, self.serial_number_textbox)
        QWidget.setTabOrder(self.serial_number_textbox, self.radioButton)
        QWidget.setTabOrder(self.radioButton, self.radioButton_2)
        QWidget.setTabOrder(self.radioButton_2, self.radioButton_3)
        QWidget.setTabOrder(self.radioButton_3, self.short_description_textbox)
        QWidget.setTabOrder(self.short_description_textbox, self.po_textbox)
        QWidget.setTabOrder(self.po_textbox, self.order_number_textbox)
        QWidget.setTabOrder(self.order_number_textbox, self.reset_button)
        QWidget.setTabOrder(self.reset_button, self.save_button)

        self.retranslateUi(MainWindow)

        self.save_button.setDefault(True)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Carrierade", None))
        self.date_label.setText(QCoreApplication.translate("MainWindow", u"Date", None))
        self.warranty_label.setText(QCoreApplication.translate("MainWindow", u"Confirmed Warranty?", None))
        self.reset_button.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.save_button.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.model_line_edit.setText(QCoreApplication.translate("MainWindow", u"Model Number", None))
        self.order_number_label.setText(QCoreApplication.translate("MainWindow", u"Order Number", None))
        self.po_label.setText(QCoreApplication.translate("MainWindow", u"PO", None))
        self.dealer_label.setText(QCoreApplication.translate("MainWindow", u"Dealer", None))
        self.account_label.setText(QCoreApplication.translate("MainWindow", u"Account Number", None))
        self.caller_label.setText(QCoreApplication.translate("MainWindow", u"Caller", None))
        self.description_label.setText(QCoreApplication.translate("MainWindow", u"Short Description", None))
        self.serial_number_label.setText(QCoreApplication.translate("MainWindow", u"Serial Number", None))
        self.time_edit.setDisplayFormat(QCoreApplication.translate("MainWindow", u"hh:mm:ss\u202fAP", None))
        self.time_label.setText(QCoreApplication.translate("MainWindow", u"Time", None))
        self.date_edit.setDisplayFormat(QCoreApplication.translate("MainWindow", u"MM/dd/yyyy", None))
        self.groupBox.setTitle("")
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"Yes", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"No", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.dealer_combobox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Select Dealer", None))
        self.phone_label.setText(QCoreApplication.translate("MainWindow", u"Phone", None))
    # retranslateUi

