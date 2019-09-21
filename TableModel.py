from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QAbstractTableModel
from PyQt5.QtGui import *
import sys

#Model
class TableModel(QAbstractTableModel):

    def __init__(self,data_list):
        super().__init__()
        self.data_list = data_list
        #header_label = ['Date', 'Amount', 'Category']
        #self.setHeaderData(0, Qt.Horizontal, Qt.AlignJustify, Qt.TextAlignmentRole)
    
    def rowCount(self, parent=None, *args, **kwargs):
        return len(self.data_list)

    def columnCount(self, parent=None, *args, **kwargs):
        return 3

    def data(self, idx, role=None):
        i = idx.row()
        if (idx.column() == 0 and  role == Qt.DisplayRole):
            return self.data_list[i][0]


        if (idx.column() == 1 and role == Qt.DisplayRole):
            return self.data_list[i][1]

        if (idx.column() == 2 and role == Qt.DisplayRole ):
           
            return self.data_list[i][2]

        else:
          
            return None
