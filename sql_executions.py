import mysql.connector

class Database:
    def __init__(self):
        self.db = mysql.connector.connect(
            host='localhost',
            user='root',
            password='macrun96',
            db='studio_app_2'
        )
        self.cur = self.db.cursor()
        print('Connected to Database')





