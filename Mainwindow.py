import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Docktablewidget import Tablewidget
from DateLineEdit import DateLineEdit

from controller import Controller

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.save_btn = QPushButton("Save")
        self.save_btn.setToolTip('save')

       
        self.date_label = QLabel('Date')
        self.date_label.setAlignment(Qt.AlignLeft)
        self.amount_label = QLabel('Amount')
        self.category_label = QLabel('Category')
        self.cb = QComboBox()
        self.cb.addItems(['Groceries', 'fruits', 'households', 'weekends', 'clothes', 'Extra'])
        #self.cb.currentIndexChanged.connect(self.selectionchange)
        self.icon = r'C:\Users\Nivetha\Desktop\Homework code\cal.png'
        self.date_lineedit = DateLineEdit(self.icon)
        
        self.amount_lineedit = QLineEdit()

        self.tablewidget = Tablewidget()
        self.list_wid = QListWidget()

        self.grid = QGridLayout()
        self.main_lay = QVBoxLayout()
        self.save_lay = QHBoxLayout()
        self.main_widget = QWidget()


       
        #self.label_lay.addWidget(self.save_btn)
        self.addDockWidget(Qt.RightDockWidgetArea, self.tablewidget)
        self.grid.addWidget(self.date_label, 1, 0)
        self.grid.addWidget(self.date_lineedit, 1, 1)
        self.grid.addWidget(self.amount_label, 4, 0)
        self.grid.addWidget(self.amount_lineedit, 4, 1)
        self.grid.addWidget(self.category_label, 6, 0)
        self.grid.addWidget(self.cb, 6, 1)

        self.save_lay.addWidget(self.save_btn)

        self.main_lay.addLayout(self.grid)
        self.main_lay.addLayout(self.save_lay)

        self.main_widget.setLayout(self.main_lay)

        self.setCentralWidget(self.main_widget)
        
        self.data_list = []
        self.initUI()



    def initUI(self):
        self.setWindowTitle("Main Dashbboard")
        self.setGeometry(0, 0, 800, 600)
        self.show()
        self.center()


    def center(self):
        frameGm = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())
        



    

            
        

        

    
        