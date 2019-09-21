import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import Mainwindow
from TableModel import TableModel
from sqlite import ExpenseDatabase



class Controller():

    def __init__(self):
        self.database =  ExpenseDatabase()
        self.win = Mainwindow.MainWindow()
        
        print(self.win)

        self.win.save_btn.clicked.connect(self.data_to_database)


    def data_to_database(self):
        date = self.win.date_lineedit.text()
        amount = float(self.win.amount_lineedit.text())
        category = self.win.cb.currentText()

        self.database.insert_data(date, amount, category)
        table_list = self.database.select_query()
        self.model = TableModel(table_list)
        self.win.tablewidget.set_model(self.model)


    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    con = Controller()
    sys.exit(app.exec_())

