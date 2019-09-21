import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *



class DateLineEdit(QLineEdit):

    def __init__(self, icon):
        super().__init__()

        self.icon = icon
        self.cal_but = QToolButton(self)
        self.cal_but.setIcon(QIcon(self.icon))
        self.cal_but.clicked.connect(self.showcalwidget)
        self.cal_but.setCursor(Qt.ArrowCursor)

       
    def showcalwidget(self):
        self.calendar = QCalendarWidget()
        self.calendar.setMinimumDate(QDate(1900, 1, 1))
        self.calendar.setMaximumDate(QDate(3000, 1, 1))
        self.calendar.setGridVisible(True)
        self.calendar.clicked.connect(self.updateDate)
        self.calendar.setWindowFlags(Qt.FramelessWindowHint)
        self.calendar.setStyleSheet('background: white; color: black')
        self.calendar.setGridVisible(True)
        pos = QCursor.pos()
        self.calendar.setGeometry(pos.x(), pos.y(),300, 200)
        self.calendar.show()

    def updateDate(self,*args):
        getDate = self.calendar.selectedDate().toString()
        self.setText(getDate)
        self.calendar.deleteLater()
        #print(self.text())
        
