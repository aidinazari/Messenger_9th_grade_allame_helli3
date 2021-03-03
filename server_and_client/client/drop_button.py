

import sys

from PyQt5.QtWidgets import (QPushButton, QWidget,
                             QLineEdit, QApplication)
from PyQt5 import *
from threading import Thread
class Drop_button(QPushButton):

    def __init__(self, title, parent, ui):
        self.ui = ui
        self.parent = parent
        super().__init__(title, parent)
            

        self.setAcceptDrops(True)

    def dragEnterEvent(self, e):
    
##        self.hide()
        if e.mimeData().hasFormat('text/plain'):
 
            self.first_geometry = self.ui.image_attach.first_geometry
            self.setGeometry(QtCore.QRect(0, self.parent.height() // 2, self.parent.width(), self.parent.height() // 2))
            self.setText("Drop file here")
           
            
##            self.show()
            e.accept()
        else:
            e.ignore()

        

    def dropEvent(self, e):
        self.setGeometry(self.first_geometry)
        self.setText('I')
      
        self.file = e.mimeData().text()
        self.file = self.file[7:-2]

        thread = Thread(target=self.ui.send, args=('img',))
        thread.start()

        
        
        print('file draged succesfully')
