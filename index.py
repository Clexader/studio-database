# pip3 install PyQt5 (install library)

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUiType
import sys
import datetime

# library to connect to mysql
import mysql.connector
from sql_executions import Database


# link UI file here
MainUI, _ = loadUiType('main.ui')


# Initiate MainWindow class
class Main(QMainWindow, MainUI):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)

        # App functions
        Database.__init__(self)
        self.handle_buttons()
        self.handle_signals()
        self.ui_changes()

# set app Base start

    def ui_changes(self):
        # UI_Changes in login
        self.tabWidget.tabBar().setVisible(False)           # hide tab bar
        self.tabWidget.setCurrentIndex(0)
        # order tab
        self.input_masks()
        self.dateEdit_5.setVisible(False)
        self.dateEdit_5.setDate(datetime.date.today())
        self.dateEdit_10.setDate(datetime.date.today())
        self.dateEdit_12.setDate(datetime.date.today())
        self.comboBox_4.setVisible(False)
        self.calendarWidget.setSelectedDate(datetime.date.today())

        # Combo boxes
        self.show_packages_combo()
        self.show_photographers_combo()
        self.show_employee_combo()
        # Show TableWidgets
        self.show_all_orders()
        self.show_all_photographers()
        self.show_all_packages()
        self.show_all_employees()
        self.show_all_deliveries()

    def handle_buttons(self):
        self.pushButton.clicked.connect(self.handle_login)
        self.pushButton_24.clicked.connect(self.handle_logout)
        # handle main tab widget
        self.calender_button.clicked.connect(self.open_calender_tab)
        self.new_order_button.clicked.connect(self.open_new_order_tab)
        self.deliveries_button.clicked.connect(self.open_deliveries_tab)
        self.reports_button.clicked.connect(self.open_reports_tab)
        self.photographers_button.clicked.connect(self.open_photographers_tab)
        self.packages_button.clicked.connect(self.open_packages_tab)
        self.history_button.clicked.connect(self.open_history_tab)
        self.statistics_button.clicked.connect(self.open_statistics_tab)
        self.settings_button.clicked.connect(self.open_settings_tab)
        # back to main menu
        self.pushButton_3.clicked.connect(self.open_main_menu_tab)
        self.pushButton_4.clicked.connect(self.open_main_menu_tab)
        self.pushButton_13.clicked.connect(self.open_main_menu_tab)
        self.pushButton_16.clicked.connect(self.open_main_menu_tab)
        self.pushButton_17.clicked.connect(self.open_main_menu_tab)
        self.pushButton_18.clicked.connect(self.open_main_menu_tab)
        self.pushButton_19.clicked.connect(self.open_main_menu_tab)
        self.pushButton_22.clicked.connect(self.open_main_menu_tab)
        self.pushButton_23.clicked.connect(self.open_main_menu_tab)
        # ADD INFO
        self.pushButton_58.clicked.connect(self.add_photographer)
        self.pushButton_34.clicked.connect(self.add_package)
        self.pushButton_49.clicked.connect(self.add_employee)
        self.pushButton_9.clicked.connect(self.add_new_order)
        # SEARCH INFO
        self.pushButton_50.clicked.connect(self.search_employee_edit)
        self.pushButton_36.clicked.connect(self.search_package)
        self.pushButton_10.clicked.connect(self.search_order_intable)
        self.pushButton_29.clicked.connect(self.search_photographer_intable)
        self.pushButton_35.clicked.connect(self.search_employee_intable)
        # EDIT INFO
        self.pushButton_48.clicked.connect(self.edit_employee)
        self.pushButton_20.clicked.connect(self.edit_order)
        self.pushButton_56.clicked.connect(self.enable_edit_order)
        self.pushButton_41.clicked.connect(self.edit_photographer)
        self.pushButton_42.clicked.connect(self.edit_package)
        # DELETE INFO
        self.pushButton_21.clicked.connect(self.delete_order)
        self.pushButton_33.clicked.connect(self.delete_package)
        self.pushButton_53.clicked.connect(self.delete_photographers)
        self.pushButton_54.clicked.connect(self.delete_employee)
        # PERMISSIONS
        self.pushButton_38.clicked.connect(self.employee_permissions)
        # COOL ACTIONS
        self.pushButton_11.clicked.connect(self.proceed_to_order)
        # self.pushButton_32.clicked.connect(self.show_full_order)

        #testing
        self.pushButton_37.clicked.connect(self.clear_newOrder_data)

# HANDLE COOL STUFF
    def handle_signals(self):
        #COMBOBOXES
        self.comboBox_3.currentIndexChanged.connect(self.order_date_search)
        self.comboBox_packages.currentIndexChanged.connect(self.package_active_New)
        self.comboBox_packages_3.currentIndexChanged.connect(self.package_active_Edit)
        self.comboBox_packages_2.currentIndexChanged.connect(self.apply_discount)
        #TABLES
        self.tableWidget.doubleClicked.connect(self.show_selected_order)
        self.tableWidget_7.doubleClicked.connect(self.show_selected_photographer)
        self.tableWidget_11.doubleClicked.connect(self.show_full_order)
        self.calendarWidget.clicked.connect(self.catch_date)
        #CHECKBOXES
        self.checkBox_14.stateChanged.connect(self.location_fee_New)
        self.checkBox_15.stateChanged.connect(self.location_fee_Edit)
        self.lineEdit_28.textChanged.connect(self.update_remaining_Edit)
        self.lineEdit_31.textChanged.connect(self.update_remaining_Edit)
        self.lineEdit_11.textChanged.connect(self.update_remaining_New)
        self.lineEdit_10.textChanged.connect(self.update_remaining_New)

    def input_masks(self):
        self.lineEdit_8.setInputMask('(000) 0000-0000')
        self.lineEdit_9.setInputMask('(000) 0000-0000')
        self.lineEdit_27.setInputMask('(000) 0000-0000')
        self.lineEdit_26.setInputMask('(000) 0000-0000')

    # set app functions
    def handle_login(self):
        self.tabWidget.setCurrentIndex(1)

    def handle_logout(self):
        self.tabWidget.setCurrentIndex(0)

    def handle_reset_password(self):
        pass

# HANDLE COMPLEX CALENDER
    def show_calender(self):
        pass

# HANDLE ORDERS
    def add_new_order(self):
        groom_name = self.lineEdit_6.text()
        bride_name = self.lineEdit_7.text()
        phone1 = self.lineEdit_8.text()
        phone2 = self.lineEdit_9.text()
        event_type = self.comboBox_2.currentText()
        event_date = self.dateEdit_10.date().toString("yyyy/MM/dd")  # only format expeted in date by MySQL
        package = self.comboBox_packages.currentIndex()
        price = self.lineEdit_10.text()
        down_payment = self.lineEdit_11.text()
        remaining_payment = str(float(price) - float(down_payment))      # call operation (price - down payment)
        photographer = self.comboBox_photographers.currentIndex()
        location = self.textEdit.toPlainText()
        if self.checkBox_14.isChecked():
            out_mansoura = 'Yes'
        else:
            out_mansoura = 'No'
        comments = self.textEdit_2.toPlainText()
        employee = 1                                # call it by default by login

        c_date = datetime.datetime.now()                               # calls current date [not formated]
        current_date = c_date.strftime("%d/%m/%Y %H:%M:%S")

        self.cur.execute('''
            INSERT INTO orders (
                Groom_Name,
                Bride_Name,
                Phone_Number,
                Phone_Number_2,
                Event_Type,
                Event_Date,
                Package_id,
                Price,
                Down_Payment,
                Remaining_Payment,
                Photographer_id,
                Locations,
                outside_mansoura,
                Comments,
                Employee_id,
                DateStamp
                )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''',
            (
                groom_name,
                bride_name,
                phone1,
                phone2,
                event_type,
                event_date,
                package,
                price,
                down_payment,
                remaining_payment,
                photographer,
                location,
                out_mansoura,
                comments,
                employee,
                current_date
            )
        )
        self.db.commit()
        self.statusBar().showMessage('Order added successfully!')
        self.show_all_orders()              # to update the table with the new data
        self.clear_orderEdit_data()

    def search_order_intable(self):
        order = self.lineEdit_17.text()
        date = self.dateEdit_5.date().toString("yyyy-MM-dd")
        event_type = self.comboBox_4.currentText()
        index = self.comboBox_3.currentIndex()
        mysql_str = '%'                                 # required for "LIKE statment" in mysql query
        search = order + mysql_str

        if index == 1:
            self.cur.execute('''
                SELECT
                    o.id, o.Groom_Name, o.Bride_Name, o.Event_Type, o.Event_Date, Phone_Number, Phone_Number_2, p.Name,
                    o.Price, o.Down_Payment, o.Remaining_Payment, ph.Name, o.Locations, o.outside_mansoura, o.Comments
                FROM orders o
                JOIN packages p ON o.Package_id = p.id
                JOIN photographers ph ON o.Photographer_id = ph.id
                WHERE o.id LIKE %s
                ''', [search])
        elif index == 2:
            self.cur.execute('''
                SELECT
                    o.id, o.Groom_Name, o.Bride_Name, o.Event_Type, o.Event_Date, Phone_Number, Phone_Number_2, p.Name,
                    o.Price, o.Down_Payment, o.Remaining_Payment, ph.Name, o.Locations, o.outside_mansoura, o.Comments
                FROM orders o
                JOIN packages p ON o.Package_id = p.id
                JOIN photographers ph ON o.Photographer_id = ph.id
                WHERE o.Groom_Name LIKE %s
                ''', [search])
        elif index == 3:
            self.cur.execute('''
                SELECT
                    o.id, o.Groom_Name, o.Bride_Name, o.Event_Type, o.Event_Date, Phone_Number, Phone_Number_2, p.Name,
                    o.Price, o.Down_Payment, o.Remaining_Payment, ph.Name, o.Locations, o.outside_mansoura, o.Comments
                FROM orders o
                JOIN packages p ON o.Package_id = p.id
                JOIN photographers ph ON o.Photographer_id = ph.id
                WHERE o.Bride_Name LIKE %s
                ''', [search])
        elif index == 4:
            self.cur.execute('''
                SELECT
                    o.id, o.Groom_Name, o.Bride_Name, o.Event_Type, o.Event_Date, Phone_Number, Phone_Number_2, p.Name,
                    o.Price, o.Down_Payment, o.Remaining_Payment, ph.Name, o.Locations, o.outside_mansoura, o.Comments
                FROM orders o
                JOIN packages p ON o.Package_id = p.id
                JOIN photographers ph ON o.Photographer_id = ph.id
                WHERE Phone_Number LIKE %s OR Phone_Number_2 LIKE %s
                ''', (search, search))
        elif index == 5:
            self.cur.execute('''
                SELECT
                    o.id, o.Groom_Name, o.Bride_Name, o.Event_Type, o.Event_Date, Phone_Number, Phone_Number_2, p.Name,
                    o.Price, o.Down_Payment, o.Remaining_Payment, ph.Name, o.Locations, o.outside_mansoura, o.Comments
                FROM orders o
                JOIN packages p ON o.Package_id = p.id
                JOIN photographers ph ON o.Photographer_id = ph.id
                WHERE o.Event_Date LIKE %s
                ''', [date])
        elif index == 6:
            self.cur.execute('''
                SELECT
                    o.id, o.Groom_Name, o.Bride_Name, o.Event_Type, o.Event_Date, Phone_Number, Phone_Number_2, p.Name,
                    o.Price, o.Down_Payment, o.Remaining_Payment, ph.Name, o.Locations, o.outside_mansoura, o.Comments
                FROM orders o
                JOIN packages p ON o.Package_id = p.id
                JOIN photographers ph ON o.Photographer_id = ph.id
                WHERE o.Event_Type LIKE %s
                ''', [event_type])
        else:
            QMessageBox.warning(self, 'Search error', 'Choose search filter!')

        data = self.cur.fetchall()
        # Update table
        self.tableWidget.setRowCount(0)
        self.tableWidget.insertRow(0)
        for row, order in enumerate(data):
            for col, item in enumerate(order):
                self.tableWidget.setItem(row, col, QTableWidgetItem(str(item)))
                col += 1

            row_position = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row_position)

        self.statusBar().showMessage(f'{len(data)} order(s) found')

    def edit_order(self):  #ERROR
        base = self.lineEdit_35.text()

        groom_name = self.lineEdit_32.text()
        bride_name = self.lineEdit_30.text()
        phone1 = self.lineEdit_27.text()
        phone2 = self.lineEdit_26.text()
        event_type = self.comboBox_7.currentText()
        event_date = self.dateEdit_12.date().toString("yyyy/MM/dd")
        package = self.comboBox_packages_3.currentIndex()
        price = self.lineEdit_31.text()
        down_payment = self.lineEdit_28.text()
        remaining_payment = self.lineEdit_33.text()      # call operation (price - down payment)
        photographer = self.comboBox_photographers_3.currentIndex()
        location = self.textEdit_7.toPlainText()
        if self.checkBox_15.isChecked():
            out_mansoura = 'Yes'
        else:
            out_mansoura = 'No'
        comments = self.textEdit_8.toPlainText()

        self.cur.execute('''
            UPDATE orders
            SET Groom_Name = %s,
                Bride_Name = %s,
                Phone_Number = %s,
                Phone_Number_2 = %s,
                Event_Type = %s,
                Event_Date = %s,
                Package_id = %s,
                Price = %s,
                Down_Payment = %s,
                Remaining_Payment = %s,
                Photographer_id = %s,
                Locations = %s,
                outside_mansoura = %s,
                Comments = %s
            WHERE id = %s
            ''',
            (
                groom_name,
                bride_name,
                phone1,
                phone2,
                event_type,
                event_date,
                package,
                price,
                down_payment,
                remaining_payment,
                photographer,
                location,
                out_mansoura,
                comments,
                base
            )
        )
        self.db.commit()
        self.statusBar().showMessage('Order edited successfully!')
        self.show_all_orders()
        self.clear_orderEdit_data()

    def print_new_order(self):
        pass

    def show_all_orders(self):
        # show all orders in 'show tab'
        self.tableWidget.setRowCount(0)
        self.tableWidget.insertRow(0)

        self.cur.execute('''
                SELECT
                    o.id, o.Groom_Name, o.Bride_Name, o.Event_Type, o.Event_Date, Phone_Number, Phone_Number_2, p.Name,
                    o.Price, o.Down_Payment, o.Remaining_Payment, ph.Name, o.Locations, o.outside_mansoura, o.Comments
                FROM orders o
                JOIN packages p ON o.Package_id = p.id
                JOIN photographers ph ON o.Photographer_id = ph.id
                ''')
        data = self.cur.fetchall()

        for row, order in enumerate(data):      # enumerate count the loop, row= counts , order = items
            for col, item in enumerate(order):
                self.tableWidget.setItem(row, col, QTableWidgetItem(str(item)))
                col += 1

            row_position = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row_position)

    def delete_order(self):
        order_id = self.lineEdit_35.text()
        order = self.lineEdit_32.text()

        confirm = QMessageBox.question(self, 'Confirm', f'Are You sure you want to delete ({order}) order',
                                      QMessageBox.Yes | QMessageBox.No)
        if confirm == QMessageBox.Yes:
            self.cur.execute('''DELETE FROM orders WHERE id = %s''', [order_id])
            self.db.commit()
            self.statusBar().showMessage('Order deleted successfully!')
            self.show_all_orders()

        else:
            self.statusBar().showMessage('Order delete aborted!')

    def clear_newOrder_data(self):
        self.lineEdit_6.setText('')
        self.lineEdit_7.setText('')
        self.lineEdit_8.setText('')
        self.lineEdit_9.setText('')
        self.comboBox_2.setCurrentIndex(0)
        self.dateEdit_10.setDate(datetime.date.today())
        self.comboBox_packages.setCurrentIndex(0)
        self.comboBox_packages_2.setCurrentIndex(0)
        self.lineEdit_10.setText('')
        self.lineEdit_11.setText('')
        self.comboBox_photographers.setCurrentIndex(0)
        self.textEdit.setPlainText('')
        self.checkBox_14.setCheckState(False)
        self.textEdit_2.setPlainText('')

    def clear_orderEdit_data(self):
        self.lineEdit_32.setEnabled(False)
        self.lineEdit_30.setEnabled(False)
        self.lineEdit_27.setEnabled(False)
        self.lineEdit_26.setEnabled(False)
        self.comboBox_7.setEnabled(False)
        self.dateEdit_12.setEnabled(False)
        self.comboBox_packages_3.setEnabled(False)
        self.comboBox_photographers_3.setEnabled(False)
        self.lineEdit_28.setEnabled(False)
        self.textEdit_7.setEnabled(False)
        self.textEdit_8.setEnabled(False)
        self.pushButton_20.setEnabled(False)
        self.pushButton_21.setEnabled(False)
        self.checkBox_15.setEnabled(False)
        self.checkBox_15.setChecked(False)
        self.lineEdit_31.setText('')
        self.lineEdit_33.setText('')
        self.lineEdit_32.setText('')
        self.lineEdit_30.setText('')
        self.lineEdit_27.setText('')
        self.lineEdit_26.setText('')
        self.comboBox_7.setCurrentIndex(0)
        # self.dateEdit_12.setText('')
        self.comboBox_packages_3.setCurrentIndex(0)
        self.comboBox_photographers_3.setCurrentIndex(0)
        self.lineEdit_28.setText('')
        self.textEdit_7.setPlainText('')
        self.textEdit_8.setPlainText('')
        self.pushButton_20.setEnabled(False)
        self.pushButton_21.setEnabled(False)

# HANDLE DELIVERIES
    def show_all_deliveries(self):
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.insertRow(0)

        self.cur.execute('''
                    SELECT
                        o.id as 'ID',
                        o.Groom_Name as 'Name',
                        o.Phone_Number as 'phone',
                        o.Event_Date,
                        p.Name,
                        p.Banners,
                        p.Frames,
                        p.Photos,
                        p.Albums,
                        DATE_ADD(o.Event_Date, INTERVAL 20 day) as "deadline"
                    FROM orders o
                    JOIN packages p
                        ON o.Package_id = p.id
                ''')
        data = self.cur.fetchall()

        for row, order in enumerate(data):  # enumerate count the loop, row= counts , order = items
            for col, item in enumerate(order):
                self.tableWidget_2.setItem(row, col, QTableWidgetItem(str(item)))
                col += 1

            row_position = self.tableWidget_2.rowCount()
            self.tableWidget_2.insertRow(row_position)

    def edit_deliveries(self):
        pass

# HANDLE PHOTOGRAPHERS
    def show_all_photographers(self):
        self.tableWidget_7.setRowCount(0)
        self.tableWidget_7.insertRow(0)

        self.cur.execute('''
                    SELECT id, Name, Studio, Phone, Email, Description
                    FROM photographers
                ''')
        data = self.cur.fetchall()

        for row, order in enumerate(data):  # enumerate count the loop, row= counts , order = items
            for col, item in enumerate(order):
                self.tableWidget_7.setItem(row, col, QTableWidgetItem(str(item)))
                col += 1

            row_position = self.tableWidget_7.rowCount()
            self.tableWidget_7.insertRow(row_position)

    def add_photographer(self):
        # get data from gui
        photographer_name = self.lineEdit_59.text()        # Qstring attribute for lineedit is text
        photographer_studio = self.lineEdit_60.text()
        photographer_phone = self.lineEdit_68.text()
        photographer_email = self.lineEdit_67.text()
        photographer_info = self.textEdit_9.toPlainText()  # Qstring for textedit is toPlainText

        # use mysql query
        self.cur.execute('''
            INSERT INTO photographers (Name , Studio , Phone , Email , Description)
            VALUES (%s , %s , %s , %s , %s)''',
            (
                photographer_name,
                photographer_studio,
                photographer_phone,
                photographer_email,
                photographer_info
            )
        )

        self.db.commit()
        self.statusBar().showMessage('Photographer added successfully!')
        self.show_all_photographers()
        QMessageBox.information(self, 'Appp Message', 'Photographer added successfully!')
        self.lineEdit_59.setText('')
        self.lineEdit_60.setText('')
        self.lineEdit_68.setText('')
        self.lineEdit_67.setText('')
        self.textEdit_9.setPlainText('')


    def edit_photographer(self):
        search = self.lineEdit_47.text()

        photographer_name = self.lineEdit_54.text()
        photographer_studio = self.lineEdit_56.text()
        photographer_phone = self.lineEdit_64.text()
        photographer_email = self.lineEdit_65.text()
        photographer_info = self.textEdit_5.toPlainText()

        self.cur.execute('''
            UPDATE photographers
            SET Name = %s, Studio = %s, Phone = %s, Email = %s, Description = %s
            WHERE id = %s
            ''', (
                photographer_name,
                photographer_studio,
                photographer_phone,
                photographer_email,
                photographer_info,
                search
            )
        )
        self.db.commit()
        self.statusBar().showMessage('Photographer edited successfully!')
        self.show_all_photographers()

    def search_photographer_intable(self):
        search = self.lineEdit_53.text()
        index = self.comboBox_11.currentIndex()
        mysql_str = '%'
        record = search + mysql_str
        des_filter = mysql_str + search + mysql_str         # search in equipment for anything

        if index == 1:
            self.cur.execute('''
                SELECT
                    id, Name, Studio, Phone, Email, Description
                FROM photographers WHERE id LIKE %s
                ''', [record])
        elif index == 2:
            self.cur.execute('''
                SELECT
                    id, Name, Studio, Phone, Email, Description
                FROM photographers WHERE Name LIKE %s
                ''', [record])
        elif index == 3:
            self.cur.execute('''
                SELECT
                    id, Name, Studio, Phone, Email, Description
                FROM photographers WHERE Studio LIKE %s
                ''', [record])
        elif index == 4:
            self.cur.execute('''
                SELECT
                    id, Name, Studio, Phone, Email, Description
                FROM photographers WHERE Phone LIKE %s
                ''', [record])
        elif index == 5:
            self.cur.execute('''
                SELECT
                    id, Name, Studio, Phone, Email, Description
                FROM photographers WHERE Email LIKE %s
                ''', [record])
        elif index == 6:
            self.cur.execute('''
                SELECT
                    id, Name, Studio, Phone, Email, Description
                FROM photographers WHERE Description LIKE %s
                ''', [des_filter])
        else:
            QMessageBox.warning(self, 'Search error', 'Choose search filter!')

        data = self.cur.fetchall()
        # Update table
        self.tableWidget_7.setRowCount(0)
        self.tableWidget_7.insertRow(0)
        for row, order in enumerate(data):
            for col, item in enumerate(order):
                self.tableWidget_7.setItem(row, col, QTableWidgetItem(str(item)))
                col += 1

            row_position = self.tableWidget_7.rowCount()
            self.tableWidget_7.insertRow(row_position)

        if len(data) == 1:
            self.statusBar().showMessage(f'{len(data)} photographer found')
        else:
            self.statusBar().showMessage(f'{len(data)} photographer found')

    def delete_photographers(self):
        search = self.lineEdit_47.text()
        name = self.lineEdit_54.text()

        confirm = QMessageBox.question(self, 'Confirm', f'Are You sure you want to delete {name} from packages',
                                       QMessageBox.Yes | QMessageBox.No)
        if confirm == QMessageBox.Yes:
            self.cur.execute('''DELETE FROM photographers WHERE id = %s''', [search])
            self.statusBar().showMessage('Photographer deleted successfully!')
            self.show_all_photographers()
            self.db.commit()
        else:
            self.statusBar().showMessage('Photographer delete aborted!')

    def show_photographers_combo(self):
        #combo box in  orders tab
        self.comboBox_photographers.clear()
        self.comboBox_photographers_3.clear()
        self.comboBox_photographers.addItem('------------')
        self.comboBox_photographers_3.addItem('------------')
        self.cur.execute('''
            SELECT Name FROM photographers
            ORDER BY id
        ''')

        photographers = self.cur.fetchall()
        photographers_list = []
        for photographer in photographers:
            photographers_list.append(photographer[0])

        self.comboBox_photographers.addItems(photographers_list)
        self.comboBox_photographers_3.addItems(photographers_list)

# HANDLE PACKAGES
    def show_all_packages(self):        # for list view in package tab
        self.tableWidget_5.setRowCount(0)
        self.tableWidget_5.insertRow(0)

        self.cur.execute('''SELECT Name, Price FROM packages ORDER BY Price''')
        data = self.cur.fetchall()

        for row, order in enumerate(data):  # enumerate count the loop, row= counts , order = items
            for col, item in enumerate(order):
                self.tableWidget_5.setItem(row, col, QTableWidgetItem(str(item)))
                col += 1

            row_position = self.tableWidget_5.rowCount()
            self.tableWidget_5.insertRow(row_position)

    def add_package(self):
        package_name = self.lineEdit_58.text()
        package_price = self.lineEdit_57.text()
        num_banners = self.spinBox_banners.value()     # int attribute for spinBox is value
        num_frames = self.spinBox_frames.value()
        num_photos = self.spinBox_photos.value()
        num_albums = self.spinBox_albums.value()
        package_info = self.textEdit_6.toPlainText()

        self.cur.execute('''
            INSERT INTO packages (Name , Price , Banners , Frames , Photos , Albums , Description)
            VALUES (%s , %s , %s , %s , %s , %s , %s)''',
            (
                package_name,
                package_price,
                num_banners,
                num_frames,
                num_photos,
                num_albums,
                package_info
            )
        )

        self.db.commit()
        self.statusBar().showMessage('Package added successfully!')
        self.show_all_packages()

    def search_package(self):
        search = self.lineEdit_61.text()

        self.cur.execute('''SELECT * FROM packages WHERE Name = %s''', [search])
        data = self.cur.fetchall()

        self.lineEdit_58.setText(str(data[0][1]))
        self.lineEdit_57.setText(str(data[0][2]))
        self.spinBox_banners.setValue(data[0][3])
        self.spinBox_frames.setValue(data[0][4])
        self.spinBox_photos.setValue(data[0][5])
        self.spinBox_albums.setValue(data[0][6])
        self.textEdit_6.setPlainText(str(data[0][7]))

    def edit_package(self):
        search = self.lineEdit_61.text()
        package_name = self.lineEdit_58.text()
        package_price = self.lineEdit_57.text()
        num_banners = self.spinBox_banners.value()
        num_frames = self.spinBox_frames.value()
        num_photos = self.spinBox_photos.value()
        num_albums = self.spinBox_albums.value()
        package_info = self.textEdit_6.toPlainText()

        self.cur.execute('''
            UPDATE packages
            SET Name = %s, Price = %s, Banners = %s, Frames = %s, Photos = %s, Albums = %s, Description = %s
            WHERE Name = %s
        ''', (
                package_name,
                package_price,
                num_banners,
                num_frames,
                num_photos,
                num_albums,
                package_info,
                search
            )
        )
        self.db.commit()
        self.statusBar().showMessage('Package edited successfully!')
        self.show_all_packages()

    def delete_package(self):
        search = self.lineEdit_61.text()

        confirm = QMessageBox.question(self, 'Confirm', f'Are You sure you want to delete ({search}) from packages',
                                       QMessageBox.Yes | QMessageBox.No)
        if confirm == QMessageBox.Yes:
            self.cur.execute('''DELETE FROM packages WHERE Name = %s''', [search])
            self.statusBar().showMessage('Package deleted successfully!')
            self.show_all_packages()
            self.db.commit()
        else:
            self.statusBar().showMessage('Package delete aborted!')

    def show_packages_combo(self):          # show packages in comboBox
        #combo box in  orders tab
        self.comboBox_packages.clear()
        self.comboBox_packages_3.clear()
        self.comboBox_packages.addItem('------------')
        self.comboBox_packages_3.addItem('------------')
        self.cur.execute('''
            SELECT Name FROM packages
            ORDER BY id
        ''')

        packages = self.cur.fetchall()      # the function return tuble, must tranfer into list
        packages_list = []

        for package in packages:
            packages_list.append(package[0])

        self.comboBox_packages.addItems(packages_list)      # addItems takes list , addItem takes str
        self.comboBox_packages_3.addItems(packages_list)

#################################################
#################################################
# HANDLE REPORTS
    def all_orders_report(self):
        pass

    def orders_filter_report(self):
        # search in orders report
        pass

    def orders_export_report(self):
        # export report
        pass

# HANDLE PHOTOGRAPHERS
    def all_photographers_report(self):
        pass

    def photographers_filter_report(self):
        # search in photographers report
        pass

    def photographers_export_report(self):
        # export report
        pass

# HANDLE DELIVERIES
    def all_deliveries_report(self):
        pass

    def deliveries_filter_report(self):
        # search in deliveries report
        pass

    def deliveries_export_report(self):
        # export report
        pass

#################################################
#################################################

# ADMINSTRATOR SYSTEM
    def show_history(self):
        # handle all action in the app
        pass

    def admin_report(self):
        pass

# EMPLOYEE PROPERTIES
    def add_employee(self):
        employee_name = self.lineEdit_96.text()
        employee_phone = self.lineEdit_93.text()
        employee_email = self.lineEdit_95.text()
        join_date = self.dateEdit_4.date().toString("yyyy/MM/dd")
        # join date not fixed, need to work with Qdateedit to add date to MySQL
        national_id = self.lineEdit_97.text()
        priority = self.lineEdit_99.text()
        password = self.lineEdit_92.text()
        check_password = self.lineEdit_94.text()

        if password == check_password:
            self.cur.execute('''
                INSERT INTO employees (Name, phone, Email, Date, National_ID, Priority, Password)
                VALUES (%s, %s, %s, %s, %s, %s, %s)''',
                (
                    employee_name,
                    employee_phone,
                    employee_email,
                    join_date,
                    national_id,
                    priority,
                    password
                )
            )

            self.db.commit()
            self.statusBar().showMessage('Employee added successfully!')
            self.show_all_employees()
        else:
            print('Password not matched!')

    def search_employee_edit(self):           # search
        employee = self.lineEdit_91.text()
        password = self.lineEdit_105.text()

        self.cur.execute('''SELECT * FROM employees''')
        data = self.cur.fetchall()
        for row in data:
            if row[1] == employee and row[7] == password:
                self.groupBox_12.setEnabled(True)
                self.lineEdit_102.setText(row[1])
                self.lineEdit_88.setText(row[2])
                self.lineEdit_98.setText(str(row[5]))
                self.lineEdit_90.setText(row[3])
                self.lineEdit_100.setText(str(row[6]))
                self.lineEdit_101.setText(row[4])  # call date in date edit
                break
        else:           # if the loop finished no record found, lock the edit group box
            self.groupBox_12.setEnabled(False)
            self.lineEdit_102.setText('')
            self.lineEdit_88.setText('')
            self.lineEdit_98.setText('')
            self.lineEdit_90.setText('')
            self.lineEdit_100.setText('')
            self.lineEdit_101.setText('')
            QMessageBox.warning(self, 'Error', 'Wrong username or password, try again.')

        self.statusBar().showMessage('Search Done!')

    def edit_employee(self):
        search = self.lineEdit_91.text()        # used to save in the right row in case employee name changed

        employee_name = self.lineEdit_102.text()
        employee_phone = self.lineEdit_88.text()
        employee_email = self.lineEdit_90.text()
        join_date = self.lineEdit_101.text()               # not fixed, need to work with Qdateedit to add date to MySQL
        national_id = self.lineEdit_98.text()
        priority = self.lineEdit_100.text()

        self.cur.execute('''
            UPDATE employees
            SET Name = %s,
                Phone = %s,
                Email = %s,
                Date = %s,
                National_ID = %s,
                Priority = %s
            WHERE Name = %s
            ''',
            (
                employee_name,
                employee_phone,
                employee_email,
                join_date,
                national_id,
                priority,
                search
            )
        )

        self.db.commit()
        self.statusBar().showMessage('Employee edited successfully!')
        self.show_all_employees()
        self.groupBox_12.setEnabled(False)
        # clear data
        self.lineEdit_91.setText('')
        self.lineEdit_105.setText('')
        self.lineEdit_102.setText('')
        self.lineEdit_88.setText('')
        self.lineEdit_90.setText('')
        self.lineEdit_101.setText('')
        self.lineEdit_98.setText('')
        self.lineEdit_100.setText('')
        QMessageBox.information(self, 'Employee Database', 'Employee edited successfully!')

    def employee_permissions(self):
        employee_id = self.comboBox.currentText()
        calendar = 0
        orders = 0
        deliveries = 0
        reports = 0
        history = 0
        photographer = 0
        package = 0
        statistics = 0
        settings = 0

        if self.checkBox_5.isChecked():
            calendar = 1
        if self.checkBox_6.isChecked():
            orders = 1
        if self.checkBox_8.isChecked():
            deliveries = 1
        if self.checkBox_7.isChecked():
            reports = 1
        if self.checkBox_11.isChecked():
            history = 1
        if self.checkBox_9.isChecked():
            photographer = 1
        if self.checkBox_10.isChecked():
            package = 1
        if self.checkBox_12.isChecked():
            statistics = 1
        if self.checkBox_13.isChecked():
            settings = 1

        self.cur.execute('''
            INSERT INTO employee_permissions 
            (
                employee_name,
                calender_tab,
                orders_tab,
                deliveries_tab,
                reports_tab,
                history_tab,
                photographer_tab,
                package_tab,
                statistics_tab,
                settings_tab
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ''',(employee_id, calendar, orders, deliveries, reports, history, photographer, package, statistics, settings))
        self.db.commit()
        print('permissions added')

    def search_employee_intable(self):
        search = self.lineEdit_55.text()
        index = self.comboBox_14.currentIndex()
        mysql_str = '%'
        record = search + mysql_str

        if index == 1:
            self.cur.execute('''
                SELECT id, Name, Phone, Email, Priority, Date
                FROM employees WHERE id LIKE %s
            ''', [record])
        elif index == 2:
            self.cur.execute('''
                SELECT id, Name, Phone, Email, Priority, Date
                FROM employees WHERE Name LIKE %s
            ''', [record])
        elif index == 3:
            self.cur.execute('''
                SELECT id, Name, Phone, Email, Priority, Date
                FROM employees WHERE Phone LIKE %s
            ''', [record])
        elif index == 4:
            self.cur.execute('''
                SELECT id, Name, Phone, Email, Priority, Date
                FROM employees WHERE Email LIKE %s
            ''', [record])
        elif index == 5:
            self.cur.execute('''
                SELECT id, Name, Phone, Email, Priority, Date
                FROM employees WHERE Priority LIKE %s
            ''', [record])
        else:
            QMessageBox.warning(self, 'Search error', 'Choose search filter!')

        data = self.cur.fetchall()
        # Update table
        self.tableWidget_8.setRowCount(0)
        self.tableWidget_8.insertRow(0)
        for row, order in enumerate(data):
            for col, item in enumerate(order):
                self.tableWidget_8.setItem(row, col, QTableWidgetItem(str(item)))
                col += 1

            row_position = self.tableWidget_8.rowCount()
            self.tableWidget_8.insertRow(row_position)

        if len(data) == 1:
            self.statusBar().showMessage(f'{len(data)} employee found')
        else:
            self.statusBar().showMessage(f'{len(data)} employees found')

    def show_all_employees(self):
        self.tableWidget_8.setRowCount(0)
        self.tableWidget_8.insertRow(0)

        self.cur.execute('''
                    SELECT id, Name, Phone, Email, Priority
                    FROM employees
                    ORDER BY Name
                ''')
        data = self.cur.fetchall()

        for row, order in enumerate(data):  # enumerate count the loop, row= counts , order = items
            for col, item in enumerate(order):
                self.tableWidget_8.setItem(row, col, QTableWidgetItem(str(item)))
                col += 1

            row_position = self.tableWidget_8.rowCount()
            self.tableWidget_8.insertRow(row_position)

    def delete_employee(self):
        search = self.lineEdit_91.text()

        confirm = QMessageBox.question(self, 'Confirm', f'Are You sure you want to delete {search} from Employees',
                                       QMessageBox.Yes | QMessageBox.No)
        if confirm == QMessageBox.Yes:
            self.cur.execute('''DELETE FROM employees WHERE Name = %s''', [search])
            self.statusBar().showMessage('Employee deleted successfully!')
            self.show_all_employees()
            self.db.commit()
        else:
            self.statusBar().showMessage('Employee delete aborted!')

    def show_employee_combo(self):
        self.comboBox.clear()
        self.comboBox.addItem('------------')
        self.cur.execute('''
            SELECT Name FROM employees
        ''')
        employees = self.cur.fetchall()
        for employee in employees:
            self.comboBox.addItem(employee[0])

# ############################################################
# #######ORDERS####### HANDLE COOL STUFF ######ORDERS#######
    def order_date_search(self):
        index = self.comboBox_3.currentIndex()
        if index == 5:
            self.lineEdit_17.setVisible(False)          #search
            self.dateEdit_5.setVisible(True)            #date
            self.comboBox_4.setVisible(False)           #eventtype
        elif index == 6:
            self.lineEdit_17.setVisible(False)
            self.dateEdit_5.setVisible(False)
            self.comboBox_4.setVisible(True)
        else:
            self.lineEdit_17.setVisible(True)
            self.dateEdit_5.setVisible(False)
            self.comboBox_4.setVisible(False)

    def show_selected_order(self, mu):
        self.tabWidget_order.setCurrentIndex(2)
        row = mu.row()
        column = 0
        list_s = []
        while column < 15:
            cell = self.tableWidget.item(row, column).text()
            column += 1
            list_s.append(cell)
        print(list_s)
        self.lineEdit_35.setText(list_s[0])
        self.lineEdit_32.setText(list_s[1])
        self.lineEdit_30.setText(list_s[2])
        self.lineEdit_27.setText(str(list_s[5]))
        self.lineEdit_26.setText(str(list_s[6]))
        self.comboBox_7.setCurrentText(list_s[3])
        self.dateEdit_12.setDate(datetime.datetime.strptime(list_s[4], '%Y-%m-%d').date())
        # dateEdit_12
        self.comboBox_packages_3.setCurrentText(list_s[7])
        self.comboBox_photographers_3.setCurrentText(list_s[11])
        self.lineEdit_33.setText(list_s[10])
        self.lineEdit_31.setText(list_s[8])
        self.lineEdit_28.setText(list_s[9])
        self.textEdit_7.setPlainText(list_s[12])
        self.textEdit_8.setPlainText(list_s[14])
        print(list_s[13])
        if list_s[13] == 'Yes':
            self.checkBox_15.setChecked(True)
        elif list_s[13] == 'No':
            self.checkBox_15.setChecked(False)

    def package_active_New(self):
        index = self.comboBox_packages.currentText()
        if index != '------------':
            self.cur.execute('''
                SELECT Name, Price, Banners, Frames, Photos, Albums FROM packages WHERE Name = %s''', [index])
            data = self.cur.fetchall()
            self.lineEdit_10.setText(str(data[0][1]))
            self.spinBox_5.setValue(data[0][2])
            self.spinBox_7.setValue(data[0][3])
            self.spinBox_6.setValue(data[0][4])
            self.spinBox_8.setValue(data[0][5])

        global original_price_new
        original_price_new = self.lineEdit_10.text()

    def package_active_Edit(self):
        index = self.comboBox_packages_3.currentText()
        if index != '------------':
            self.cur.execute('''
                SELECT Name, Price FROM packages WHERE Name = %s''', [index])
            data = self.cur.fetchall()
            self.lineEdit_31.setText(str(data[0][1]))

        global original_price_edit
        original_price_edit = self.lineEdit_31.text()

    def location_fee_New(self):
        if self.checkBox_14.isChecked():
            price = float(self.lineEdit_10.text()) + 500
            self.lineEdit_10.setText(str(price))
        elif not self.checkBox_14.isChecked():
            price = float(self.lineEdit_10.text()) - 500
            self.lineEdit_10.setText(str(price))

    def location_fee_Edit(self):          #ERROR + check package for edit
        if self.checkBox_15.isChecked():
            price = float(self.lineEdit_31.text()) + 500
            self.lineEdit_31.setText(str(price))
        elif not self.checkBox_15.isChecked():
            price = float(self.lineEdit_31.text()) - 500
            self.lineEdit_31.setText(str(price))

    def apply_discount(self):    # the discounts overlap
        index = self.comboBox_packages_2.currentIndex()
        if index == 1:
            price = int(original_price_new) * 0.95
            self.lineEdit_10.setText(str(price))
        elif index == 2:
            price = int(original_price_new) * 0.90
            self.lineEdit_10.setText(str(price))
        elif index == 3:
            price = int(original_price_new) * 0.85
            self.lineEdit_10.setText(str(price))
        elif index == 4:
            price = int(original_price_new) * 0.80
            self.lineEdit_10.setText(str(price))
        elif index == 0:
            if self.checkBox_14.isChecked():
                self.lineEdit_10.setText(str(int(original_price_new) + 500))
            else:
                self.lineEdit_10.setText(original_price_new)

    def enable_edit_order(self):
        self.lineEdit_32.setEnabled(True)
        self.lineEdit_30.setEnabled(True)
        self.lineEdit_27.setEnabled(True)
        self.lineEdit_26.setEnabled(True)
        self.comboBox_7.setEnabled(True)
        self.dateEdit_12.setEnabled(True)
        self.comboBox_packages_3.setEnabled(True)
        self.comboBox_photographers_3.setEnabled(True)
        self.lineEdit_28.setEnabled(True)
        self.textEdit_7.setEnabled(True)
        self.textEdit_8.setEnabled(True)
        self.checkBox_15.setEnabled(True)
        self.pushButton_20.setEnabled(True)
        self.pushButton_21.setEnabled(True)

    def update_remaining_New(self):
        price = self.lineEdit_10.text()
        down_payment = self.lineEdit_11.text()
        if down_payment == '':
            down_payment = 0
        else:
            pass
        remaining = float(price) - float(down_payment)
        self.lineEdit_36.setText(str(remaining))

    def update_remaining_Edit(self):
        price = self.lineEdit_31.text()
        down_payment = self.lineEdit_28.text()
        if down_payment == '':
            down_payment = 0
        else:
            pass
        remaining = float(price) - float(down_payment)
        self.lineEdit_33.setText(str(remaining))

# ############################################################
# #######PHOTOGRAPHERS####### HANDLE COOL STUFF ######PHOTOGRAPHERS#######
    def show_selected_photographer(self, mi):
        self.tabWidget_photographer.setCurrentIndex(1)
        row = mi.row()
        column = 0
        list_s = []
        while column < 6:
            cell = self.tableWidget_7.item(row, column).text()
            column += 1
            list_s.append(cell)
        print(list_s)

        self.lineEdit_47.setText(list_s[0])
        self.lineEdit_54.setText(list_s[1])
        self.lineEdit_56.setText(list_s[2])
        self.lineEdit_64.setText(list_s[3])
        self.lineEdit_65.setText(list_s[4])
        self.textEdit_5.setPlainText(list_s[5])

        #check edit save delete

# ############################################################
# HANDLE CALENDAR
    def catch_date(self):
        global date_calendar
        date_calendar = self.calendarWidget.selectedDate()
        date_sql = date_calendar.toString("yyyy/MM/dd")
        self.cur.execute('''
            SELECT o.id, o.Groom_name, p.Name, ph.Name
            FROM orders o
                JOIN packages p ON o.Package_id = p.id
                JOIN photographers ph ON o.Photographer_id = ph.id
                WHERE o.Event_Date = %s''', [date_sql])
        data = self.cur.fetchall()
        self.lcdNumber.display(len(data))
        self.tableWidget_11.setRowCount(0)
        self.tableWidget_11.insertRow(0)
        for row, order in enumerate (data):
            for col, item in enumerate (order):
                self.tableWidget_11.setItem(row,col, QTableWidgetItem(str(item)))
                col += 1
            row_position = self.tableWidget_11.rowCount()
            self.tableWidget_11.insertRow(row_position)

    def proceed_to_order(self):
        self.tabWidget.setCurrentIndex(4)
        self.tabWidget_order.setCurrentIndex(0)
        self.dateEdit_10.setDate(date_calendar)

    def show_full_order(self, mu):
        row = mu.row()
        column = 0
        cell = self.tableWidget_11.item(row, column).text()
        self.tabWidget.setCurrentIndex(4)
        self.tabWidget_order.setCurrentIndex(2)
        self.cur.execute('''SELECT * FROM orders WHERE id = %s''',[cell])
        data = self.cur.fetchone()
        self.lineEdit_35.setText(str(data[0]))
        self.lineEdit_32.setText(data[1])
        self.lineEdit_30.setText(data[2])
        self.lineEdit_27.setText(str(data[3]))
        self.lineEdit_26.setText(str(data[4]))
        self.comboBox_7.setCurrentText(data[5])
        self.dateEdit_12.setDate(data[6])
        self.comboBox_packages_3.setCurrentIndex(data[7])
        self.comboBox_photographers_3.setCurrentIndex(data[11])
        self.lineEdit_33.setText(str(data[10]))
        self.lineEdit_31.setText(str(data[8]))
        self.lineEdit_28.setText(str(data[9]))
        self.textEdit_7.setPlainText(str(data[12]))
        self.textEdit_8.setPlainText(str(data[14]))
        if data[13] == 'Yes':
            self.checkBox_15.setChecked(True)
        elif data[13] == 'No':
            self.checkBox_15.setChecked(False)


# #####################################################
# #################Controls tabs#######################
    def open_login_tab(self):
        self.tabWidget.setCurrentIndex(0)
        print('Login tab')

    def open_reset_password_tab(self):
        self.tabWidget.setCurrentIndex(2)
        print('Reset Password tab')

    def open_calender_tab(self):
        self.tabWidget.setCurrentIndex(3)
        print('Calendar tab')

    def open_new_order_tab(self):
        self.tabWidget.setCurrentIndex(4)
        self.tabWidget_order.setCurrentIndex(0)
        print('New Order tab')

    def open_deliveries_tab(self):
        self.tabWidget.setCurrentIndex(5)
        self.tabWidget_deliveries.setCurrentIndex(0)
        print('Deliveries tab')

    def open_reports_tab(self):
        self.tabWidget.setCurrentIndex(6)
        self.tabWidget_reports.setCurrentIndex(0)
        print('Reports tab')

    def open_photographers_tab(self):
        self.tabWidget.setCurrentIndex(8)
        self.tabWidget_photographer.setCurrentIndex(0)
        print('Photographers tab')

    def open_packages_tab(self):
        self.tabWidget.setCurrentIndex(9)
        print('Packages tab')

    def open_history_tab(self):
        self.tabWidget.setCurrentIndex(7)
        print('History tab')

    def open_statistics_tab(self):
        self.tabWidget.setCurrentIndex(10)
        print('Statistics tab')

    def open_settings_tab(self):
        self.tabWidget.setCurrentIndex(11)
        self.tabWidget_settings.setCurrentIndex(0)
        print('Settings tab')

    def open_main_menu_tab(self):
        self.tabWidget.setCurrentIndex(1)
        print('Main Menu tab')


# call loop app
def main():
    app = QApplication(sys.argv)
    window = Main()
    window.setGeometry(500, 200, 1012, 660)
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
