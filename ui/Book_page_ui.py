# Form implementation generated from reading ui file 'c:\Users\torre\Documents\INFO MANAGEMENT\FinalProject\ui\Book_page.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_BookPageWindow(object):
    def setupUi(self, BookPageWindow):
        BookPageWindow.setObjectName("BookPageWindow")
        BookPageWindow.resize(1009, 550)
        BookPageWindow.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.label_149 = QtWidgets.QLabel(parent=BookPageWindow)
        self.label_149.setGeometry(QtCore.QRect(210, 60, 131, 16))
        self.label_149.setObjectName("label_149")
        self.txt_vehicleplate = QtWidgets.QLineEdit(parent=BookPageWindow)
        self.txt_vehicleplate.setGeometry(QtCore.QRect(480, 80, 201, 31))
        self.txt_vehicleplate.setStyleSheet("background-color: white;\n"
"border-radius: 5px;")
        self.txt_vehicleplate.setObjectName("txt_vehicleplate")
        self.label_154 = QtWidgets.QLabel(parent=BookPageWindow)
        self.label_154.setGeometry(QtCore.QRect(210, 120, 81, 16))
        self.label_154.setObjectName("label_154")
        self.txt_cusid = QtWidgets.QLineEdit(parent=BookPageWindow)
        self.txt_cusid.setGeometry(QtCore.QRect(210, 80, 201, 31))
        self.txt_cusid.setStyleSheet("background-color: white;\n"
"border-radius: 5px;")
        self.txt_cusid.setText("")
        self.txt_cusid.setClearButtonEnabled(False)
        self.txt_cusid.setObjectName("txt_cusid")
        self.btn_cancel = QtWidgets.QPushButton(parent=BookPageWindow)
        self.btn_cancel.setGeometry(QtCore.QRect(860, 470, 81, 31))
        self.btn_cancel.setStyleSheet("background-color: rgb(147, 154, 153);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.btn_cancel.setObjectName("btn_cancel")
        self.btn_submit = QtWidgets.QPushButton(parent=BookPageWindow)
        self.btn_submit.setGeometry(QtCore.QRect(770, 470, 81, 31))
        self.btn_submit.setStyleSheet("background-color: rgb(44, 171, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.btn_submit.setObjectName("btn_submit")
        self.label_155 = QtWidgets.QLabel(parent=BookPageWindow)
        self.label_155.setGeometry(QtCore.QRect(480, 120, 81, 16))
        self.label_155.setObjectName("label_155")
        self.label_153 = QtWidgets.QLabel(parent=BookPageWindow)
        self.label_153.setGeometry(QtCore.QRect(730, 60, 71, 16))
        self.label_153.setObjectName("label_153")
        self.drp_vehicle_type = QtWidgets.QComboBox(parent=BookPageWindow)
        self.drp_vehicle_type.setGeometry(QtCore.QRect(730, 80, 201, 31))
        self.drp_vehicle_type.setStyleSheet("background-color: white;\n"
"border-radius: 5px;")
        self.drp_vehicle_type.setObjectName("drp_vehicle_type")
        self.drp_vehicle_type.addItem("")
        self.drp_vehicle_type.addItem("")
        self.drp_vehicle_type.addItem("")
        self.drp_vehicle_type.addItem("")
        self.drp_vehicle_type.addItem("")
        self.label_152 = QtWidgets.QLabel(parent=BookPageWindow)
        self.label_152.setGeometry(QtCore.QRect(480, 60, 141, 16))
        self.label_152.setObjectName("label_152")
        self.btn_settings = QtWidgets.QPushButton(parent=BookPageWindow)
        self.btn_settings.setGeometry(QtCore.QRect(10, 510, 31, 24))
        self.btn_settings.setStyleSheet("border-style: none;\n"
"background-color: rgb(0, 0, 0);")
        self.btn_settings.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\torre\\Documents\\INFO MANAGEMENT\\FinalProject\\ui\\../img/settingsIM.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_settings.setIcon(icon)
        self.btn_settings.setIconSize(QtCore.QSize(20, 20))
        self.btn_settings.setObjectName("btn_settings")
        self.label_33 = QtWidgets.QLabel(parent=BookPageWindow)
        self.label_33.setGeometry(QtCore.QRect(20, 20, 41, 41))
        self.label_33.setStyleSheet("border-style: none;\n"
"background-color: black;\n"
"")
        self.label_33.setText("")
        self.label_33.setPixmap(QtGui.QPixmap("c:\\Users\\torre\\Documents\\INFO MANAGEMENT\\FinalProject\\ui\\../img/ARMS_LGO(1).png"))
        self.label_33.setScaledContents(True)
        self.label_33.setObjectName("label_33")
        self.btn_dashboard = QtWidgets.QPushButton(parent=BookPageWindow)
        self.btn_dashboard.setGeometry(QtCore.QRect(20, 160, 151, 31))
        self.btn_dashboard.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.btn_dashboard.setObjectName("btn_dashboard")
        self.btn_customer = QtWidgets.QPushButton(parent=BookPageWindow)
        self.btn_customer.setGeometry(QtCore.QRect(40, 380, 111, 31))
        self.btn_customer.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.btn_customer.setObjectName("btn_customer")
        self.attendant_name = QtWidgets.QLabel(parent=BookPageWindow)
        self.attendant_name.setGeometry(QtCore.QRect(80, 40, 91, 16))
        self.attendant_name.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"")
        self.attendant_name.setObjectName("attendant_name")
        self.label_13 = QtWidgets.QLabel(parent=BookPageWindow)
        self.label_13.setGeometry(QtCore.QRect(80, 20, 61, 16))
        self.label_13.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.label_13.setObjectName("label_13")
        self.btn_books = QtWidgets.QPushButton(parent=BookPageWindow)
        self.btn_books.setGeometry(QtCore.QRect(30, 230, 131, 31))
        self.btn_books.setStyleSheet("border-style: none;\n"
"color: #FC8100;\n"
"border-radius: 15px;\n"
"background-color: #1E1E1E;\n"
"")
        self.btn_books.setObjectName("btn_books")
        self.label = QtWidgets.QLabel(parent=BookPageWindow)
        self.label.setGeometry(QtCore.QRect(0, 0, 191, 701))
        self.label.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.btn_invoice = QtWidgets.QPushButton(parent=BookPageWindow)
        self.btn_invoice.setGeometry(QtCore.QRect(40, 310, 111, 31))
        self.btn_invoice.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.btn_invoice.setObjectName("btn_invoice")
        self.label_2 = QtWidgets.QLabel(parent=BookPageWindow)
        self.label_2.setGeometry(QtCore.QRect(0, 90, 191, 16))
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.txt_vehicle_brand = QtWidgets.QLineEdit(parent=BookPageWindow)
        self.txt_vehicle_brand.setGeometry(QtCore.QRect(210, 140, 201, 31))
        self.txt_vehicle_brand.setStyleSheet("background-color: white;\n"
"border-radius: 5px;")
        self.txt_vehicle_brand.setObjectName("txt_vehicle_brand")
        self.txt_vehicle_model = QtWidgets.QLineEdit(parent=BookPageWindow)
        self.txt_vehicle_model.setGeometry(QtCore.QRect(480, 140, 201, 31))
        self.txt_vehicle_model.setStyleSheet("background-color: white;\n"
"border-radius: 5px;")
        self.txt_vehicle_model.setObjectName("txt_vehicle_model")
        self.btn_searchcus = QtWidgets.QPushButton(parent=BookPageWindow)
        self.btn_searchcus.setGeometry(QtCore.QRect(370, 80, 41, 31))
        self.btn_searchcus.setStyleSheet("background-color: white;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.btn_searchcus.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("c:\\Users\\torre\\Documents\\INFO MANAGEMENT\\FinalProject\\ui\\../img/search.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_searchcus.setIcon(icon1)
        self.btn_searchcus.setObjectName("btn_searchcus")
        self.label_151 = QtWidgets.QLabel(parent=BookPageWindow)
        self.label_151.setGeometry(QtCore.QRect(730, 120, 91, 16))
        self.label_151.setStyleSheet("color:black;\n"
"")
        self.label_151.setObjectName("label_151")
        self.drp_service_cat = QtWidgets.QComboBox(parent=BookPageWindow)
        self.drp_service_cat.setGeometry(QtCore.QRect(730, 140, 201, 31))
        self.drp_service_cat.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.drp_service_cat.setObjectName("drp_service_cat")
        self.drp_service_cat.addItem("")
        self.drp_service_cat.addItem("")
        self.drp_service_cat.addItem("")
        self.drp_service_cat.addItem("")
        self.drp_service_cat.addItem("")
        self.drp_service_cat.addItem("")
        self.drp_service_cat.addItem("")
        self.txt_details = QtWidgets.QPlainTextEdit(parent=BookPageWindow)
        self.txt_details.setGeometry(QtCore.QRect(270, 320, 211, 91))
        self.txt_details.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.txt_details.setObjectName("txt_details")
        self.label_81 = QtWidgets.QLabel(parent=BookPageWindow)
        self.label_81.setGeometry(QtCore.QRect(550, 300, 71, 16))
        self.label_81.setStyleSheet("color:white;\n"
"background-color: black;")
        self.label_81.setObjectName("label_81")
        self.drp_service_type = QtWidgets.QComboBox(parent=BookPageWindow)
        self.drp_service_type.setGeometry(QtCore.QRect(270, 260, 211, 31))
        self.drp_service_type.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.drp_service_type.setObjectName("drp_service_type")
        self.drp_service_type.addItem("")
        self.drp_service_type.addItem("")
        self.label_79 = QtWidgets.QLabel(parent=BookPageWindow)
        self.label_79.setGeometry(QtCore.QRect(270, 300, 71, 16))
        self.label_79.setStyleSheet("color:white;\n"
"background-color: black;")
        self.label_79.setObjectName("label_79")
        self.label_80 = QtWidgets.QLabel(parent=BookPageWindow)
        self.label_80.setGeometry(QtCore.QRect(270, 240, 71, 16))
        self.label_80.setStyleSheet("color:white;\n"
"background-color: black;")
        self.label_80.setObjectName("label_80")
        self.label_77 = QtWidgets.QLabel(parent=BookPageWindow)
        self.label_77.setGeometry(QtCore.QRect(550, 240, 49, 16))
        self.label_77.setStyleSheet("color:white;\n"
"background-color: black;")
        self.label_77.setObjectName("label_77")
        self.drp_assigned = QtWidgets.QComboBox(parent=BookPageWindow)
        self.drp_assigned.setGeometry(QtCore.QRect(550, 320, 211, 31))
        self.drp_assigned.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.drp_assigned.setObjectName("drp_assigned")
        self.drp_service = QtWidgets.QComboBox(parent=BookPageWindow)
        self.drp_service.setGeometry(QtCore.QRect(550, 260, 211, 31))
        self.drp_service.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.drp_service.setObjectName("drp_service")
        self.label_34 = QtWidgets.QLabel(parent=BookPageWindow)
        self.label_34.setGeometry(QtCore.QRect(210, 210, 741, 241))
        self.label_34.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border-radius: 10px;")
        self.label_34.setText("")
        self.label_34.setObjectName("label_34")
        self.label_78 = QtWidgets.QLabel(parent=BookPageWindow)
        self.label_78.setGeometry(QtCore.QRect(550, 360, 71, 16))
        self.label_78.setStyleSheet("color:white;\n"
"background-color: black;")
        self.label_78.setObjectName("label_78")
        self.txt_service_fee = QtWidgets.QLineEdit(parent=BookPageWindow)
        self.txt_service_fee.setGeometry(QtCore.QRect(550, 380, 211, 31))
        self.txt_service_fee.setStyleSheet("background-color: white;\n"
"border-radius: 5px;")
        self.txt_service_fee.setReadOnly(True)
        self.txt_service_fee.setObjectName("txt_service_fee")
        self.label_34.raise_()
        self.label.raise_()
        self.label_149.raise_()
        self.txt_vehicleplate.raise_()
        self.label_154.raise_()
        self.txt_cusid.raise_()
        self.btn_cancel.raise_()
        self.btn_submit.raise_()
        self.label_155.raise_()
        self.label_153.raise_()
        self.drp_vehicle_type.raise_()
        self.label_152.raise_()
        self.btn_settings.raise_()
        self.label_33.raise_()
        self.btn_dashboard.raise_()
        self.btn_customer.raise_()
        self.attendant_name.raise_()
        self.label_13.raise_()
        self.btn_books.raise_()
        self.btn_invoice.raise_()
        self.label_2.raise_()
        self.txt_vehicle_brand.raise_()
        self.txt_vehicle_model.raise_()
        self.btn_searchcus.raise_()
        self.label_151.raise_()
        self.drp_service_cat.raise_()
        self.txt_details.raise_()
        self.label_81.raise_()
        self.drp_service_type.raise_()
        self.label_79.raise_()
        self.label_80.raise_()
        self.label_77.raise_()
        self.drp_assigned.raise_()
        self.drp_service.raise_()
        self.label_78.raise_()
        self.txt_service_fee.raise_()

        self.retranslateUi(BookPageWindow)
        QtCore.QMetaObject.connectSlotsByName(BookPageWindow)

    def retranslateUi(self, BookPageWindow):
        _translate = QtCore.QCoreApplication.translate
        BookPageWindow.setWindowTitle(_translate("BookPageWindow", "Form"))
        self.label_149.setText(_translate("BookPageWindow", "Customer ID"))
        self.label_154.setText(_translate("BookPageWindow", "Vehicle Brand"))
        self.btn_cancel.setText(_translate("BookPageWindow", "CANCEL"))
        self.btn_submit.setText(_translate("BookPageWindow", "SUBMIT"))
        self.label_155.setText(_translate("BookPageWindow", "Vehicle Model"))
        self.label_153.setText(_translate("BookPageWindow", "Vehicle Type"))
        self.drp_vehicle_type.setItemText(0, _translate("BookPageWindow", "2 Wheeler"))
        self.drp_vehicle_type.setItemText(1, _translate("BookPageWindow", "3 Wheeler"))
        self.drp_vehicle_type.setItemText(2, _translate("BookPageWindow", "4 Wheeler"))
        self.drp_vehicle_type.setItemText(3, _translate("BookPageWindow", "6 Wheeler"))
        self.drp_vehicle_type.setItemText(4, _translate("BookPageWindow", "8 Wheeler"))
        self.label_152.setText(_translate("BookPageWindow", "Vehicle Registration Plate"))
        self.btn_dashboard.setText(_translate("BookPageWindow", "DASHBOARD"))
        self.btn_customer.setText(_translate("BookPageWindow", "CUSTOMER"))
        self.attendant_name.setText(_translate("BookPageWindow", "attendant_name"))
        self.label_13.setText(_translate("BookPageWindow", "WELCOME"))
        self.btn_books.setText(_translate("BookPageWindow", "BOOK"))
        self.btn_invoice.setText(_translate("BookPageWindow", "INVOICE"))
        self.label_151.setText(_translate("BookPageWindow", "Service Category"))
        self.drp_service_cat.setItemText(0, _translate("BookPageWindow", "Vehicle Repair"))
        self.drp_service_cat.setItemText(1, _translate("BookPageWindow", "Vehicle Maintenance"))
        self.drp_service_cat.setItemText(2, _translate("BookPageWindow", "Diagnostic Services"))
        self.drp_service_cat.setItemText(3, _translate("BookPageWindow", "Body and Paint Services"))
        self.drp_service_cat.setItemText(4, _translate("BookPageWindow", "Tire Services"))
        self.drp_service_cat.setItemText(5, _translate("BookPageWindow", "Auto Detailing"))
        self.drp_service_cat.setItemText(6, _translate("BookPageWindow", "Air Conditioning Services"))
        self.label_81.setText(_translate("BookPageWindow", "Assigned To"))
        self.drp_service_type.setItemText(0, _translate("BookPageWindow", "Paid"))
        self.drp_service_type.setItemText(1, _translate("BookPageWindow", "Free"))
        self.label_79.setText(_translate("BookPageWindow", "Details"))
        self.label_80.setText(_translate("BookPageWindow", "Service Type"))
        self.label_77.setText(_translate("BookPageWindow", "Service"))
        self.label_78.setText(_translate("BookPageWindow", "Service Fee"))
