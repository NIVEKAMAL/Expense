from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys



class Tablewidget(QDockWidget):

# This is is a subclass of a Dock Widget where a tableview can attach on it, which is in the main window.
    def __init__(self):
        super().__init__("Expenses")
        self.tableview = QTableView()
        self.setWidget(self.tableview)
      
        

    # This method is used to attach the model in the tableview.
    
    def set_model(self, model): 
        self.tableview.setModel(model)
       
    

       
      
      
   