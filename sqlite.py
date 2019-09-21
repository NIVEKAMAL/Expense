import sqlite3


class ExpenseDatabase():

    def __init__(self):
        self.sqlite_connection = sqlite3.connect('SQLite Python.db')
        self.cursor = self.sqlite_connection.cursor()
        check = self.check_table_name()
        if len(check) == 0:
            create_query = """ CREATE TABLE Expense_table (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                buying_date datetime,
                                amount REAL NOT NULL,
                                category TEXT NOT NULL);"""
            self.cursor.execute(create_query)
        else:
            print('Database and table are already created')   

    def insert_data(self, date, amount, category):

        sql_insert_query = """INSERT INTO 'Expense_table'
                          ('buying_date','amount', 'category') 
                          VALUES (?, ?, ?);"""
        data_tuple = (date, amount, category)
        self.cursor.execute(sql_insert_query, data_tuple)
        self.sqlite_connection.commit()

    def select_query(self):

        sql_select_query = """SELECT * from Expense_table"""
        self.cursor.execute(sql_select_query)
        records = self.cursor.fetchall()
        return records


        
            

    def update_table(self, id, amount):
        sql_update_query = """ Update Expense_table set amount = ? where id = ? """

        data_tuple = (id, amount)
        self.cursor.execute(sql_update_query, data_tuple)
        self.sqlite_connection.commit()


    def delete_table(self, id):

        sql_delete_query =  """DELETE from Expense_table where id = ?"""

        
        self.cursor.execute(sql_delete_query, (id,))
        self.sqlite_connection.commit()

    def check_table_name(self):
        sql_table_name = '''SELECT name FROM sqlite_master WHERE type =  'table' AND name = 'Expense_table' ''' 
        record = self.cursor.execute(sql_table_name)
        return record.fetchall()
         





