# Form implementation generated from reading ui file 'c:\Users\torre\Documents\INFO MANAGEMENT\FinalProject\ui\Booking_details.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1010, 560)
        Form.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.label_91 = QtWidgets.QLabel(parent=Form)
        self.label_91.setGeometry(QtCore.QRect(230, 270, 71, 16))
        self.label_91.setStyleSheet("font: 8pt \"Segoe UI\";\n"
"color: white;\n"
"background-color: black;")
        self.label_91.setObjectName("label_91")
        self.label_96 = QtWidgets.QLabel(parent=Form)
        self.label_96.setGeometry(QtCore.QRect(490, 210, 91, 16))
        self.label_96.setStyleSheet("font: 8pt \"Segoe UI\";\n"
"color: white;\n"
"background-color: black;")
        self.label_96.setObjectName("label_96")
        self.label_92 = QtWidgets.QLabel(parent=Form)
        self.label_92.setGeometry(QtCore.QRect(230, 330, 71, 16))
        self.label_92.setStyleSheet("font: 8pt \"Segoe UI\";\n"
"color: white;\n"
"background-color: black;")
        self.label_92.setObjectName("label_92")
        self.label_90 = QtWidgets.QLabel(parent=Form)
        self.label_90.setGeometry(QtCore.QRect(230, 210, 71, 16))
        self.label_90.setStyleSheet("font: 8pt \"Segoe UI\";\n"
"color: white;\n"
"background-color: black;")
        self.label_90.setObjectName("label_90")
        self.label_10 = QtWidgets.QLabel(parent=Form)
        self.label_10.setGeometry(QtCore.QRect(230, 60, 111, 21))
        self.label_10.setObjectName("label_10")
        self.label_93 = QtWidgets.QLabel(parent=Form)
        self.label_93.setGeometry(QtCore.QRect(230, 390, 91, 16))
        self.label_93.setStyleSheet("font: 8pt \"Segoe UI\";\n"
"color: white;\n"
"background-color: black;")
        self.label_93.setObjectName("label_93")
        self.txt_totspending = QtWidgets.QLineEdit(parent=Form)
        self.txt_totspending.setGeometry(QtCore.QRect(230, 410, 221, 31))
        self.txt_totspending.setStyleSheet("background-color: white;\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 5px;")
        self.txt_totspending.setObjectName("txt_totspending")
        self.label_98 = QtWidgets.QLabel(parent=Form)
        self.label_98.setGeometry(QtCore.QRect(490, 330, 91, 16))
        self.label_98.setStyleSheet("font: 8pt \"Segoe UI\";\n"
"color: white;\n"
"background-color: black;")
        self.label_98.setObjectName("label_98")
        self.label_102 = QtWidgets.QLabel(parent=Form)
        self.label_102.setGeometry(QtCore.QRect(750, 280, 131, 16))
        self.label_102.setStyleSheet("font: 8pt \"Segoe UI\";\n"
"color: white;\n"
"background-color: black;")
        self.label_102.setObjectName("label_102")
        self.date_end = QtWidgets.QDateEdit(parent=Form)
        self.date_end.setGeometry(QtCore.QRect(490, 350, 221, 31))
        self.date_end.setStyleSheet("background-color: white;\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 5px;")
        self.date_end.setMinimumDate(QtCore.QDate(2012, 1, 1))
        self.date_end.setCalendarPopup(True)
        self.date_end.setObjectName("date_end")
        self.btn_booking_update = QtWidgets.QPushButton(parent=Form)
        self.btn_booking_update.setGeometry(QtCore.QRect(810, 480, 81, 31))
        self.btn_booking_update.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(30, 184, 255);\n"
"border-radius: 5px;")
        self.btn_booking_update.setObjectName("btn_booking_update")
        self.txt_booking_vehicleplate_2 = QtWidgets.QLineEdit(parent=Form)
        self.txt_booking_vehicleplate_2.setEnabled(False)
        self.txt_booking_vehicleplate_2.setGeometry(QtCore.QRect(750, 110, 221, 31))
        self.txt_booking_vehicleplate_2.setStyleSheet("background-color: white;\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 5px;")
        self.txt_booking_vehicleplate_2.setObjectName("txt_booking_vehicleplate_2")
        self.txt_booking_vehicle_type = QtWidgets.QLineEdit(parent=Form)
        self.txt_booking_vehicle_type.setEnabled(False)
        self.txt_booking_vehicle_type.setGeometry(QtCore.QRect(230, 170, 221, 31))
        self.txt_booking_vehicle_type.setStyleSheet("background-color: white;\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 5px;")
        self.txt_booking_vehicle_type.setObjectName("txt_booking_vehicle_type")
        self.label_95 = QtWidgets.QLabel(parent=Form)
        self.label_95.setGeometry(QtCore.QRect(490, 150, 91, 16))
        self.label_95.setStyleSheet("font: 8pt \"Segoe UI\";\n"
"color: white;\n"
"background-color: black;")
        self.label_95.setObjectName("label_95")
        self.txt_booking_details = QtWidgets.QTextEdit(parent=Form)
        self.txt_booking_details.setGeometry(QtCore.QRect(750, 300, 221, 81))
        self.txt_booking_details.setStyleSheet("background-color: white;\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 5px;")
        self.txt_booking_details.setObjectName("txt_booking_details")
        self.label_94 = QtWidgets.QLabel(parent=Form)
        self.label_94.setGeometry(QtCore.QRect(490, 90, 91, 16))
        self.label_94.setStyleSheet("font: 8pt \"Segoe UI\";\n"
"color: white;\n"
"background-color: black;")
        self.label_94.setObjectName("label_94")
        self.txt_booking_cusname = QtWidgets.QLineEdit(parent=Form)
        self.txt_booking_cusname.setEnabled(False)
        self.txt_booking_cusname.setGeometry(QtCore.QRect(230, 110, 221, 31))
        self.txt_booking_cusname.setStyleSheet("background-color: white;\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 5px;")
        self.txt_booking_cusname.setText("")
        self.txt_booking_cusname.setObjectName("txt_booking_cusname")
        self.label_101 = QtWidgets.QLabel(parent=Form)
        self.label_101.setGeometry(QtCore.QRect(750, 210, 131, 16))
        self.label_101.setStyleSheet("font: 8pt \"Segoe UI\";\n"
"color: white;\n"
"background-color: black;")
        self.label_101.setObjectName("label_101")
        self.date_booked = QtWidgets.QDateEdit(parent=Form)
        self.date_booked.setGeometry(QtCore.QRect(230, 290, 221, 31))
        self.date_booked.setStyleSheet("background-color: white;\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 5px;")
        self.date_booked.setMinimumDate(QtCore.QDate(2012, 1, 1))
        self.date_booked.setCalendarPopup(True)
        self.date_booked.setObjectName("date_booked")
        self.drp_booking_status = QtWidgets.QComboBox(parent=Form)
        self.drp_booking_status.setGeometry(QtCore.QRect(490, 290, 221, 31))
        self.drp_booking_status.setStyleSheet("background-color: white;\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 5px;")
        self.drp_booking_status.setObjectName("drp_booking_status")
        self.drp_booking_status.addItem("")
        self.drp_booking_status.addItem("")
        self.label_97 = QtWidgets.QLabel(parent=Form)
        self.label_97.setGeometry(QtCore.QRect(490, 270, 91, 16))
        self.label_97.setStyleSheet("font: 8pt \"Segoe UI\";\n"
"color: white;\n"
"background-color: black;")
        self.label_97.setObjectName("label_97")
        self.label_100 = QtWidgets.QLabel(parent=Form)
        self.label_100.setGeometry(QtCore.QRect(750, 150, 131, 16))
        self.label_100.setStyleSheet("font: 8pt \"Segoe UI\";\n"
"color: white;\n"
"background-color: black;")
        self.label_100.setObjectName("label_100")
        self.label_89 = QtWidgets.QLabel(parent=Form)
        self.label_89.setGeometry(QtCore.QRect(230, 150, 71, 16))
        self.label_89.setStyleSheet("font: 8pt \"Segoe UI\";\n"
"color: white;\n"
"background-color: black;")
        self.label_89.setObjectName("label_89")
        self.label_99 = QtWidgets.QLabel(parent=Form)
        self.label_99.setGeometry(QtCore.QRect(750, 90, 131, 16))
        self.label_99.setStyleSheet("font: 8pt \"Segoe UI\";\n"
"color: white;\n"
"background-color: black;")
        self.label_99.setObjectName("label_99")
        self.btn_booking_cancel = QtWidgets.QPushButton(parent=Form)
        self.btn_booking_cancel.setGeometry(QtCore.QRect(900, 480, 81, 31))
        self.btn_booking_cancel.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(148, 148, 148);\n"
"border-radius: 5px;")
        self.btn_booking_cancel.setObjectName("btn_booking_cancel")
        self.date_start = QtWidgets.QDateEdit(parent=Form)
        self.date_start.setGeometry(QtCore.QRect(230, 350, 221, 31))
        self.date_start.setStyleSheet("background-color: white;\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 5px;")
        self.date_start.setMinimumDate(QtCore.QDate(2012, 1, 1))
        self.date_start.setCalendarPopup(True)
        self.date_start.setObjectName("date_start")
        self.txt_booking_vehiclebrand = QtWidgets.QLineEdit(parent=Form)
        self.txt_booking_vehiclebrand.setEnabled(False)
        self.txt_booking_vehiclebrand.setGeometry(QtCore.QRect(490, 170, 221, 31))
        self.txt_booking_vehiclebrand.setStyleSheet("background-color: white;\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 5px;")
        self.txt_booking_vehiclebrand.setObjectName("txt_booking_vehiclebrand")
        self.txt_booking_service_type = QtWidgets.QLineEdit(parent=Form)
        self.txt_booking_service_type.setEnabled(False)
        self.txt_booking_service_type.setGeometry(QtCore.QRect(490, 230, 221, 31))
        self.txt_booking_service_type.setStyleSheet("background-color: white;\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 5px;")
        self.txt_booking_service_type.setObjectName("txt_booking_service_type")
        self.txt_booking_service = QtWidgets.QLineEdit(parent=Form)
        self.txt_booking_service.setEnabled(False)
        self.txt_booking_service.setGeometry(QtCore.QRect(230, 230, 221, 31))
        self.txt_booking_service.setStyleSheet("background-color: white;\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 5px;")
        self.txt_booking_service.setObjectName("txt_booking_service")
        self.label_88 = QtWidgets.QLabel(parent=Form)
        self.label_88.setGeometry(QtCore.QRect(230, 90, 91, 16))
        self.label_88.setStyleSheet("font: 8pt \"Segoe UI\";\n"
"color: white;\n"
"background-color: black;")
        self.label_88.setObjectName("label_88")
        self.txt_booking_service_cat = QtWidgets.QLineEdit(parent=Form)
        self.txt_booking_service_cat.setEnabled(False)
        self.txt_booking_service_cat.setGeometry(QtCore.QRect(490, 110, 221, 31))
        self.txt_booking_service_cat.setStyleSheet("background-color: white;\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 5px;")
        self.txt_booking_service_cat.setObjectName("txt_booking_service_cat")
        self.txt_booking_vehicle_model = QtWidgets.QLineEdit(parent=Form)
        self.txt_booking_vehicle_model.setEnabled(False)
        self.txt_booking_vehicle_model.setGeometry(QtCore.QRect(750, 170, 221, 31))
        self.txt_booking_vehicle_model.setStyleSheet("background-color: white;\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 5px;")
        self.txt_booking_vehicle_model.setObjectName("txt_booking_vehicle_model")
        self.btn_books = QtWidgets.QPushButton(parent=Form)
        self.btn_books.setGeometry(QtCore.QRect(30, 230, 131, 31))
        self.btn_books.setStyleSheet("border-style: none;\n"
"color: #FC8100;\n"
"border-radius: 15px;\n"
"background-color: #1E1E1E;\n"
"")
        self.btn_books.setObjectName("btn_books")
        self.btn_dashboard = QtWidgets.QPushButton(parent=Form)
        self.btn_dashboard.setGeometry(QtCore.QRect(20, 160, 151, 31))
        self.btn_dashboard.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.btn_dashboard.setObjectName("btn_dashboard")
        self.btn_invoice = QtWidgets.QPushButton(parent=Form)
        self.btn_invoice.setGeometry(QtCore.QRect(40, 310, 111, 31))
        self.btn_invoice.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.btn_invoice.setObjectName("btn_invoice")
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 191, 701))
        self.label.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setGeometry(QtCore.QRect(0, 90, 191, 16))
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.attendant_name = QtWidgets.QLabel(parent=Form)
        self.attendant_name.setGeometry(QtCore.QRect(80, 40, 91, 16))
        self.attendant_name.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"")
        self.attendant_name.setObjectName("attendant_name")
        self.btn_settings = QtWidgets.QPushButton(parent=Form)
        self.btn_settings.setGeometry(QtCore.QRect(10, 510, 31, 24))
        self.btn_settings.setStyleSheet("border-style: none;\n"
"background-color: rgb(0, 0, 0);")
        self.btn_settings.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\torre\\Documents\\INFO MANAGEMENT\\FinalProject\\ui\\../img/settingsIM.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_settings.setIcon(icon)
        self.btn_settings.setIconSize(QtCore.QSize(20, 20))
        self.btn_settings.setObjectName("btn_settings")
        self.label_33 = QtWidgets.QLabel(parent=Form)
        self.label_33.setGeometry(QtCore.QRect(20, 20, 41, 41))
        self.label_33.setStyleSheet("border-style: none;\n"
"background-color: black;\n"
"")
        self.label_33.setText("")
        self.label_33.setPixmap(QtGui.QPixmap("c:\\Users\\torre\\Documents\\INFO MANAGEMENT\\FinalProject\\ui\\../img/ARMS_LGO(1).png"))
        self.label_33.setScaledContents(True)
        self.label_33.setObjectName("label_33")
        self.btn_customer = QtWidgets.QPushButton(parent=Form)
        self.btn_customer.setGeometry(QtCore.QRect(40, 380, 111, 31))
        self.btn_customer.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.btn_customer.setObjectName("btn_customer")
        self.label_13 = QtWidgets.QLabel(parent=Form)
        self.label_13.setGeometry(QtCore.QRect(80, 20, 61, 16))
        self.label_13.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.label_13.setObjectName("label_13")
        self.txt_booking_assignedto = QtWidgets.QComboBox(parent=Form)
        self.txt_booking_assignedto.setGeometry(QtCore.QRect(750, 240, 221, 31))
        self.txt_booking_assignedto.setStyleSheet("background-color: white;\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 5px;")
        self.txt_booking_assignedto.setObjectName("txt_booking_assignedto")
        self.label_34 = QtWidgets.QLabel(parent=Form)
        self.label_34.setGeometry(QtCore.QRect(210, 40, 791, 431))
        self.label_34.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border-radius: 10px;")
        self.label_34.setText("")
        self.label_34.setObjectName("label_34")
        self.label_34.raise_()
        self.label.raise_()
        self.btn_settings.raise_()
        self.label_13.raise_()
        self.btn_customer.raise_()
        self.attendant_name.raise_()
        self.label_33.raise_()
        self.btn_dashboard.raise_()
        self.label_2.raise_()
        self.btn_books.raise_()
        self.btn_invoice.raise_()
        self.label_91.raise_()
        self.label_96.raise_()
        self.label_92.raise_()
        self.label_90.raise_()
        self.label_10.raise_()
        self.label_93.raise_()
        self.txt_totspending.raise_()
        self.label_98.raise_()
        self.label_102.raise_()
        self.date_end.raise_()
        self.btn_booking_update.raise_()
        self.txt_booking_vehicleplate_2.raise_()
        self.txt_booking_vehicle_type.raise_()
        self.label_95.raise_()
        self.txt_booking_details.raise_()
        self.label_94.raise_()
        self.txt_booking_cusname.raise_()
        self.label_101.raise_()
        self.date_booked.raise_()
        self.drp_booking_status.raise_()
        self.label_97.raise_()
        self.label_100.raise_()
        self.label_89.raise_()
        self.label_99.raise_()
        self.btn_booking_cancel.raise_()
        self.date_start.raise_()
        self.txt_booking_vehiclebrand.raise_()
        self.txt_booking_service_type.raise_()
        self.txt_booking_service.raise_()
        self.label_88.raise_()
        self.txt_booking_service_cat.raise_()
        self.txt_booking_vehicle_model.raise_()
        self.txt_booking_assignedto.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_91.setText(_translate("Form", "Date Booked"))
        self.label_96.setText(_translate("Form", "Service Type"))
        self.label_92.setText(_translate("Form", "Date Start"))
        self.label_90.setText(_translate("Form", "Service"))
        self.label_10.setStyleSheet(_translate("Form", "font: 8pt \"Segoe UI\";\n"
"color: white;\n"
"background-color: black;"))
        self.label_10.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:700;\">BOOKING DETAILS</span></p></body></html>"))
        self.label_93.setText(_translate("Form", "Total Spendings"))
        self.label_98.setText(_translate("Form", "Date End"))
        self.label_102.setText(_translate("Form", "Details"))
        self.btn_booking_update.setText(_translate("Form", "UPDATE"))
        self.label_95.setText(_translate("Form", "Vehicle Brand"))
        self.label_94.setText(_translate("Form", "Service Category"))
        self.label_101.setText(_translate("Form", "Assigned To"))
        self.drp_booking_status.setItemText(0, _translate("Form", "Pending"))
        self.drp_booking_status.setItemText(1, _translate("Form", "Completed"))
        self.label_97.setText(_translate("Form", "Status"))
        self.label_100.setText(_translate("Form", "Vehicle Model"))
        self.label_89.setText(_translate("Form", "Vehicle Type"))
        self.label_99.setText(_translate("Form", "Vehicle Registration Plate"))
        self.btn_booking_cancel.setText(_translate("Form", "CANCEL"))
        self.label_88.setText(_translate("Form", "Customer Name"))
        self.btn_books.setText(_translate("Form", "BOOK"))
        self.btn_dashboard.setText(_translate("Form", "DASHBOARD"))
        self.btn_invoice.setText(_translate("Form", "INVOICE"))
        self.attendant_name.setText(_translate("Form", "attendant_name"))
        self.btn_customer.setText(_translate("Form", "CUSTOMER"))
        self.label_13.setText(_translate("Form", "WELCOME"))
