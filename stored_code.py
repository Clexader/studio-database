# def search_order_intab(self):
#     order = self.lineEdit_103.text()
#     index = self.comboBox_4.currentIndex()
#
#     try:
#         if index == 1:
#             self.cur.execute('''SELECT * FROM orders WHERE id = %s''', [order])
#         elif index == 2:
#             self.cur.execute('''SELECT * FROM orders WHERE Groom_Name = %s''', [order])
#         elif index == 3:
#             self.cur.execute('''SELECT * FROM orders WHERE Bride_Name = %s''', [order])
#         elif index == 4:
#             self.cur.execute('''SELECT * FROM orders WHERE Phone_Number = %s''', [order])
#         elif index == 5:
#             self.cur.execute(f'''SELECT * FROM orders WHERE Event_Date = %s''', [order])
#         else:
#             QMessageBox.warning(self, 'Search error', 'Choose search filter!')
#
#         data = self.cur.fetchall()
#         self.lineEdit_35.setText(str(data[0][0]))
#         self.lineEdit_32.setText(data[0][1])
#         self.lineEdit_30.setText(data[0][2])
#         self.lineEdit_27.setText(data[0][3])
#         self.lineEdit_26.setText(data[0][4])
#         self.comboBox_7.setCurrentIndex(int(data[0][5]))  # call date in dateedit
#         self.lineEdit_34.setText(str(data[0][6]))
#         self.comboBox_packages_3.setCurrentIndex(int(data[0][7]))
#         self.lineEdit_31.setText(str(data[0][8]))
#         self.lineEdit_28.setText(str(data[0][9]))
#         self.lineEdit_33.setText(str(data[0][10]))
#         self.comboBox_photographers_3.setCurrentIndex(int(data[0][11]))
#         self.textEdit_7.setPlainText(data[0][12])
#         self.textEdit_8.setPlainText(data[0][13])
#     except IndexError:
#         QMessageBox.information(self, 'No match found', f'{order} not found')
#
#     self.statusBar().showMessage('Search Done!')
#     print('Search Done!')
#
#
# def search_photographer_intab(self):
#     search = self.lineEdit_104.text()
#
#     self.cur.execute('''SELECT * FROM photographers WHERE Name = %s''', [search])
#     data = self.cur.fetchall()
#
#     self.lineEdit_60.setText(data[0][1])
#     self.lineEdit_59.setText(data[0][2])
#     self.lineEdit_66.setText(data[0][3])
#     self.lineEdit_67.setText(data[0][4])
#     self.textEdit_9.setPlainText(data[0][5])
#
#     self.statusBar().showMessage('Search Done!')
#     print('Search Done!')