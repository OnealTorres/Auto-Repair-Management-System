# Form implementation generated from reading ui file 'c:\Users\torre\Documents\INFO MANAGEMENT\FinalProject\ui\Admin_dashboard.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_DashboardWindow(object):
    def setupUi(self, DashboardWindow):
        DashboardWindow.setObjectName("DashboardWindow")
        DashboardWindow.resize(1013, 615)
        DashboardWindow.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.label_2 = QtWidgets.QLabel(parent=DashboardWindow)
        self.label_2.setGeometry(QtCore.QRect(0, 90, 191, 16))
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.txt_admin_name = QtWidgets.QLabel(parent=DashboardWindow)
        self.txt_admin_name.setGeometry(QtCore.QRect(80, 40, 91, 16))
        self.txt_admin_name.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"")
        self.txt_admin_name.setObjectName("txt_admin_name")
        self.btn_settings = QtWidgets.QPushButton(parent=DashboardWindow)
        self.btn_settings.setGeometry(QtCore.QRect(10, 520, 31, 24))
        self.btn_settings.setStyleSheet("border-style: none;\n"
"background-color: rgb(0, 0, 0);")
        self.btn_settings.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\torre\\Documents\\INFO MANAGEMENT\\FinalProject\\ui\\../img/settingsIM.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_settings.setIcon(icon)
        self.btn_settings.setIconSize(QtCore.QSize(20, 20))
        self.btn_settings.setObjectName("btn_settings")
        self.label_13 = QtWidgets.QLabel(parent=DashboardWindow)
        self.label_13.setGeometry(QtCore.QRect(80, 20, 61, 16))
        self.label_13.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.label_13.setObjectName("label_13")
        self.label_33 = QtWidgets.QLabel(parent=DashboardWindow)
        self.label_33.setGeometry(QtCore.QRect(20, 20, 41, 41))
        self.label_33.setStyleSheet("border-style: none;\n"
"background-color: black;\n"
"")
        self.label_33.setText("")
        self.label_33.setPixmap(QtGui.QPixmap("c:\\Users\\torre\\Documents\\INFO MANAGEMENT\\FinalProject\\ui\\../img/ARMS_LGO(1).png"))
        self.label_33.setScaledContents(True)
        self.label_33.setObjectName("label_33")
        self.label_5 = QtWidgets.QLabel(parent=DashboardWindow)
        self.label_5.setGeometry(QtCore.QRect(390, 330, 31, 16))
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.label_5.setObjectName("label_5")
        self.label_23 = QtWidgets.QLabel(parent=DashboardWindow)
        self.label_23.setGeometry(QtCore.QRect(710, 70, 161, 141))
        self.label_23.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.label_23.setText("")
        self.label_23.setObjectName("label_23")
        self.label_4 = QtWidgets.QLabel(parent=DashboardWindow)
        self.label_4.setGeometry(QtCore.QRect(760, 180, 71, 16))
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.label_4.setObjectName("label_4")
        self.label_28 = QtWidgets.QLabel(parent=DashboardWindow)
        self.label_28.setGeometry(QtCore.QRect(710, 230, 161, 131))
        self.label_28.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.label_28.setText("")
        self.label_28.setObjectName("label_28")
        self.label_7 = QtWidgets.QLabel(parent=DashboardWindow)
        self.label_7.setGeometry(QtCore.QRect(760, 330, 51, 20))
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.label_7.setObjectName("label_7")
        self.label_22 = QtWidgets.QLabel(parent=DashboardWindow)
        self.label_22.setGeometry(QtCore.QRect(330, 70, 161, 141))
        self.label_22.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border-radius: 5px;")
        self.label_22.setText("")
        self.label_22.setObjectName("label_22")
        self.pushButton_5 = QtWidgets.QPushButton(parent=DashboardWindow)
        self.pushButton_5.setGeometry(QtCore.QRect(740, 90, 101, 71))
        self.pushButton_5.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"")
        self.pushButton_5.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("c:\\Users\\torre\\Documents\\INFO MANAGEMENT\\FinalProject\\ui\\../img/Employees.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_5.setIcon(icon1)
        self.pushButton_5.setIconSize(QtCore.QSize(80, 80))
        self.pushButton_5.setCheckable(False)
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_26 = QtWidgets.QLabel(parent=DashboardWindow)
        self.label_26.setGeometry(QtCore.QRect(330, 230, 161, 131))
        self.label_26.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.label_26.setText("")
        self.label_26.setObjectName("label_26")
        self.txt_numcustomer = QtWidgets.QLabel(parent=DashboardWindow)
        self.txt_numcustomer.setGeometry(QtCore.QRect(540, 160, 121, 20))
        self.txt_numcustomer.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.txt_numcustomer.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.txt_numcustomer.setObjectName("txt_numcustomer")
        self.label_29 = QtWidgets.QLabel(parent=DashboardWindow)
        self.label_29.setGeometry(QtCore.QRect(360, 80, 101, 81))
        self.label_29.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.label_29.setText("")
        self.label_29.setPixmap(QtGui.QPixmap("c:\\Users\\torre\\Documents\\INFO MANAGEMENT\\FinalProject\\ui\\../img/pendings.png"))
        self.label_29.setScaledContents(True)
        self.label_29.setObjectName("label_29")
        self.label_24 = QtWidgets.QLabel(parent=DashboardWindow)
        self.label_24.setGeometry(QtCore.QRect(520, 70, 161, 141))
        self.label_24.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.label_24.setText("")
        self.label_24.setObjectName("label_24")
        self.label_30 = QtWidgets.QLabel(parent=DashboardWindow)
        self.label_30.setGeometry(QtCore.QRect(560, 80, 81, 81))
        self.label_30.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.label_30.setText("")
        self.label_30.setPixmap(QtGui.QPixmap("c:\\Users\\torre\\Documents\\INFO MANAGEMENT\\FinalProject\\ui\\../img/cusotmer-removebg-preview.png"))
        self.label_30.setScaledContents(True)
        self.label_30.setObjectName("label_30")
        self.txt_numsales = QtWidgets.QLabel(parent=DashboardWindow)
        self.txt_numsales.setGeometry(QtCore.QRect(560, 310, 81, 16))
        self.txt_numsales.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.txt_numsales.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.txt_numsales.setObjectName("txt_numsales")
        self.txt_numpending = QtWidgets.QLabel(parent=DashboardWindow)
        self.txt_numpending.setGeometry(QtCore.QRect(350, 160, 121, 20))
        self.txt_numpending.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.txt_numpending.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.txt_numpending.setObjectName("txt_numpending")
        self.label_34 = QtWidgets.QLabel(parent=DashboardWindow)
        self.label_34.setGeometry(QtCore.QRect(240, 380, 741, 161))
        self.label_34.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border-radius: 10px;")
        self.label_34.setText("")
        self.label_34.setObjectName("label_34")
        self.label_6 = QtWidgets.QLabel(parent=DashboardWindow)
        self.label_6.setGeometry(QtCore.QRect(380, 180, 61, 21))
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.label_6.setObjectName("label_6")
        self.txt_numdues = QtWidgets.QLabel(parent=DashboardWindow)
        self.txt_numdues.setGeometry(QtCore.QRect(350, 310, 121, 21))
        self.txt_numdues.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.txt_numdues.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.txt_numdues.setObjectName("txt_numdues")
        self.label_8 = QtWidgets.QLabel(parent=DashboardWindow)
        self.label_8.setGeometry(QtCore.QRect(270, 390, 131, 21))
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: black;\n"
"")
        self.label_8.setObjectName("label_8")
        self.label_31 = QtWidgets.QLabel(parent=DashboardWindow)
        self.label_31.setGeometry(QtCore.QRect(560, 240, 81, 71))
        self.label_31.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.label_31.setText("")
        self.label_31.setPixmap(QtGui.QPixmap("c:\\Users\\torre\\Documents\\INFO MANAGEMENT\\FinalProject\\ui\\../img/Sale.png"))
        self.label_31.setScaledContents(True)
        self.label_31.setWordWrap(False)
        self.label_31.setObjectName("label_31")
        self.label_27 = QtWidgets.QLabel(parent=DashboardWindow)
        self.label_27.setGeometry(QtCore.QRect(520, 230, 161, 131))
        self.label_27.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.label_27.setText("")
        self.label_27.setObjectName("label_27")
        self.label_83 = QtWidgets.QLabel(parent=DashboardWindow)
        self.label_83.setGeometry(QtCore.QRect(750, 240, 81, 71))
        self.label_83.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_83.setText("")
        self.label_83.setPixmap(QtGui.QPixmap("c:\\Users\\torre\\Documents\\INFO MANAGEMENT\\FinalProject\\ui\\../img/Services.png"))
        self.label_83.setScaledContents(True)
        self.label_83.setObjectName("label_83")
        self.txt_numservice = QtWidgets.QLabel(parent=DashboardWindow)
        self.txt_numservice.setGeometry(QtCore.QRect(730, 316, 121, 20))
        self.txt_numservice.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.txt_numservice.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.txt_numservice.setObjectName("txt_numservice")
        self.txt_numemp = QtWidgets.QLabel(parent=DashboardWindow)
        self.txt_numemp.setGeometry(QtCore.QRect(730, 160, 121, 20))
        self.txt_numemp.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.txt_numemp.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.txt_numemp.setObjectName("txt_numemp")
        self.Customers = QtWidgets.QLabel(parent=DashboardWindow)
        self.Customers.setGeometry(QtCore.QRect(570, 180, 71, 16))
        self.Customers.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.Customers.setObjectName("Customers")
        self.label_9 = QtWidgets.QLabel(parent=DashboardWindow)
        self.label_9.setGeometry(QtCore.QRect(580, 326, 41, 16))
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.label_9.setObjectName("label_9")
        self.label_25 = QtWidgets.QLabel(parent=DashboardWindow)
        self.label_25.setGeometry(QtCore.QRect(370, 240, 71, 71))
        self.label_25.setAutoFillBackground(False)
        self.label_25.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.label_25.setText("")
        self.label_25.setPixmap(QtGui.QPixmap("c:\\Users\\torre\\Documents\\INFO MANAGEMENT\\FinalProject\\ui\\../img/Notification bell.png"))
        self.label_25.setScaledContents(True)
        self.label_25.setObjectName("label_25")
        self.tbl_dashboard = QtWidgets.QTableWidget(parent=DashboardWindow)
        self.tbl_dashboard.setEnabled(True)
        self.tbl_dashboard.setGeometry(QtCore.QRect(270, 420, 681, 101))
        self.tbl_dashboard.setAutoFillBackground(False)
        self.tbl_dashboard.setStyleSheet("background-color: white")
        self.tbl_dashboard.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tbl_dashboard.setRowCount(10)
        self.tbl_dashboard.setObjectName("tbl_dashboard")
        self.tbl_dashboard.setColumnCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_dashboard.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_dashboard.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_dashboard.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_dashboard.setHorizontalHeaderItem(3, item)
        self.tbl_dashboard.horizontalHeader().setDefaultSectionSize(160)
        self.btn_salesrep = QtWidgets.QPushButton(parent=DashboardWindow)
        self.btn_salesrep.setGeometry(QtCore.QRect(10, 490, 171, 31))
        self.btn_salesrep.setStyleSheet("border-style: none;\n"
"color: #fff;\n"
"\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.btn_salesrep.setObjectName("btn_salesrep")
        self.btn_books = QtWidgets.QPushButton(parent=DashboardWindow)
        self.btn_books.setGeometry(QtCore.QRect(20, 200, 151, 31))
        self.btn_books.setStyleSheet("border-style: none;\n"
"color: #fff;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"")
        self.btn_books.setObjectName("btn_books")
        self.btn_services = QtWidgets.QPushButton(parent=DashboardWindow)
        self.btn_services.setGeometry(QtCore.QRect(10, 380, 171, 31))
        self.btn_services.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"")
        self.btn_services.setObjectName("btn_services")
        self.btn_employees = QtWidgets.QPushButton(parent=DashboardWindow)
        self.btn_employees.setGeometry(QtCore.QRect(10, 430, 171, 31))
        self.btn_employees.setStyleSheet("border-style: none;\n"
"color: #fff;\n"
"\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.btn_employees.setObjectName("btn_employees")
        self.btn_customer = QtWidgets.QPushButton(parent=DashboardWindow)
        self.btn_customer.setGeometry(QtCore.QRect(20, 320, 151, 31))
        self.btn_customer.setStyleSheet("border-style: none;\n"
"color: #fff;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"")
        self.btn_customer.setObjectName("btn_customer")
        self.btn_invoice = QtWidgets.QPushButton(parent=DashboardWindow)
        self.btn_invoice.setGeometry(QtCore.QRect(20, 260, 151, 31))
        self.btn_invoice.setStyleSheet("border-style: none;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.btn_invoice.setObjectName("btn_invoice")
        self.btn_dashboard = QtWidgets.QPushButton(parent=DashboardWindow)
        self.btn_dashboard.setGeometry(QtCore.QRect(20, 140, 151, 31))
        self.btn_dashboard.setStyleSheet("border-style: none;\n"
"color: #FC8100;\n"
"border-radius: 15px;\n"
"background-color: #1E1E1E;\n"
"")
        self.btn_dashboard.setObjectName("btn_dashboard")
        self.label = QtWidgets.QLabel(parent=DashboardWindow)
        self.label.setGeometry(QtCore.QRect(0, 0, 191, 621))
        self.label.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label.raise_()
        self.label_24.raise_()
        self.label_28.raise_()
        self.label_27.raise_()
        self.label_26.raise_()
        self.label_2.raise_()
        self.txt_admin_name.raise_()
        self.label_13.raise_()
        self.label_33.raise_()
        self.label_5.raise_()
        self.label_23.raise_()
        self.label_4.raise_()
        self.label_7.raise_()
        self.label_22.raise_()
        self.pushButton_5.raise_()
        self.txt_numcustomer.raise_()
        self.label_29.raise_()
        self.label_30.raise_()
        self.txt_numsales.raise_()
        self.label_34.raise_()
        self.label_6.raise_()
        self.txt_numdues.raise_()
        self.label_8.raise_()
        self.label_31.raise_()
        self.label_83.raise_()
        self.txt_numservice.raise_()
        self.txt_numemp.raise_()
        self.Customers.raise_()
        self.label_9.raise_()
        self.label_25.raise_()
        self.tbl_dashboard.raise_()
        self.btn_salesrep.raise_()
        self.btn_books.raise_()
        self.btn_services.raise_()
        self.btn_employees.raise_()
        self.btn_customer.raise_()
        self.btn_invoice.raise_()
        self.btn_dashboard.raise_()
        self.btn_settings.raise_()
        self.txt_numpending.raise_()

        self.retranslateUi(DashboardWindow)
        QtCore.QMetaObject.connectSlotsByName(DashboardWindow)

    def retranslateUi(self, DashboardWindow):
        _translate = QtCore.QCoreApplication.translate
        DashboardWindow.setWindowTitle(_translate("DashboardWindow", "Dashboard"))
        self.txt_admin_name.setText(_translate("DashboardWindow", "ADMIN"))
        self.label_13.setText(_translate("DashboardWindow", "WELCOME"))
        self.label_5.setText(_translate("DashboardWindow", "DUES"))
        self.label_4.setText(_translate("DashboardWindow", "EMPLOYEES"))
        self.label_7.setText(_translate("DashboardWindow", "SERVICES"))
        self.txt_numcustomer.setText(_translate("DashboardWindow", "txt_numcustomer"))
        self.txt_numsales.setText(_translate("DashboardWindow", "txt_numsales"))
        self.txt_numpending.setText(_translate("DashboardWindow", "txt_numpending"))
        self.label_6.setText(_translate("DashboardWindow", "PENDING"))
        self.txt_numdues.setText(_translate("DashboardWindow", "txt_numdues"))
        self.label_8.setText(_translate("DashboardWindow", "RECENTLY COMPLETED"))
        self.txt_numservice.setText(_translate("DashboardWindow", "txt_numservice"))
        self.txt_numemp.setText(_translate("DashboardWindow", "txt_numemp"))
        self.Customers.setText(_translate("DashboardWindow", "CUSTOMERS"))
        self.label_9.setText(_translate("DashboardWindow", "SALES"))
        item = self.tbl_dashboard.horizontalHeaderItem(0)
        item.setText(_translate("DashboardWindow", "ID"))
        item = self.tbl_dashboard.horizontalHeaderItem(1)
        item.setText(_translate("DashboardWindow", "NAME"))
        item = self.tbl_dashboard.horizontalHeaderItem(2)
        item.setText(_translate("DashboardWindow", "SERVICE"))
        item = self.tbl_dashboard.horizontalHeaderItem(3)
        item.setText(_translate("DashboardWindow", "DATE COMPLETED"))
        self.btn_salesrep.setText(_translate("DashboardWindow", "SALES REPORT"))
        self.btn_books.setText(_translate("DashboardWindow", "BOOK"))
        self.btn_services.setText(_translate("DashboardWindow", "SERVICES"))
        self.btn_employees.setText(_translate("DashboardWindow", "EMPLOYEES"))
        self.btn_customer.setText(_translate("DashboardWindow", "CUSTOMER"))
        self.btn_invoice.setText(_translate("DashboardWindow", "INVOICE"))
        self.btn_dashboard.setText(_translate("DashboardWindow", "DASHBOARD"))
