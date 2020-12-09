

import sys

from PyQt5.QtWidgets import (QPushButton, QWidget,
                             QLineEdit, QApplication)
from PyQt5 import *
class Drop_button(QPushButton):

    def __init__(self, title, parent, ui):
        self.ui = ui
        self.parent = parent
        super().__init__(title, parent)
            

        self.setAcceptDrops(True)

    def dragEnterEvent(self, e):
        print('1')
##        self.hide()
        if e.mimeData().hasFormat('text/plain'):
            print('1')
            print(self.parent.geometry())
            self.setGeometry(QtCore.QRect(0, self.parent.height() // 2, self.parent.width(), self.parent.height() // 2))
            self.setText("Drop file here")
            print('2')
            
##            self.show()
            e.accept()
        else:
            e.ignore()

        

    def dropEvent(self, e):
        self.setGeometry(self.ui.image_attach.geometry())
      
        self.file = e.mimeData().text()
        self.file = self.file[7:-2]

