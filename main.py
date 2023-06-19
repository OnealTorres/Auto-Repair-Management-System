import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox, QTableWidgetItem
from PyQt6 import uic
from datetime import date, timedelta
from PyQt6.QtCore import QRect, QDate

from chart import BarChart
import psycopg2
from psycopg2 import extras
import configparser


class AddBook(QWidget):
    def __init__(self):
        super().__init__()
        # Load the UI file
        self = uic.loadUi("ui/book_addbtn_pop_up.ui", self)
        self.setFixedSize(709, 490)
        self.setWindowTitle("Add Service")


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        # Create a ConfigParser object
        config = configparser.ConfigParser()

        # Read the config.ini file
        config.read('config.ini')

        self.conn = psycopg2.connect(
            host=config.get('conn', 'host'),
            port=config.get('conn', 'port'),
            database=config.get('conn', 'database'),
            user=config.get('conn', 'user'),
            password=config.get('conn', 'password')
        )
        # Load the first UI file
        self.load_login()

    def load_login(self):
        self.ui = uic.loadUi("ui/LoginForm.ui")
        self.setWindowTitle("Login")
        self.ui.btn_signin.clicked.connect(self.check_user)
        self.setCentralWidget(self.ui)
        self.setFixedSize(709, 490)
        self.emp_mname = ""

    def update_admin_info(self):
        cur = self.conn.cursor(cursor_factory=extras.RealDictCursor)
        cur.execute("SELECT * FROM SHOP")
        rows = cur.fetchone()

        self.admin_email = rows['shop_email']
        self.admin_password = rows['shop_password']
        self.shop_name = rows['shop_name']
        self.shop_address = rows['shop_address']
        self.shop_owner = rows['shop_owner']
        self.shop_mobile = rows['shop_mobile']
        self.shop_telephone = rows['shop_telephone']
        self.shop_socials = rows['shop_socials']

        cur.close()

    def get_attendant_info(self, email, password):
        cur = self.conn.cursor(cursor_factory=extras.RealDictCursor)
        cur.execute("SELECT * FROM EMPLOYEE WHERE emp_type = 'Attendant' AND emp_status='Active' AND emp_email = '" +
                    email+"' AND emp_password = '"+password+"'")
        rows = cur.fetchone()

        if (rows):
            self.emp_email = rows['emp_email']
            self.emp_password = rows['emp_password']
            self.attendant_name = rows['emp_lname']
            self.attendant_fullname = rows['emp_fname'] + \
                " "+rows['emp_mname']+" " + rows['emp_lname']
            self.attendant_mobile = rows['emp_mobile']
            self.attendant_address = rows['emp_address']
            return True
        else:
            return False

    def check_user(self):
        self.update_admin_info()

        if (self.ui.txt_email.text() == "" or self.ui.txt_password.text() == ""):
            QMessageBox.warning(
                self, "Message", "Please enter email and password!")

        elif (self.ui.txt_email.text() == self.admin_email and self.ui.txt_password.text() == self.admin_password):
            QMessageBox.information(self, "Message", "Welcome Admin!")
            self.login_admin_sucess()
        else:
            if (self.get_attendant_info(self.ui.txt_email.text(), self.ui.txt_password.text())):
                self.login_sucess()
            else:
                QMessageBox.information(
                    self, "Message", "Account does not exist!")

    def login_admin_sucess(self):
        self.on_admin_dashboard_clicked()

    def login_sucess(self):
        self.on_dashboard_clicked()

    # USED TO LOAD ALL ADMIN UI FILES
    def load_admin_ui_file(self, ui_file):
        # Load the UI file
        self.ui = uic.loadUi(ui_file)
        self.setFixedSize(1021, 560)

        # Set up button connections
        self.ui.btn_dashboard.clicked.connect(self.on_admin_dashboard_clicked)
        self.ui.btn_books.clicked.connect(self.on_admin_books_clicked)
        self.ui.btn_invoice.clicked.connect(self.on_admin_invoice_clicked)
        self.ui.btn_customer.clicked.connect(self.on_admin_customer_clicked)
        self.ui.btn_services.clicked.connect(self.on_admin_services_clicked)
        self.ui.btn_employees.clicked.connect(self.on_admin_employees_clicked)
        self.ui.btn_salesrep.clicked.connect(self.on_admin_salesrep_clicked)
        self.ui.btn_settings.clicked.connect(
            self.on_admin_settings_clicked)
        # Set the loaded UI as the central widget
        self.setCentralWidget(self.ui)

    def on_admin_dashboard_clicked(self):
        self.load_admin_ui_file("ui/admin_dashboard.ui")
        self.setWindowTitle("Dashboard")

        cur = self.conn.cursor(cursor_factory=extras.RealDictCursor)
        cur.execute(
            "SELECT COUNT(*) AS pending FROM BOOK WHERE book_status='Pending'")
        pending = cur.fetchone()

        if (pending):
            self.ui.txt_numpending.setText(str(pending['pending']))

        else:
            self.ui.txt_numpending.setText('0')

        cur = self.conn.cursor(cursor_factory=extras.RealDictCursor)
        cur.execute(
            "SELECT COUNT(*) AS customers FROM CUSTOMER WHERE cus_status='Active'")
        customers = cur.fetchone()

        if (customers):
            self.ui.txt_numcustomer.setText(str(customers['customers']))
        else:
            self.ui.txt_numcustomer.setText('0')

        cur = self.conn.cursor(cursor_factory=extras.RealDictCursor)
        cur.execute(
            "SELECT COUNT(*) AS employees FROM EMPLOYEE WHERE emp_status='Active'")
        employees = cur.fetchone()

        if (employees):
            self.ui.txt_numemp.setText(str(employees['employees']))
        else:
            self.ui.txt_numemp.setText('0')

        cur = self.conn.cursor(cursor_factory=extras.RealDictCursor)
        cur.execute(
            "SELECT COUNT(*) AS dues FROM BOOK WHERE book_status='Pending' AND book_end < CURRENT_DATE")
        dues = cur.fetchone()

        if (dues):
            self.ui.txt_numdues.setText(str(dues['dues']))
        else:
            self.ui.txt_numdues.setText('0')

        cur = self.conn.cursor(cursor_factory=extras.RealDictCursor)
        cur.execute("SELECT COUNT(*) AS sales FROM INVOICE")
        sales = cur.fetchone()

        if (sales):
            self.ui.txt_numsales.setText(str(sales['sales']))
        else:
            self.ui.txt_numsales.setText('0')

        cur = self.conn.cursor(cursor_factory=extras.RealDictCursor)
        cur.execute("SELECT COUNT(*) AS services FROM SERVICE")
        services = cur.fetchone()

        if (services):
            self.ui.txt_numservice.setText(str(services['services']))
        else:
            self.ui.txt_numservice.setText('0')

        cur = self.conn.cursor(cursor_factory=extras.RealDictCursor)
        cur.execute("SELECT inv_id, CONCAT(cus_fname,' ',cus_mname,' ',cus_lname),srv_name,DATE(INVOICE.date_created) AS date_finished" +
                    " FROM INVOICE INNER JOIN BOOK USING(book_id) INNER JOIN CUSTOMER USING(cus_id) INNER JOIN SERVICE USING(srv_id) ORDER BY(date_finished) LIMIT 10")
        rows = cur.fetchall()

        if rows:
            for row_idx, row_data in enumerate(rows):
                for col_idx, col_data in enumerate(row_data.values()):
                    item = QTableWidgetItem(str(col_data))
                    self.ui.tbl_dashboard.setItem(row_idx, col_idx, item)

        # Close the cursor
        cur.close()

    def on_admin_books_clicked(self):
        self.load_admin_ui_file("ui/admin_bookings.ui")
        self.setWindowTitle("Book")
        self.ui.btn_searchcus.clicked.connect(
            self.on_admin_book_btn_searchcus_clicked)
        self.ui.btn_searchbook.clicked.connect(
            self.on_admin_book_btn_searchbook_clicked)

        cur = self.conn.cursor(cursor_factory=extras.RealDictCursor)
        cur.execute(
            "SELECT book_id,book_type,book_status,book_total,book_vcl_plate,book_vcl_brand,book_vcl_model,CONCAT(emp_fname,' ',emp_mname,' ',emp_lname) AS employee_name,CONCAT(cus_fname,' ',cus_mname,' ',cus_lname) AS customer_name,srv_name,book_details,DATE(book_start) AS book_start,DATE(book_end) AS book_end,emp_id,cus_id,srv_id,DATE(BOOK.date_created) AS date_created" +
            " FROM BOOK INNER JOIN EMPLOYEE USING(emp_id) INNER JOIN CUSTOMER USING(cus_id) INNER JOIN SERVICE USING(srv_id) WHERE book_status != 'Finished' ORDER BY(date_created) DESC ")
        rows = cur.fetchall()

        if rows:
            for row_idx, row_data in enumerate(rows):
                for col_idx, col_data in enumerate(row_data.values()):
                    item = QTableWidgetItem(str(col_data))
                    self.ui.tbl_bookings.setItem(row_idx, col_idx, item)
        # Close the cursor
        cur.close()

    def on_admin_invoice_clicked(self):
        self.load_admin_ui_file("ui/admin_invoice.ui")
        self.setWindowTitle("Invoice")
        self.ui.search_btn.clicked.connect(
            self.on_admin_invoice_btn_searchcus_clicked)
        self.ui.search_btn_invoice.clicked.connect(
            self.on_admin_invoice_search_btn_invoice_clicked)

        cur = self.conn.cursor(cursor_factory=extras.RealDictCursor)
        cur.execute(
            "SELECT inv_id,book_type,book_status,book_total,book_vcl_plate,book_vcl_brand,book_vcl_model,CONCAT(emp_fname,' ',emp_mname,' ',emp_lname) AS employee_name,CONCAT(cus_fname,' ',cus_mname,' ',cus_lname) AS customer_name,srv_name,book_details,DATE(book_start) AS book_start,DATE(book_end) AS book_end,emp_id,cus_id,srv_id,book_id,DATE(BOOK.date_created) AS date_created,DATE(INVOICE.date_created) AS date_finished" +
            " FROM BOOK INNER JOIN EMPLOYEE USING(emp_id) INNER JOIN CUSTOMER USING(cus_id) INNER JOIN SERVICE USING(srv_id) INNER JOIN INVOICE USING(book_id) ORDER BY(date_finished) DESC")
        rows = cur.fetchall()

        if rows:
            for row_idx, row_data in enumerate(rows):
                for col_idx, col_data in enumerate(row_data.values()):
                    item = QTableWidgetItem(str(col_data))
                    self.ui.tbl_invoice.setItem(row_idx, col_idx, item)
        # Close the cursor
        cur.close()

    def on_admin_customer_clicked(self):
        self.load_admin_ui_file("ui/admin_customer.ui")
        self.setWindowTitle("Customer")
        self.ui.search_btn.clicked.connect(
            self.on_admin_customer_btn_searchcus_clicked)

        cur = self.conn.cursor(cursor_factory=extras.RealDictCursor)
        cur.execute(
            "SELECT cus_id, cus_fname, cus_mname, cus_lname,cus_mobile,cus_email,cus_sex,cus_address,cus_status,DATE(date_created) FROM CUSTOMER ORDER BY(date_created)")
        rows = cur.fetchall()

        if rows:
            for row_idx, row_data in enumerate(rows):
                for col_idx, col_data in enumerate(row_data.values()):
                    item = QTableWidgetItem(str(col_data))
                    self.ui.tbl_customer.setItem(row_idx, col_idx, item)
        # Close the cursor
        cur.close()

    def on_admin_settings_clicked(self):
        self.load_admin_ui_file("ui/admin_settings.ui")
        self.setWindowTitle("Settings")
        self.ui.btn_admin_update.clicked.connect(
            self.on_btn_admin_update_clicked)
        self.ui.btn_logout.clicked.connect(
            self.load_login)

        self.ui.txt_admin_comp.setText(self.shop_name)
        self.ui.txt_admin_name.setText(self.shop_owner)
        self.ui.txt_admin_contnum.setText(self.shop_mobile)
        self.ui.txt_admin_telnum.setText(self.shop_telephone)
        self.ui.txt_admin_address.setText(self.shop_address)
        self.ui.txt_admin_social.setText(self.shop_socials)
        self.ui.txt_show_email.setText(self.admin_email)
        self.ui.txt_admin_password.setText(self.admin_password)

    def on_admin_services_clicked(self):
        self.load_admin_ui_file("ui/admin_services.ui")
        self.srv_id = ""
        self.setWindowTitle("Services")
        self.ui.search_btn.clicked.connect(
            self.on_service_search_btn_clicked)
        self.ui.btn_service_add.clicked.connect(
            self.on_service_add_clicked)
        self.ui.btn_service_view.clicked.connect(
            self.on_service_view_clicked)

        cur = self.conn.cursor(cursor_factory=extras.RealDictCursor)
        cur.execute(
            "SELECT srv_category, srv_name, srv_time, srv_fee, srv_type FROM SERVICE ")
        rows = cur.fetchall()

        if rows:
            for row_idx, row_data in enumerate(rows):
                for col_idx, col_data in enumerate(row_data.values()):
                    item = QTableWidgetItem(str(col_data))
                    self.ui.tbl_services.setItem(row_idx, col_idx, item)
        # Close the cursor and the connection
        cur.close()

    def on_admin_employees_clicked(self):
        self.load_admin_ui_file("ui/admin_employees.ui")
        self.setWindowTitle("Employees")
        self.ui.search_btn.clicked.connect(
            self.on_employee_search_btn_clicked)
        self.ui.btn_employee_add.clicked.connect(
            self.on_employee_add_clicked)
        self.ui.btn_employee_view.clicked.connect(
            self.on_employee_view_clicked)

        self.emp_id = ""
        cur = self.conn.cursor(cursor_factory=extras.RealDictCursor)
        cur.execute(
            "SELECT emp_id, emp_fname, emp_mname, emp_lname,emp_type,emp_mobile,emp_email,emp_address,emp_sex,emp_dob,emp_status,emp_service FROM EMPLOYEE ORDER BY(date_created) DESC")
        rows = cur.fetchall()

        if rows:
            for row_idx, row_data in enumerate(rows):
                for col_idx, col_data in enumerate(row_data.values()):
                    item = QTableWidgetItem(str(col_data))
                    self.ui.tbl_employee.setItem(row_idx, col_idx, item)
        # Close the cursor and the connection
        cur.close()

    def on_admin_salesrep_clicked(self):
        self.load_admin_ui_file("ui/admin_sale_report.ui")
        self.setWindowTitle("Sales Report")
        self.ui.btn_sales.clicked.connect(
            self.on_btn_sales_clicked)
        self.ui.btn_revenue.clicked.connect(
            self.on_btn_revenue_clicked)

        self.current_year_idx = 0
        current_year = QDate.currentDate().year()
        for i in range(200):
            year = str(2000 + i)
            self.ui.drp_report_year.addItem(year)
            if year == str(current_year):
                self.current_year_idx = i
        self.ui.drp_report_year.setCurrentIndex(self.current_year_idx)

        cur = self.conn.cursor(cursor_factory=extras.RealDictCursor)
        cur.execute(
            "SELECT book_id, emp_fname,emp_mname,emp_lname,COUNT(*) AS completed, SUM(book_total) as earnings" +
            " FROM BOOK INNER JOIN EMPLOYEE USING(emp_id) WHERE book_status='Finished' GROUP BY(book_id, emp_fname,emp_mname,emp_lname) ORDER BY(earnings) DESC LIMIT 3;")
        rows = cur.fetchall()

        self.ui.tbl_top_mechanics.clearContents()

        if rows:
            for row_idx, row_data in enumerate(rows):
                for col_idx, col_data in enumerate(row_data.values()):
                    item = QTableWidgetItem(str(col_data))
                    self.ui.tbl_top_mechanics.setItem(row_idx, col_idx, item)
        # Close the cursor
        cur.close()

        cur = self.conn.cursor(cursor_factory=extras.RealDictCursor)
        cur.execute(
            "SELECT book_id,cus_fname,cus_mname,cus_lname,COUNT(*) AS completed, SUM(book_total) as payment" +
            " FROM BOOK INNER JOIN CUSTOMER USING(cus_id) WHERE book_status='Finished' GROUP BY(book_id,cus_fname,cus_mname,cus_lname) ORDER BY(payment) DESC LIMIT 3;")
        rows = cur.fetchall()

        self.ui.tbl_top_customers.clearContents()

        if rows:
            for row_idx, row_data in enumerate(rows):
                for col_idx, col_data in enumerate(row_data.values()):
                    item = QTableWidgetItem(str(col_data))
                    self.ui.tbl_top_customers.setItem(row_idx, col_idx, item)
        # Close the cursor
        cur.close()

    # ADMIN UPDATE

    def on_btn_admin_update_clicked(self):

        if (self.ui.txt_admin_comp.text() == "" or self.ui.txt_admin_name.text() == "" or self.ui.txt_admin_contnum.text() == "" or self.ui.txt_admin_telnum.text() == "" or self.ui.txt_admin_address.text() == "" or self.ui.txt_admin_social.text() == "" or self.ui.txt_show_email.text() == "" or self.ui.txt_admin_password.text() == ""):
            QMessageBox.information(
                self, "Message", "Please fill out all of the fields!")
        else:
            cur = self.conn.cursor(cursor_factory=extras.RealDictCursor)
            cur.execute("UPDATE SHOP SET shop_name='" + self.ui.txt_admin_comp.text() +
                        "', shop_owner='" + self.ui.txt_admin_name.text() +
                        "', shop_mobile='" + self.ui.txt_admin_contnum.text() +
                        "', shop_telephone='" + self.ui.txt_admin_telnum.text() +
                        "', shop_address='" + self.ui.txt_admin_address.text() +
                        "', shop_socials='" + self.ui.txt_admin_social.text() +
                        "', shop_email='" + self.ui.txt_show_email.text() +
                        "', shop_password='" + self.ui.txt_admin_password.text()+"';")

            # Commit the changes to the database
            self.conn.commit()

            # Close the cursor
            cur.close()
            QMessageBox.information(self, "Message", "Shop Details Updated!")
            cur = self.conn.cursor(cursor_factory=extras.RealDictCursor)

            cur.execute("SELECT * FROM SHOP")
            rows = cur.fetchone()

            self.admin_email = rows['shop_email']
            self.admin_password = rows['shop_password']
            self.shop_name = rows['shop_name']
            self.shop_address = rows['shop_address']
            self.shop_owner = rows['shop_owner']
            self.shop_mobile = rows['shop_mobile']
            self.shop_telephone = rows['shop_telephone']
            self.shop_socials = rows['shop_socials']

            cur.close()
            self.on_admin_settings_clicked()

    # BOOK_PAGE BUTTONS
    # book search

    def on_admin_book_btn_searchcus_clicked(self):
        if (self.ui.txt_customerid.text() and self.is_numeric(self.ui.txt_customerid.text())):

            cur = self.conn.cursor(cursor_factory=extras.RealDictCursor)
            cur.execute(
                "SELECT book_id,book_type,book_status,book_total,book_vcl_plate,book_vcl_brand,book_vcl_model,CONCAT(emp_fname,' ',emp_mname,' ',emp_lname) AS employee_name,CONCAT(cus_fname,' ',cus_mname,' ',cus_lname) AS customer_name,srv_name,book_details,DATE(book_start) AS book_start,DATE(book_end) AS book_end,emp_id,cus_id,srv_id,DATE(BOOK.date_created) AS date_created" +
                " FROM BOOK INNER JOIN EMPLOYEE USING(emp_id) INNER JOIN CUSTOMER USING(cus_id) INNER JOIN SERVICE USING(srv_id) WHERE book_status != 'Finished' AND cus_id="+self.ui.txt_customerid.text()+" ORDER BY(date_created) DESC")
            rows = cur.fetchall()

            self.ui.tbl_bookings.clearContents()

            if rows:
                QMessageBox.information(self, "Message", "Booking Found!")
                for row_idx, row_data in enumerate(rows):
                    for col_idx, col_data in enumerate(row_data.values()):
                        item = QTableWidgetItem(str(col_data))
                        self.ui.tbl_bookings.setItem(row_idx, col_idx, item)
            else:
                QMessageBox.warning(self, "Warning", "Booking Not Found!")
            # Close the cursor
            cur.close()

        else:
            self.on_admin_books_clicked()

    def on_admin_book_btn_searchbook_clicked(self):
        if (self.ui.txt_bookid.text() and self.is_numeric(self.ui.txt_bookid.text())):
            cur = self.conn.cursor(cursor_factory=extras.RealDictCursor)
            cur.execute(
                "SELECT book_id,book_type,book_status,book_total,book_vcl_plate,book_vcl_brand,book_vcl_model,CONCAT(emp_fname,' ',emp_mname,' ',emp_lname) AS employee_name,CONCAT(cus_fname,' ',cus_mname,' ',cus_lname) AS customer_name,srv_name,book_details,DATE(book_start) AS book_start,DATE(book_end) AS book_end,emp_id,cus_id,srv_id,DATE(BOOK.date_created) AS date_created" +
                " FROM BOOK INNER JOIN EMPLOYEE USING(emp_id) INNER JOIN CUSTOMER USING(cus_id) INNER JOIN SERVICE USING(srv_id) WHERE book_status != 'Finished' AND book_id="+self.ui.txt_bookid.text()+"")
            row = cur.fetchone()

            self.ui.tbl_bookings.clearContents()

            if row:
                row_idx = 0
                for col_idx, col_data in enumerate(row.values()):
                    item = QTableWidgetItem(str(col_data))
                    self.ui.tbl_bookings.setItem(row_idx, col_idx, item)
                QMessageBox.information(self, "Message", "Booking Found!")

                self.book_id = row['book_id']
                self.book_type = row['book_type']
                self.book_status = row['book_status']
                self.book_total = row['book_total']
                self.book_vcl_plate = row['book_vcl_plate']
                self.book_vcl_brand = row['book_vcl_brand']
                self.book_vcl_model = row['book_vcl_model']
                self.book_details = row['book_details']
                self.book_start = row['book_start']
                self.book_end = row['book_end']
                self.customer_name = row['customer_name']
                self.srv_name = row['srv_name']
                self.emp_id = row['emp_id']
                self.cus_id = row['cus_id']
                self.srv_id = row['srv_id']
                self.date_created = row['date_created']

            else:
                QMessageBox.warning(self, "Warning", "Booking Not Found!")
            # Close the cursor
            cur.close()
        else:
            self.on_admin_books_clicked()

    # INVOICE BUTTONS
    # invoice search
    def on_admin_invoice_btn_searchcus_clicked(self):
        if (self.ui.txt_cusid.text() and self.is_numeric(self.ui.txt_cusid.text())):
            self.inv_id = ""
            cur = self.conn.cursor(cursor_factory=extras.RealDictCursor)
            cur.execute(
                "SELECT inv_id,book_type,book_status,book_total,book_vcl_plate,book_vcl_brand,book_vcl_model,CONCAT(emp_fname,' ',emp_mname,' ',emp_lname) AS employee_name,CONCAT(cus_fname,' ',cus_mname,' ',cus_lname) AS customer_name,srv_name,book_details,DATE(book_start) AS book_start,DATE(book_end) AS book_end,emp_id,cus_id,srv_id,book_id,DATE(BOOK.date_created) AS date_created,DATE(INVOICE.date_created) AS date_finished" +
                " FROM BOOK INNER JOIN EMPLOYEE USING(emp_id) INNER JOIN CUSTOMER USING(cus_id) INNER JOIN SERVICE USING(srv_id) INNER JOIN INVOICE USING(book_id) WHERE cus_id="+self.ui.txt_cusid.text()+" ORDER BY(date_finished) DESC")
            rows = cur.fetchall()

            self.ui.tbl_invoice.clearContents()

            if rows:
                for row_idx, row_data in enumerate(rows):
                    for col_idx, col_data in enumerate(row_data.values()):
                        item = QTableWidgetItem(str(col_data))
                        self.ui.tbl_invoice.setItem(row_idx, col_idx, item)
                QMessageBox.information(self, "Message", "Customer Found!")
            else:
                QMessageBox.information(self, "Message", "Customer Not Found!")
                self.on_admin_invoice_clicked()
            # Close the cursor
            cur.close()

    def on_admin_invoice_search_btn_invoice_clicked(self):
        if (self.ui.txt_invoiceid.text() and self.is_numeric(self.ui.txt_invoiceid.text())):
            cur = self.conn.cursor(cursor_factory=extras.RealDictCursor)
            cur.execute(
                "SELECT inv_id,book_type,book_status,book_total,book_vcl_plate,book_vcl_brand,book_vcl_model,CONCAT(emp_fname,' ',emp_mname,' ',emp_lname) AS employee_name,CONCAT(cus_fname,' ',cus_mname,' ',cus_lname) AS customer_name,srv_name,book_details,DATE(book_start) AS book_start,DATE(book_end) AS book_end,emp_id,cus_id,srv_id,book_id,DATE(BOOK.date_created) AS date_created,DATE(INVOICE.date_created) AS date_finished" +
                " FROM BOOK INNER JOIN EMPLOYEE USING(emp_id) INNER JOIN CUSTOMER USING(cus_id) INNER JOIN SERVICE USING(srv_id) INNER JOIN INVOICE USING(book_id) WHERE inv_id="+self.ui.txt_invoiceid.text()+"")
            row = cur.fetchone()

            self.ui.tbl_invoice.clearContents()

            if row:
                row_idx = 0
                for col_idx, col_data in enumerate(row.values()):
                    item = QTableWidgetItem(str(col_data))
                    self.ui.tbl_invoice.setItem(row_idx, col_idx, item)
                QMessageBox.information(self, "Message", "Invoice Found!")
            else:
                QMessageBox.warning(self, "Warning", "Invoice Not Found!")
                self.on_admin_invoice_clicked()
            # Close the cursor
            cur.close()

    # CUSTOMERS BUTTONS
    # customer search
    def on_admin_customer_btn_searchcus_clicked(self):
        if (self.ui.txt_customerfname.text() == "" or self.ui.txt_customerlname.text() == ""):
            self.on_admin_customer_clicked()
        else:
            add_email_query = ''
            if (self.ui.txt_email.text()):
                add_email_query = " AND cus_email='"+self.ui.txt_email.text()+"' "

            cur = self.conn.cursor(cursor_factory=extras.RealDictCursor)
            cur.execute(
                "SELECT cus_id, cus_fname, cus_mname, cus_lname,cus_mobile,cus_email,cus_sex,cus_address,cus_status,DATE(date_created) AS date_created FROM CUSTOMER WHERE cus_fname='"+self.ui.txt_customerfname.text()+"' AND cus_mname='"+self.ui.txt_customermname.text()+"' AND cus_lname='"+self.ui.txt_customerlname.text()+"' "+add_email_query)
            row = cur.fetchone()
            if row:

                self.cus_id = row['cus_id']
                self.cus_fname = row['cus_fname']
                self.cus_mname = row['cus_mname']
                self.cus_lname = row['cus_lname']
                self.cus_mobile = row['cus_mobile']
                self.cus_email = row['cus_email']
                self.cus_sex = row['cus_sex']
                self.cus_address = row['cus_address']
                self.cus_status = row['cus_status']
                self.date_created = row['date_created']

                self.ui.tbl_customer.clearContents()
                if row:
                    row_idx = 0
                    for col_idx, col_data in enumerate(row.values()):
                        item = QTableWidgetItem(str(col_data))
                        self.ui.tbl_customer.setItem(row_idx, col_idx, item)

                QMessageBox.information(self, "Message", "Customer Found!")

            else:
                QMessageBox.information(self, "Message", "Customer Not Found!")
                self.on_admin_customer_clicked()
            # Close the cursor
            cur.close()

    # SERVICES BUTTONS
    # service search
    def on_service_search_btn_clicked(self):

        if (self.ui.txt_service.text() != ""):

            cur = self.conn.cursor(cursor_factory=extras.RealDictCursor)
            cur.execute(
                "SELECT srv_id,srv_category,srv_name,srv_time,srv_fee,srv_type FROM SERVICE WHERE srv_name = '"+self.ui.txt_service.text()+"'")
            row = cur.fetchone()

            if row:

                self.srv_id = row['srv_id']
                self.srv_category = row['srv_category']
                self.srv_name = row['srv_name']
                self.srv_time = row['srv_time']
                self.srv_fee = row['srv_fee']
                self.srv_type = row['srv_type']

                self.ui.tbl_services.clearContents()
                row_idx = 0
                for col_idx, col_data in enumerate(row.values()):
                    if (col_idx == 0):
                        continue
                    else:
                        item = QTableWidgetItem(str(col_data))
                        self.ui.tbl_services.setItem(row_idx, col_idx-1, item)
                QMessageBox.information(self, "Message", "Service Found!")

            else:
                QMessageBox.information(self, "Message", "Service Not Found!")

            # Close the cursor
            cur.close()
        else:
            self.srv_id = ""
            self.on_admin_services_clicked()

    # service add
    def on_service_add_clicked(self):
        self.load_admin_ui_file("ui/admin_add_service.ui")
        self.ui.btn_add_service.clicked.connect(
            self.on_add_service_clicked)
        self.ui.btn_cancel_service.clicked.connect(
            self.on_admin_services_clicked)

    def on_add_service_clicked(self):
        # drp_service_category
        # txt_service
        # txt_timeallotment
        # txt_service_fee
        # drp_addvehicle_type
        if (self.ui.txt_service.text() == ""):
            QMessageBox.information(
                self, "Message", "Please enter service name!")
        elif (self.ui.txt_timeallotment.text() == "" or not self.ui.txt_timeallotment.text().isdigit()):
            QMessageBox.information(
                self, "Message", "Please enter the number of days!")
        elif (self.ui.txt_service_fee.text() == "" or not self.is_numeric(self.ui.txt_service_fee.text())):
            QMessageBox.information(
                self, "Message", "Please enter the service fee!")
        else:
            cur = self.conn.cursor(cursor_factory=extras.RealDictCursor)
            cur.execute("INSERT INTO SERVICE (srv_category,srv_name,srv_time,srv_fee,srv_type)VALUES('"+self.ui.drp_service_category.currentText()+"','" +
                        self.ui.txt_service.text()+"','"+self.ui.txt_timeallotment.text()+"',"+self.ui.txt_service_fee.text()+",'"+self.ui.drp_addvehicle_type.currentText()+"');")
            # Commit the changes to the database
            self.conn.commit()

            # Close the cursor
            cur.close()
            QMessageBox.information(self, "Message", "Service Added!")
            self.on_admin_services_clicked()

    # service view
    def on_service_view_clicked(self):
        if (self.srv_id and self.is_numeric(self.srv_id)):
            self.load_admin_ui_file("ui/admin_update_service.ui")
            self.ui.btn_update_service.clicked.connect(
                self.on_update_service_clicked)
            self.ui.btn_delete.clicked.connect(
                self.on_delete_service_clicked)
            self.ui.btn_updateser_cancel.clicked.connect(
                self.on_admin_services_clicked)
            service_category_list = ['Vehicle Repair', 'Vehicle Maintenance', 'Diagnostic Services',
                                     'Body and Paint Services', 'Tire Services', 'Auto Detailing', 'Air Conditioning Services']
            service_vehicle_type_list = [
                '2 Wheeler', '3 Wheeler', '4 Wheeler', '6 Wheeler', '8 Wheeler']

            for i in range(len(service_category_list)):
                if (self.srv_category == service_category_list[i]):
                    self.ui.drp_update_service_category.setCurrentIndex(i)
                    break

            for i in range(len(service_vehicle_type_list)):
                if (self.srv_type == service_vehicle_type_list[i]):
                    self.ui.drp_update_vehicle_type.setCurrentIndex(i)
                    break

            self.ui.txt_update_service.setText(self.srv_name)
            self.ui.txt_update_timeallotment.setText(self.srv_time)
            self.ui.txt_update_service_fee.setText(str(self.srv_fee))

    def on_update_service_clicked(self):
        if (self.ui.txt_update_service.text() == ""):
            QMessageBox.information(
                self, "Message", "Please enter service name!")
        elif (self.ui.txt_update_timeallotment.text() == "" or not self.ui.txt_update_timeallotment.text().isdigit()):
            QMessageBox.information(
                self, "Message", "Please enter the number of days!")
        elif (self.ui.txt_update_service_fee.text() == "" or not self.is_numeric(self.ui.txt_update_service_fee.text())):
            QMessageBox.information(
                self, "Message", "Please enter the service fee!")
        else:
            cur = self.conn.cursor(cursor_factory=extras.RealDictCursor)
            cur.execute("UPDATE SERVICE SET srv_category='" + self.ui.drp_update_service_category.currentText() +
                        "', srv_name='" + self.ui.txt_update_service.text() +
                        "', srv_time='" + str(self.ui.txt_update_timeallotment.text()) +
                        "', srv_fee=" + str(self.ui.txt_update_service_fee.text()) +
                        ", srv_type='" + self.ui.drp_update_vehicle_type.currentText() +
                        "' WHERE srv_id=" + str(self.srv_id) + ";")

            # Commit the changes to the database
            self.conn.commit()

            # Close the cursor
            cur.close()
            QMessageBox.information(self, "Message", "Service Updated!")
            self.srv_id = ""
            self.on_admin_services_clicked()

    def on_delete_service_clicked(self):
        cur = self.conn.cursor(cursor_factory=extras.RealDictCursor)
        cur.execute("DELETE FROM SERVICE WHERE srv_id="+str(self.srv_id))

        # Close the cursor
        cur.close()
        QMessageBox.information(self, "Message", "Service Deleted!")
        self.on_admin_services_clicked()

    # EMPLOYEES BUTTONS
    # employees search
    def on_employee_search_btn_clicked(self):
        if (self.ui.txt_empfname.text() == "" or self.ui.txt_emplname.text() == ""):
            self.on_admin_employees_clicked()
        else:
            add_email_query = ''
            if (self.ui.txt_email.text()):
                add_email_query = " AND emp_email='"+self.ui.txt_email.text()+"' "

            cur = self.conn.cursor(cursor_factory=extras.RealDictCursor)
            cur.execute(
                "SELECT emp_id,emp_fname,emp_mname, emp_lname,emp_type,emp_mobile,emp_email,emp_password,emp_address,emp_sex,emp_dob,emp_status,emp_service FROM EMPLOYEE WHERE emp_fname='"+self.ui.txt_empfname.text()+"' AND emp_mname='"+self.ui.txt_empmname.text()+"' AND emp_lname='"+self.ui.txt_emplname.text()+"' "+add_email_query)
            row = cur.fetchone()
            if row:

                self.emp_id = row['emp_id']
                self.emp_fname = row['emp_fname']
                self.emp_mname = row['emp_mname']
                self.emp_lname = row['emp_lname']
                self.emp_type = row['emp_type']
                self.emp_mobile = row['emp_mobile']
                self.emp_email = row['emp_email']
                self.emp_password = row['emp_password']
                self.emp_address = row['emp_address']
                self.emp_sex = row['emp_sex']
                self.emp_dob = row['emp_dob']
                self.emp_status = row['emp_status']
                self.emp_service = row['emp_service']

                columns_to_display = ['emp_id', 'emp_fname', 'emp_mname', 'emp_lname', 'emp_type',
                                      'emp_mobile', 'emp_email', 'emp_address', 'emp_sex', 'emp_dob', 'emp_status', 'emp_service']
                column_indices = [idx for idx, col_name in enumerate(
                    columns_to_display) if col_name != 'emp_password']
                self.ui.tbl_employee.clearContents()
                if row:
                    for col_idx, col_name in enumerate(columns_to_display):
                        if col_name != 'emp_password':
                            col_data = row[col_name]
                            item = QTableWidgetItem(str(col_data))
                            self.ui.tbl_employee.setItem(
                                0, column_indices.index(col_idx), item)
                QMessageBox.information(self, "Message", "Employee Found!")

            else:
                QMessageBox.information(self, "Message", "Employee Not Found!")

            # Close the cursor
            cur.close()

    # employee add
    def on_employee_add_clicked(self):
        self.load_admin_ui_file("ui/admin_add_employee.ui")
        self.ui.btn_add_employee.clicked.connect(
            self.on_add_employee_clicked)
        self.ui.btn_cancel_employee.clicked.connect(
            self.on_admin_employees_clicked)

    def on_add_employee_clicked(self):

        if (self.ui.txt_firstname.text() == "" or self.ui.txt_lastname.text() == ""):
            QMessageBox.information(
                self, "Message", "Please enter the full name!")
        elif (self.ui.txt_emp_email.text() == ""):
            QMessageBox.information(
                self, "Message", "Please enter the email!")
        elif (self.ui.txt_emp_houseadd.toPlainText() == ""):
            QMessageBox.information(
                self, "Message", "Please enter the address!")
        elif (self.ui.drp_emp_type.currentText() == "Attendant" and self.ui.txt_add_emp_password.text() == ""):
            QMessageBox.information(
                self, "Message", "Please enter the password!")
        elif (self.ui.txt_add_emp_contactnum.text() == "" or not self.is_mobile(self.ui.txt_add_emp_contactnum.text())):
            QMessageBox.information(
                self, "Message", "Please enter the mobile number!")
        else:
            cur = self.conn.cursor(cursor_factory=extras.RealDictCursor)
            cur.execute(
                "INSERT INTO EMPLOYEE (emp_fname, emp_mname, emp_lname, emp_sex, emp_dob, emp_email, emp_password, emp_address, emp_mobile, emp_type, emp_service) "
                "VALUES ('" + self.ui.txt_firstname.text() +
                "', '" + self.ui.txt_middlename.text() +
                "', '" + self.ui.txt_lastname.text() +
                "', '" + self.ui.drp_employee_sex.currentText() +
                "', '" + self.ui.date_dob_emp.text() +
                "', '" + self.ui.txt_emp_email.text() +
                "', '" + self.ui.txt_add_emp_password.text() +
                "', '" + self.ui.txt_emp_houseadd.toPlainText() +
                "', '" + str(self.ui.txt_add_emp_contactnum.text()) +
                "', '" + self.ui.drp_emp_type.currentText() +
                "', '" + self.ui.drp_service_cat.currentText() + "');")

            # Commit the changes to the database
            self.conn.commit()

            # Close the cursor
            cur.close()
            QMessageBox.information(self, "Message", "Employee Added!")
            self.on_admin_employees_clicked()

    # employee view

    def on_employee_view_clicked(self):
        if (self.emp_id):
            self.load_admin_ui_file("ui/admin_update_employees.ui")
            self.ui.btn_update_emp.clicked.connect(
                self.on_update_employee_clicked)
            self.ui.btn_cancel_emp.clicked.connect(
                self.on_admin_employees_clicked)

            employee_sex_list = ['Male', 'Female']
            employee_status_list = ['Active', 'Disabled']
            employee_type_list = ['Attendant', 'Mechanic',
                                  'Painter', 'Detailer', 'AC Technician']
            service_category_list = ['Attendant', 'Vehicle Repair', 'Vehicle Maintenance', 'Diagnostic Services',
                                     'Body and Paint Services', 'Tire Services', 'Auto Detailing', 'Air Conditioning Services']

            self.ui.txt_firstname.setText(self.emp_fname)
            self.ui.txt_middlename.setText(self.emp_mname)
            self.ui.txt_lastname.setText(self.emp_lname)
            self.ui.date_dob_emp.setDate(self.emp_dob)
            self.ui.txt_emp_email.setText(self.emp_email)
            self.ui.txt_add_emp_password.setText(self.emp_password)
            self.ui.txt_emp_houseadd.setPlainText(self.emp_address)
            self.ui.txt_add_emp_contactnum.setText(self.emp_mobile)

            for i in range(len(employee_sex_list)):
                if (self.emp_sex == employee_sex_list[i]):
                    self.ui.drp_employee_sex.setCurrentIndex(i)
                    break

            for i in range(len(employee_status_list)):
                if (self.emp_status == employee_status_list[i]):
                    self.ui.drp_emp_status.setCurrentIndex(i)
                    break

            for i in range(len(employee_type_list)):
                if (self.emp_type == employee_type_list[i]):
                    self.ui.drp_emp_type.setCurrentIndex(i)
                    break
            for i in range(len(service_category_list)):
                if (self.emp_service == service_category_list[i]):
                    self.ui.drp_service_cat.setCurrentIndex(i)
                    break

    def on_update_employee_clicked(self):
        if (self.ui.txt_firstname.text() == "" or self.ui.txt_lastname.text() == ""):
            QMessageBox.information(
                self, "Message", "Please enter the full name!")
        elif (self.ui.txt_emp_email.text() == ""):
            QMessageBox.information(
                self, "Message", "Please enter the email!")
        elif (self.ui.txt_emp_houseadd.toPlainText() == ""):
            QMessageBox.information(
                self, "Message", "Please enter the address!")
        elif (self.ui.drp_emp_type.currentText() == "Attendant" and self.ui.txt_add_emp_password.text() == ""):
            QMessageBox.information(
                self, "Message", "Please enter the password!")
        elif (self.ui.txt_add_emp_contactnum.text() == "" or not self.is_mobile(self.ui.txt_add_emp_contactnum.text())):
            QMessageBox.information(
                self, "Message", "Please enter the mobile number!")
        else:
            cur = self.conn.cursor(cursor_factory=extras.RealDictCursor)
            cur.execute("UPDATE EMPLOYEE SET emp_fname='" + self.ui.txt_firstname.text() +
                        "', emp_mname='" + self.ui.txt_middlename.text() +
                        "', emp_lname='" + self.ui.txt_lastname.text() +
                        "', emp_type='" + self.ui.drp_emp_type.currentText() +
                        "', emp_mobile='" + self.ui.txt_add_emp_contactnum.text() +
                        "', emp_email='" + self.ui.txt_emp_email.text() +
                        "', emp_password='" + self.ui.txt_add_emp_password.text() +
                        "', emp_address='" + self.ui.txt_emp_houseadd.toPlainText() +
                        "', emp_sex='" + self.ui.drp_employee_sex.currentText() +
                        "', emp_dob='" + self.ui.date_dob_emp.text() +
                        "', emp_status='" + self.ui.drp_emp_status.currentText() +
                        "', emp_service='" + self.ui.drp_service_cat.currentText() +
                        "' WHERE emp_id=" + str(self.emp_id) + ";")

            # Commit the changes to the database
            self.conn.commit()

            # Close the cursor
            cur.close()
            QMessageBox.information(self, "Message", "Employee Updated!")
            self.on_admin_employees_clicked()

    # SALES REPORT BUTTONS
    # sales button

    def on_btn_sales_clicked(self):

        sales_months = []
        for i in range(1, 13):
            cur = self.conn.cursor(cursor_factory=extras.RealDictCursor)
            cur.execute(
                "SELECT COUNT(*) AS sales FROM BOOK INNER JOIN INVOICE USING(book_id) WHERE book_status='Finished' AND EXTRACT(YEAR FROM INVOICE.date_created)="+self.ui.drp_report_year.currentText()+" AND EXTRACT(MONTH FROM INVOICE.date_created)="+str(i)+" ")
            sales = cur.fetchone()
            if (sales):
                sales_months.append(sales['sales'])
            else:
                sales_months.append(0)
        for i in range(len(sales_months)):
            print(sales_months[i])

        self.new_window = BarChart(
            sales_months, "Sales")
        self.new_window.show()

    # revenue button
    def on_btn_revenue_clicked(self):

        sales_months = []
        for i in range(1, 13):
            cur = self.conn.cursor(cursor_factory=extras.RealDictCursor)
            cur.execute(
                "SELECT SUM(book_total) AS revenue FROM BOOK INNER JOIN INVOICE USING(book_id) WHERE book_status='Finished' AND EXTRACT(YEAR FROM INVOICE.date_created)="+self.ui.drp_report_year.currentText()+" AND EXTRACT(MONTH FROM INVOICE.date_created)="+str(i)+" ")
            revenue = cur.fetchone()
            if (revenue['revenue']):
                sales_months.append(int(revenue['revenue']))
            else:
                sales_months.append(0)
        for i in range(len(sales_months)):
            print(sales_months[i])
        self.new_window = BarChart(
            sales_months, "Revenue")
        self.new_window.show()

    # USED TO LOAD ALL USER UI FILES

    def load_ui_file(self, ui_file):
        # Load the UI file
        self.ui = uic.loadUi(ui_file)
        self.setFixedSize(1021, 560)

        # Set up attendant name
        self.ui.attendant_name.setText(self.attendant_name)

        # Set up button connections
        self.ui.btn_dashboard.clicked.connect(self.on_dashboard_clicked)
        self.ui.btn_books.clicked.connect(self.on_books_clicked)
        self.ui.btn_invoice.clicked.connect(self.on_invoice_clicked)
        self.ui.btn_customer.clicked.connect(self.on_customer_clicked)
        self.ui.btn_settings.clicked.connect(self.on_btn_settings_clicked)
        # Set the loaded UI as the central widget
        self.setCentralWidget(self.ui)

    def on_dashboard_clicked(self):
        self.load_ui_file("ui/dashboard.ui")
        self.setWindowTitle("Dashboard")

        cur = self.conn.cursor(cursor_factory=extras.RealDictCursor)
        cur.execute(
            "SELECT COUNT(*) AS pending FROM BOOK WHERE book_status='Pending'")
        pending = cur.fetchone()

        if (pending):

            self.ui.txt_numpending.setText(str(pending['pending']))
        else:
            self.ui.txt_numpending.setText('0')

        cur = self.conn.cursor(cursor_factory=extras.RealDictCursor)
        cur.execute(
            "SELECT COUNT(*) AS customers FROM CUSTOMER WHERE cus_status='Active'")
        customers = cur.fetchone()

        if (customers):
            self.ui.txt_numcustomer.setText(str(customers['customers']))
        else:
            self.ui.txt_numcustomer.setText('0')

        cur = self.conn.cursor(cursor_factory=extras.RealDictCursor)
        cur.execute(
            "SELECT COUNT(*) AS employees FROM EMPLOYEE WHERE emp_status='Active'")
        employees = cur.fetchone()

        if (employees):
            self.ui.txt_numemp.setText(str(employees['employees']))
        else:
            self.ui.txt_numemp.setText('0')

        cur = self.conn.cursor(cursor_factory=extras.RealDictCursor)
        cur.execute(
            "SELECT COUNT(*) AS dues FROM BOOK WHERE book_status='Pending' AND book_end < CURRENT_DATE")
        dues = cur.fetchone()

        if (dues):
            self.ui.txt_numdues.setText(str(dues['dues']))
        else:
            self.ui.txt_numdues.setText('0')

        cur = self.conn.cursor(cursor_factory=extras.RealDictCursor)
        cur.execute("SELECT COUNT(*) AS sales FROM INVOICE")
        sales = cur.fetchone()

        if (sales):
            self.ui.txt_numsales.setText(str(sales['sales']))
        else:
            self.ui.txt_numsales.setText('0')

        cur = self.conn.cursor(cursor_factory=extras.RealDictCursor)
        cur.execute("SELECT COUNT(*) AS services FROM SERVICE")
        services = cur.fetchone()

        if (services):
            self.ui.txt_numservice.setText(str(services['services']))
        else:
            self.ui.txt_numservice.setText('0')

        cur = self.conn.cursor(cursor_factory=extras.RealDictCursor)
        cur.execute("SELECT inv_id, CONCAT(cus_fname,' ',cus_mname,' ',cus_lname),srv_name,DATE(INVOICE.date_created) AS date_finished" +
                    " FROM INVOICE INNER JOIN BOOK USING(book_id) INNER JOIN CUSTOMER USING(cus_id) INNER JOIN SERVICE USING(srv_id) ORDER BY(date_finished) LIMIT 10")
        rows = cur.fetchall()

        if rows:
            for row_idx, row_data in enumerate(rows):
                for col_idx, col_data in enumerate(row_data.values()):
                    item = QTableWidgetItem(str(col_data))
                    self.ui.tbl_dashboard.setItem(row_idx, col_idx, item)

        # Close the cursor
        cur.close()

    def on_books_clicked(self):
        self.load_ui_file("ui/Book.ui")
        self.setWindowTitle("Book")
        self.ui.btn_book.clicked.connect(self.on_book_page_clicked)
        self.ui.btn_bookings.clicked.connect(self.on_bookings_page_clicked)

    def on_invoice_clicked(self):
        self.load_ui_file("ui/invoice_page.ui")
        self.setWindowTitle("Invoice")
        self.ui.btn_invoice_view.clicked.connect(
            self.on_btn_invoice_view_clicked)
        self.ui.search_btn.clicked.connect(
            self.on_invoice_search_btn_clicked)
        self.ui.search_btn_invoice.clicked.connect(
            self.on_invoice_search_btn_invoice_clicked)

        self.inv_id = ""
        cur = self.conn.cursor(cursor_factory=extras.RealDictCursor)
        cur.execute(
            "SELECT inv_id,book_type,book_status,book_total,book_vcl_plate,book_vcl_brand,book_vcl_model,CONCAT(emp_fname,' ',emp_mname,' ',emp_lname) AS employee_name,CONCAT(cus_fname,' ',cus_mname,' ',cus_lname) AS customer_name,srv_name,book_details,DATE(book_start) AS book_start,DATE(book_end) AS book_end,emp_id,cus_id,srv_id,book_id,DATE(BOOK.date_created) AS date_created,DATE(INVOICE.date_created) AS date_finished" +
            " FROM BOOK INNER JOIN EMPLOYEE USING(emp_id) INNER JOIN CUSTOMER USING(cus_id) INNER JOIN SERVICE USING(srv_id) INNER JOIN INVOICE USING(book_id) ORDER BY(date_finished) DESC")
        rows = cur.fetchall()

        if rows:
            for row_idx, row_data in enumerate(rows):
                for col_idx, col_data in enumerate(row_data.values()):
                    item = QTableWidgetItem(str(col_data))
                    self.ui.tbl_invoice.setItem(row_idx, col_idx, item)
        # Close the cursor
        cur.close()

    def on_customer_clicked(self):
        self.load_ui_file("ui/customer_page.ui")
        self.setWindowTitle("Customer")
        self.ui.search_btn.clicked.connect(
            self.on_customer_search_btn_clicked)
        self.ui.btn_customer_add.clicked.connect(
            self.on_customer_add_clicked)
        self.ui.btn_customer_view.clicked.connect(
            self.on_customer_view_clicked)

        self.cus_id = ""
        cur = self.conn.cursor(cursor_factory=extras.RealDictCursor)
        cur.execute(
            "SELECT cus_id, cus_fname, cus_mname, cus_lname,cus_mobile,cus_email,cus_sex,cus_address,cus_status,DATE(date_created) FROM CUSTOMER ORDER BY(date_created)")
        rows = cur.fetchall()

        if rows:
            for row_idx, row_data in enumerate(rows):
                for col_idx, col_data in enumerate(row_data.values()):
                    item = QTableWidgetItem(str(col_data))
                    self.ui.tbl_customer.setItem(row_idx, col_idx, item)
        # Close the cursor
        cur.close()

    def on_btn_settings_clicked(self):
        self.load_ui_file("ui/attendant_settings.ui")
        self.setWindowTitle("Settings")
        self.ui.btn_logout.clicked.connect(
            self.load_login)
        # shop information
        self.ui.txt_admin_comp.setText(self.shop_name)
        self.ui.txt_admin_name.setText(self.shop_owner)
        self.ui.txt_admin_contnum.setText(self.shop_mobile)
        self.ui.txt_admin_telnum.setText(self.shop_telephone)
        self.ui.txt_admin_address.setText(self.shop_address)
        self.ui.txt_admin_social.setText(self.shop_socials)
        self.ui.txt_show_email.setText(self.admin_email)

        # attendant information
        self.ui.txt_att_name.setText(self.attendant_fullname)
        self.ui.txt_att_num.setText(self.attendant_mobile)
        self.ui.txt_att_email.setText(self.emp_email)
        self.ui.txt_att_address.setText(self.attendant_address)

    # BOOK BUTTONS
    # bookings
    def on_bookings_page_clicked(self):
        self.load_ui_file("ui/Bookings.ui")
        self.ui.btn_book_view.clicked.connect(self.on_bookings_view_clicked)
        self.ui.btn_searchcus.clicked.connect(
            self.on_bookings_btn_searchcus_clicked)
        self.ui.btn_searchbook.clicked.connect(
            self.on_bookings_btn_searchbook_clicked)

        self.book_id = ""
        cur = self.conn.cursor(cursor_factory=extras.RealDictCursor)
        cur.execute(
            "SELECT book_id,book_type,book_status,book_total,book_vcl_plate,book_vcl_brand,book_vcl_model,CONCAT(emp_fname,' ',emp_mname,' ',emp_lname) AS employee_name,CONCAT(cus_fname,' ',cus_mname,' ',cus_lname) AS customer_name,srv_name,book_details,DATE(book_start) AS book_start,DATE(book_end) AS book_end,emp_id,cus_id,srv_id,DATE(BOOK.date_created) AS date_created" +
            " FROM BOOK INNER JOIN EMPLOYEE USING(emp_id) INNER JOIN CUSTOMER USING(cus_id) INNER JOIN SERVICE USING(srv_id) WHERE book_status != 'Finished' ORDER BY(date_created) DESC")
        rows = cur.fetchall()

        if rows:
            for row_idx, row_data in enumerate(rows):
                for col_idx, col_data in enumerate(row_data.values()):
                    item = QTableWidgetItem(str(col_data))
                    self.ui.tbl_bookings.setItem(row_idx, col_idx, item)
        # Close the cursor
        cur.close()

    def on_bookings_btn_searchbook_clicked(self):
        if (self.ui.txt_bookid.text() and self.is_numeric(self.ui.txt_bookid.text())):
            cur = self.conn.cursor(cursor_factory=extras.RealDictCursor)
            cur.execute(
                "SELECT book_id,book_type,book_status,book_total,book_vcl_plate,book_vcl_brand,book_vcl_model,CONCAT(emp_fname,' ',emp_mname,' ',emp_lname) AS employee_name,CONCAT(cus_fname,' ',cus_mname,' ',cus_lname) AS customer_name,srv_name,book_details,DATE(book_start) AS book_start,DATE(book_end) AS book_end,emp_id,cus_id,srv_id,DATE(BOOK.date_created) AS date_created" +
                " FROM BOOK INNER JOIN EMPLOYEE USING(emp_id) INNER JOIN CUSTOMER USING(cus_id) INNER JOIN SERVICE USING(srv_id) WHERE book_status != 'Finished' AND book_id="+self.ui.txt_bookid.text()+"")
            row = cur.fetchone()

            self.ui.tbl_bookings.clearContents()

            if row:
                row_idx = 0
                for col_idx, col_data in enumerate(row.values()):
                    item = QTableWidgetItem(str(col_data))
                    self.ui.tbl_bookings.setItem(row_idx, col_idx, item)
                QMessageBox.information(self, "Message", "Booking Found!")

                self.book_id = row['book_id']
                self.book_type = row['book_type']
                self.book_status = row['book_status']
                self.book_total = row['book_total']
                self.book_vcl_plate = row['book_vcl_plate']
                self.book_vcl_brand = row['book_vcl_brand']
                self.book_vcl_model = row['book_vcl_model']
                self.book_details = row['book_details']
                self.book_start = row['book_start']
                self.book_end = row['book_end']
                self.customer_name = row['customer_name']
                self.srv_name = row['srv_name']
                self.emp_id = row['emp_id']
                self.cus_id = row['cus_id']
                self.srv_id = row['srv_id']
                self.date_created = row['date_created']

            else:
                QMessageBox.warning(self, "Warning", "Booking Not Found!")
            # Close the cursor
            cur.close()
        else:
            self.on_bookings_page_clicked()

    def on_bookings_view_clicked(self):
        if (self.book_id and self.is_numeric(self.book_id)):
            self.load_ui_file("ui/Booking_details.ui")
            self.ui.btn_booking_update.clicked.connect(
                self.btn_booking_update_clicked)
            self.ui.btn_booking_cancel.clicked.connect(
                self.on_bookings_page_clicked)

            cur = self.conn.cursor(cursor_factory=extras.RealDictCursor)
            cur.execute(
                "SELECT srv_id,srv_category,srv_name,srv_fee,srv_time FROM SERVICE WHERE srv_id=" + str(self.srv_id)+" ;")
            row = cur.fetchone()

            if row:
                self.customer_srv_cat = row['srv_category']

            cur = self.conn.cursor(cursor_factory=extras.RealDictCursor)
            cur.execute("SELECT emp_id,CONCAT(emp_fname,' ',emp_mname,' ',emp_lname) AS emp_name FROM EMPLOYEE WHERE emp_service='" +
                        self.customer_srv_cat+"' ;")
            rows = cur.fetchall()

            self.ui.drp_booking_assignedto.clear()
            self.employee_ids = []
            if rows:
                for row in rows:
                    self.employee_ids.append(row['emp_id'])
                    self.ui.drp_booking_assignedto.addItem(row['emp_name'])

            for i in range(len(self.employee_ids)):
                if (self.employee_ids[i] == self.emp_id):
                    self.ui.drp_booking_assignedto.setCurrentIndex(i)

            self.booking_status = ['Pending', 'Finished', 'Cancelled']

            for i in range(len(self.booking_status)):
                if (self.booking_status[i] == self.book_status):
                    self.ui.drp_booking_status.setCurrentIndex(i)

            self.ui.txt_booking_cusname.setText(self.customer_name)
            self.ui.txt_regplate.setText(self.book_vcl_plate)
            self.ui.txt_booking_vehiclebrand.setText(self.book_vcl_brand)
            self.ui.txt_booking_vehicle_model.setText(self.book_vcl_model)
            self.ui.txt_booking_service.setText(self.srv_name)
            self.ui.drp_service_type.setCurrentIndex(
                0 if self.book_type == 'Paid' else 1)
            self.ui.date_booked.setDate(self.date_created)
            self.ui.txt_booking_details.setText(self.book_details)
            self.ui.date_start.setDate(self.book_start)
            self.ui.date_end.setDate(self.book_end)
            self.ui.txt_totspending.setText(str(self.book_total))

    def on_bookings_btn_searchcus_clicked(self):
        if (self.ui.txt_customerid.text() and self.is_numeric(self.ui.txt_customerid.text())):

            cur = self.conn.cursor(cursor_factory=extras.RealDictCursor)
            cur.execute(
                "SELECT book_id,book_type,book_status,book_total,book_vcl_plate,book_vcl_brand,book_vcl_model,CONCAT(emp_fname,' ',emp_mname,' ',emp_lname) AS employee_name,CONCAT(cus_fname,' ',cus_mname,' ',cus_lname) AS customer_name,srv_name,book_details,DATE(book_start) AS book_start,DATE(book_end) AS book_end,emp_id,cus_id,srv_id,DATE(BOOK.date_created) AS date_created" +
                " FROM BOOK INNER JOIN EMPLOYEE USING(emp_id) INNER JOIN CUSTOMER USING(cus_id) INNER JOIN SERVICE USING(srv_id) WHERE book_status != 'Finished' AND cus_id="+self.ui.txt_customerid.text()+" ORDER BY(date_created) DESC")
            rows = cur.fetchall()

            self.ui.tbl_bookings.clearContents()

            if rows:
                QMessageBox.information(self, "Message", "Booking Found!")
                for row_idx, row_data in enumerate(rows):
                    for col_idx, col_data in enumerate(row_data.values()):
                        item = QTableWidgetItem(str(col_data))
                        self.ui.tbl_bookings.setItem(row_idx, col_idx, item)
            else:
                QMessageBox.warning(self, "Warning", "Booking Not Found!")
            # Close the cursor
            cur.close()

        else:
            self.on_bookings_page_clicked()

    def btn_booking_update_clicked(self):
        if (self.ui.date_end.date() <= self.ui.date_start.date()):
            QMessageBox.information(self, "Message", "Invalid End Date!")
        elif (self.ui.txt_booking_details.toPlainText() == ""):
            QMessageBox.information(self, "Message", "Please enter a detail!")
        elif (self.ui.txt_totspending.text() == "" and self.is_numeric(self.ui.txt_totspending.text())):
            QMessageBox.information(
                self, "Message", "Please enter the total spending!")
        else:

            cur = self.conn.cursor(cursor_factory=extras.RealDictCursor)
            cur.execute("UPDATE BOOK SET book_type='" + self.ui.drp_service_type.currentText() +
                        "', emp_id='" + str(self.employee_ids[self.ui.drp_booking_assignedto.currentIndex()]) +
                        "', book_status='" + self.ui.drp_booking_status.currentText() +
                        "', book_end='" + str(self.ui.date_end.text()) +
                        "', book_details='" + self.ui.txt_booking_details.toPlainText() +
                        "', book_total='" + self.ui.txt_totspending.text() +
                        "' WHERE book_id=" + str(self.book_id) + ";")

            # Commit the changes to the database
            self.conn.commit()

            # Close the cursor
            cur.close()
            QMessageBox.information(self, "Message", "Booking Updated!")
            self.on_bookings_page_clicked()

    # book
    def on_book_page_clicked(self):
        self.load_ui_file("ui/Book_page.ui")

        self.ui.drp_service_cat.currentTextChanged.connect(
            self.service_employee_assignment)
        self.ui.drp_vehicle_type.currentTextChanged.connect(
            self.service_employee_assignment)

        self.ui.btn_searchcus.clicked.connect(self.customer_checker)
        self.ui.btn_cancel.clicked.connect(self.on_books_clicked)
        self.ui.btn_submit.clicked.connect(self.on_books_submit_clicked)
        self.service_employee_assignment()

    def book_fields_checker(self):
        if (self.ui.txt_cusid.text() == "" and self.is_numeric(self.ui.txt_cusid.text())):
            QMessageBox.information(
                self, "Message", "Please enter the id!")
        elif (self.ui.txt_vehicleplate.text() == ""):
            QMessageBox.information(
                self, "Message", "Please enter the registration plate number!")
        elif (self.ui.txt_vehicle_brand.text() == ""):
            QMessageBox.information(
                self, "Message", "Please enter the registration plate number!")
        elif (self.ui.txt_vehicle_model.text() == ""):
            QMessageBox.information(
                self, "Message", "Please enter the registration plate number!")
        elif (self.ui.txt_details.toPlainText() == ""):
            QMessageBox.information(
                self, "Message", "Please enter the details!")
        elif (self.ui.drp_service.currentIndex() == -1 or self.ui.drp_assigned.currentIndex() == -1):
            QMessageBox.information(
                self, "Message", "Service Unavailable!")
        else:
            return True

    def customer_checker(self):
        output = self.on_book_btn_searchcus_clicked()
        if (output == 'y'):
            QMessageBox.information(self, "Message", "Customer Found!")
        elif (output == 'n'):
            QMessageBox.warning(
                self, "Warning", "Customer is currently banned!")
        else:
            QMessageBox.warning(self, "Warning", "Sorry, Customer Not Found!")

    def service_employee_assignment(self):

        self.current_customer_id = self.ui.txt_cusid.text()

        self.ui.txt_service_fee.setText("0.00")
        cur = self.conn.cursor(cursor_factory=extras.RealDictCursor)
        cur.execute("SELECT srv_id,srv_name,srv_fee,srv_time FROM SERVICE WHERE srv_category='" +
                    self.ui.drp_service_cat.currentText()+"' AND srv_type='"+self.ui.drp_vehicle_type.currentText()+"' ;")
        rows = cur.fetchall()

        self.ui.drp_service.clear()

        self.service_ids = []
        self.service_time = []
        if rows:

            for row in rows:
                self.service_ids.append(row['srv_id'])
                self.service_time.append(row['srv_time'])
                column_value = row['srv_name']
                self.ui.drp_service.addItem(str(column_value))
            self.ui.txt_service_fee.setText(str(row['srv_fee']))

        cur.execute("SELECT DISTINCT(emp_id),emp_fname,emp_mname,emp_lname,COUNT(book_id) AS pendings" +
                    " FROM EMPLOYEE LEFT JOIN BOOK USING(emp_id)" +
                    " WHERE emp_service='" + self.ui.drp_service_cat.currentText()+"' AND emp_status ='Active'" +
                    "GROUP BY(emp_id,emp_fname,emp_mname,emp_lname) ORDER BY(pendings)")

        rows = cur.fetchall()

        self.ui.drp_assigned.clear()
        self.employee_ids = []
        if rows:
            for row in rows:
                self.employee_ids.append(row['emp_id'])
                column_value = row['emp_fname']+" " + \
                    row['emp_mname']+" "+row['emp_lname']
                self.ui.drp_assigned.addItem(str(column_value))

        # Close the cursor
        cur.close()

    def on_book_btn_searchcus_clicked(self):
        if (self.ui.txt_cusid.text() and self.is_numeric(self.ui.txt_cusid.text())):
            cur = self.conn.cursor(cursor_factory=extras.RealDictCursor)
            cur.execute("SELECT * FROM CUSTOMER WHERE cus_id=" +
                        self.ui.txt_cusid.text()+"")
            rows = cur.fetchone()

            # Close the cursor
            cur.close()
            if rows:
                if (rows['cus_status'] == 'Disabled'):
                    self.ui.txt_cusid.setText("")
                    return 'n'
                else:
                    return 'y'
            else:
                self.ui.txt_cusid.setText("")
                return False

    def on_books_submit_clicked(self):
        cur = self.conn.cursor(cursor_factory=extras.RealDictCursor)
        cur.execute("SELECT book_end FROM BOOK" +
                    " WHERE emp_id='"+str(self.employee_ids[self.ui.drp_assigned.currentIndex()])+"'" +
                    " AND book_end >= CURRENT_DATE " +
                    " ORDER BY (book_end) DESC "
                    )
        row = cur.fetchone()

        if (row):
            self.latest_booking_end_date = row['book_end']
        else:
            self.latest_booking_end_date = date.today()

        cur = self.conn.cursor(cursor_factory=extras.RealDictCursor)
        cur.execute(
            "INSERT INTO BOOK " +
            "(book_type,book_total,book_vcl_plate,book_vcl_brand,book_vcl_model,emp_id,cus_id,srv_id,book_start,book_end,book_details) " +
            "VALUES ('" + self.ui.drp_service_type.currentText() +
            "', '" + str(self.ui.txt_service_fee.text()) +
            "', '" + self.ui.txt_vehicleplate.text() +
            "', '" + self.ui.txt_vehicle_brand.text() +
            "', '" + self.ui.txt_vehicle_model.text() +
            "', " + str(self.employee_ids[self.ui.drp_assigned.currentIndex()]) +
            ", " + str(self.ui.txt_cusid.text()) +
            ", " + str(self.service_ids[self.ui.drp_service.currentIndex()]) +
            ", '" + str(self.latest_booking_end_date) +
            "', '" + str(self.latest_booking_end_date + timedelta(days=float(self.service_time[self.ui.drp_service.currentIndex()]))) +
            "', '" + self.ui.txt_details.toPlainText() + "');")

        # Commit the changes to the database
        self.conn.commit()

        # Close the cursor
        cur.close()
        QMessageBox.information(self, "Message", "Booking Sucessful!")
        self.on_books_clicked()

    def add_table_service(self):
        self.new_window.close()

    # INVOICE_PAGE BUTTONS

    def on_btn_invoice_view_clicked(self):

        if (self.ui.txt_invoiceid.text() and self.is_numeric(self.ui.txt_invoiceid.text())):
            self.load_ui_file("ui/generate_invoice_page.ui")
            self.ui.btn_exit.clicked.connect(self.on_invoice_clicked)
            self.ui.btn_print.clicked.connect(self.on_btn_print_clicked)

            # shop details
            self.ui.txt_compname.setText(self.shop_name)
            self.ui.txt_contact.setText(str(self.shop_mobile))
            self.ui.txt_tel_num.setText(str(self.shop_telephone))
            self.ui.txt_owner.setText(self.shop_owner)
            self.ui.txt_email.setText(self.admin_email)
            self.ui.txt_address.setText(self.shop_address)

            # customer details
            self.ui.txt_cusid.setText(str(self.cus_id))
            self.ui.txt_cusname.setText(self.customer_name)
            self.ui.txt_cusmnum.setText(str(self.cus_mobile))
            self.ui.txt_cusemail.setText(self.cus_email)
            self.ui.txt_sex.setText(self.cus_sex)
            self.ui.txt_cusaddress.setText(self.cus_address)

            # invoice details
            self.ui.txt_invoiceid.setText(str(self.inv_id))
            self.ui.txt_bookid.setText(str(self.book_id))
            self.ui.txt_datebooked.setText(str(self.date_created))
            self.ui.txt_datefinished.setText(str(self.date_finished))

            # booking details
            self.ui.txt_brand.setText(self.book_vcl_brand)
            self.ui.txt_model.setText(self.book_vcl_model)
            self.ui.txt_regplate.setText(self.book_vcl_plate)
            self.ui.txt_assignedto.setText(self.employee_name)
            self.ui.txt_category.setText(self.srv_category)
            self.ui.txt_service.setText(self.srv_name)

            # invoice summary
            self.ui.txt_svtype.setText(self.book_type)
            self.ui.txt_laborfee.setText(str(self.srv_fee))
            self.ui.txt_amount.setText(
                str(0 if self.book_type == 'Free' else self.book_total))

    def on_btn_print_clicked(self):
        # Specify the region to capture
        region = QRect(220, 30, 771, 461)

        # Capture the screenshot of the specified region
        screenshot = window.grab(region)

        # Save the screenshot to a file
        screenshot.save("invoice-records/"+str(self.cus_id) +
                        str(self.inv_id)+str(self.book_id)+"-generated-invoice.png")

        QMessageBox.information(
            self, "Message", "Invoice Printed Sucessfully!")

    def on_invoice_search_btn_invoice_clicked(self):
        if (self.ui.txt_invoiceid.text() and self.is_numeric(self.ui.txt_invoiceid.text())):
            cur = self.conn.cursor(cursor_factory=extras.RealDictCursor)
            cur.execute(
                "SELECT inv_id,book_type,book_status,book_total,book_vcl_plate,book_vcl_brand,book_vcl_model,CONCAT(emp_fname,' ',emp_mname,' ',emp_lname) AS employee_name,CONCAT(cus_fname,' ',cus_mname,' ',cus_lname) AS customer_name,srv_name,book_details,DATE(book_start) AS book_start,DATE(book_end) AS book_end,emp_id,cus_id,srv_id,book_id,DATE(BOOK.date_created) AS date_created,DATE(INVOICE.date_created) AS date_finished" +
                " FROM BOOK INNER JOIN EMPLOYEE USING(emp_id) INNER JOIN CUSTOMER USING(cus_id) INNER JOIN SERVICE USING(srv_id) INNER JOIN INVOICE USING(book_id) WHERE inv_id="+self.ui.txt_invoiceid.text()+"")
            row = cur.fetchone()

            self.ui.tbl_invoice.clearContents()

            if row:
                row_idx = 0
                for col_idx, col_data in enumerate(row.values()):
                    item = QTableWidgetItem(str(col_data))
                    self.ui.tbl_invoice.setItem(row_idx, col_idx, item)
                QMessageBox.information(self, "Message", "Invoice Found!")

                self.inv_id = row['inv_id']
                self.book_id = row['book_id']
                self.book_type = row['book_type']
                self.book_status = row['book_status']
                self.book_total = row['book_total']
                self.book_vcl_plate = row['book_vcl_plate']
                self.book_vcl_brand = row['book_vcl_brand']
                self.book_vcl_model = row['book_vcl_model']
                self.book_details = row['book_details']
                self.book_start = row['book_start']
                self.book_end = row['book_end']
                self.employee_name = row['employee_name']
                self.customer_name = row['customer_name']
                self.srv_name = row['srv_name']
                self.emp_id = row['emp_id']
                self.cus_id = row['cus_id']
                self.srv_id = row['srv_id']
                self.date_created = row['date_created']
                self.date_finished = row['date_finished']

                cur = self.conn.cursor(cursor_factory=extras.RealDictCursor)
                cur.execute(
                    "SELECT srv_id,srv_category,srv_name,srv_time,srv_fee,srv_type FROM SERVICE WHERE srv_id = '"+str(self.srv_id)+"'")
                row = cur.fetchone()

                if row:
                    self.srv_id = row['srv_id']
                    self.srv_category = row['srv_category']
                    self.srv_name = row['srv_name']
                    self.srv_time = row['srv_time']
                    self.srv_fee = row['srv_fee']
                    self.srv_type = row['srv_type']

                cur = self.conn.cursor(cursor_factory=extras.RealDictCursor)
                cur.execute(
                    "SELECT cus_id, cus_fname, cus_mname, cus_lname,cus_mobile,cus_email,cus_sex,cus_address,cus_status,DATE(date_created) AS date_created FROM CUSTOMER WHERE cus_id="+str(self.cus_id)+"")
                row = cur.fetchone()
                if row:
                    self.cus_id = row['cus_id']
                    self.cus_fname = row['cus_fname']
                    self.cus_mname = row['cus_mname']
                    self.cus_lname = row['cus_lname']
                    self.cus_mobile = row['cus_mobile']
                    self.cus_email = row['cus_email']
                    self.cus_sex = row['cus_sex']
                    self.cus_address = row['cus_address']
                    self.cus_status = row['cus_status']
                    self.date_created = row['date_created']

            else:
                QMessageBox.warning(self, "Warning", "Invoice Not Found!")
                self.on_invoice_clicked()
            # Close the cursor
            cur.close()

    def on_invoice_search_btn_clicked(self):
        if (self.ui.txt_cusid.text() and self.is_numeric(self.ui.txt_cusid.text())):
            self.inv_id = ""
            cur = self.conn.cursor(cursor_factory=extras.RealDictCursor)
            cur.execute(
                "SELECT inv_id,book_type,book_status,book_total,book_vcl_plate,book_vcl_brand,book_vcl_model,CONCAT(emp_fname,' ',emp_mname,' ',emp_lname) AS employee_name,CONCAT(cus_fname,' ',cus_mname,' ',cus_lname) AS customer_name,srv_name,book_details,DATE(book_start) AS book_start,DATE(book_end) AS book_end,emp_id,cus_id,srv_id,book_id,DATE(BOOK.date_created) AS date_created,DATE(INVOICE.date_created) AS date_finished" +
                " FROM BOOK INNER JOIN EMPLOYEE USING(emp_id) INNER JOIN CUSTOMER USING(cus_id) INNER JOIN SERVICE USING(srv_id) INNER JOIN INVOICE USING(book_id) WHERE cus_id="+self.ui.txt_cusid.text()+" ORDER BY(date_finished) DESC")
            rows = cur.fetchall()

            self.ui.tbl_invoice.clearContents()

            if rows:
                for row_idx, row_data in enumerate(rows):
                    for col_idx, col_data in enumerate(row_data.values()):
                        item = QTableWidgetItem(str(col_data))
                        self.ui.tbl_invoice.setItem(row_idx, col_idx, item)
                QMessageBox.information(self, "Message", "Customer Found!")
            else:
                QMessageBox.information(self, "Message", "Customer Not Found!")
                self.on_invoice_clicked()
            # Close the cursor
            cur.close()

    # CUSTOMER_PAGE BUTTONS
    # customer search

    def on_customer_search_btn_clicked(self):
        if (self.ui.txt_customerfname.text() == "" or self.ui.txt_customerlname.text() == ""):
            self.on_customer_clicked()
        else:
            add_email_query = ''
            if (self.ui.txt_email.text()):
                add_email_query = " AND cus_email='"+self.ui.txt_email.text()+"' "

            cur = self.conn.cursor(cursor_factory=extras.RealDictCursor)
            cur.execute(
                "SELECT cus_id, cus_fname, cus_mname, cus_lname,cus_mobile,cus_email,cus_sex,cus_address,cus_status,DATE(date_created) AS date_created FROM CUSTOMER WHERE cus_fname='"+self.ui.txt_customerfname.text()+"' AND cus_mname='"+self.ui.txt_customermname.text()+"' AND cus_lname='"+self.ui.txt_customerlname.text()+"' "+add_email_query)
            row = cur.fetchone()
            if row:

                self.cus_id = row['cus_id']
                self.cus_fname = row['cus_fname']
                self.cus_mname = row['cus_mname']
                self.cus_lname = row['cus_lname']
                self.cus_mobile = row['cus_mobile']
                self.cus_email = row['cus_email']
                self.cus_sex = row['cus_sex']
                self.cus_address = row['cus_address']
                self.cus_status = row['cus_status']
                self.date_created = row['date_created']

                self.ui.tbl_customer.clearContents()
                if row:
                    row_idx = 0
                    for col_idx, col_data in enumerate(row.values()):
                        item = QTableWidgetItem(str(col_data))
                        self.ui.tbl_customer.setItem(row_idx, col_idx, item)

                QMessageBox.information(self, "Message", "Customer Found!")

            else:
                QMessageBox.information(self, "Message", "Customer Not Found!")
                self.on_customer_clicked()

            # Close the cursor
            cur.close()

    # customer add
    def on_customer_add_clicked(self):
        self.load_ui_file("ui/customer_add_page.ui")
        self.ui.btn_add_cus.clicked.connect(self.on_btn_add_cus_clicked)
        self.ui.btn_cancel_add.clicked.connect(self.on_customer_clicked)

    def on_btn_add_cus_clicked(self):
        if (self.ui.txt_firstname.text() == "" or self.ui.txt_lastname.text() == ""):
            QMessageBox.information(
                self, "Message", "Please enter the full name!")
        elif (self.ui.txt_cus_email.text() == ""):
            QMessageBox.information(
                self, "Message", "Please enter the email!")
        elif (self.ui.txt_cus_address.toPlainText() == ""):
            QMessageBox.information(
                self, "Message", "Please enter the address!")
        elif (self.ui.txt_mobilenum.text() == "" or not self.is_mobile(self.ui.txt_mobilenum.text())):
            QMessageBox.information(
                self, "Message", "Please enter the mobile number!")
        else:
            cur = self.conn.cursor(cursor_factory=extras.RealDictCursor)
            cur.execute(
                "INSERT INTO CUSTOMER (cus_fname, cus_mname, cus_lname,cus_mobile,cus_email,cus_sex,cus_address) " +
                "VALUES ('" + self.ui.txt_firstname.text() +
                "', '" + self.ui.txt_middlename.text() +
                "', '" + self.ui.txt_lastname.text() +
                "', '" + str(self.ui.txt_mobilenum.text()) +
                "', '" + self.ui.txt_cus_email.text() +
                "', '" + self.ui.drp_cus_sex.currentText() +
                "', '" + self.ui.txt_cus_address.toPlainText() + "');")

            # Commit the changes to the database
            self.conn.commit()

            # Close the cursor
            cur.close()
            QMessageBox.information(
                self, "Message", "Customer Added Successfully!")
            self.on_customer_clicked()

    # customer update
    def on_customer_view_clicked(self):
        if (self.cus_id):
            self.load_ui_file("ui/customer_update_page.ui")
            self.ui.btn_update_cus.clicked.connect(
                self.on_btn_update_cus_clicked)
            self.ui.btn_update_cancel.clicked.connect(self.on_customer_clicked)

            customer_sex_list = ['Male', 'Female']
            customer_status_list = ['Active', 'Disabled']

            self.ui.txt_firstname.setText(self.cus_fname)
            self.ui.txt_middlename.setText(self.cus_mname)
            self.ui.txt_lastname.setText(self.cus_lname)
            self.ui.txt_mobilenum.setText(self.cus_mobile)
            self.ui.txt_cus_email.setText(self.cus_email)
            self.ui.txt_cus_address.setPlainText(self.cus_address)

            for i in range(len(customer_sex_list)):
                if (self.cus_sex == customer_sex_list[i]):
                    self.ui.drp_cus_sex.setCurrentIndex(i)
                    break

            for i in range(len(customer_status_list)):
                if (self.cus_status == customer_status_list[i]):
                    self.ui.drp_cus_status.setCurrentIndex(i)
                    break

    def on_btn_update_cus_clicked(self):
        if (self.ui.txt_firstname.text() == "" or self.ui.txt_lastname.text() == ""):
            QMessageBox.information(
                self, "Message", "Please enter the full name!")
        elif (self.ui.txt_cus_email.text() == ""):
            QMessageBox.information(
                self, "Message", "Please enter the email!")
        elif (self.ui.txt_cus_address.toPlainText() == ""):
            QMessageBox.information(
                self, "Message", "Please enter the address!")
        elif (self.ui.txt_mobilenum.text() == "" or not self.is_mobile(self.ui.txt_mobilenum.text())):
            QMessageBox.information(
                self, "Message", "Please enter the mobile number!")
        else:
            # cus_id, cus_fname, cus_mname, cus_lname,cus_mobile,cus_email,cus_sex,cus_address,cus_status
            cur = self.conn.cursor(cursor_factory=extras.RealDictCursor)
            cur.execute("UPDATE CUSTOMER SET cus_fname='" + self.ui.txt_firstname.text() +
                        "', cus_mname='" + self.ui.txt_middlename.text() +
                        "', cus_lname='" + self.ui.txt_lastname.text() +
                        "', cus_mobile='" + str(self.ui.txt_mobilenum.text()) +
                        "', cus_email='" + self.ui.txt_cus_email.text() +
                        "', cus_sex='" + self.ui.drp_cus_sex.currentText() +
                        "', cus_address='" + self.ui.txt_cus_address.toPlainText() +
                        "', cus_status='" + self.ui.drp_cus_status.currentText() +
                        "' WHERE cus_id=" + str(self.cus_id) + ";")

            # Commit the changes to the database
            self.conn.commit()

            # Close the cursor
            cur.close()
            QMessageBox.information(
                self, "Message", "Customer Updated Successfully!")
            self.on_customer_clicked()

    # OTHER FUNCTIONS
    def is_float(self, string):
        try:
            float(string)
            return True
        except ValueError:
            return False

    def is_numeric(self, string):
        return string.isdigit()

    def is_mobile(self, string):
        return string.isdigit() and len(string) == 11


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
