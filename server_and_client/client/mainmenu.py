# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window (another copy).ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!

from get_path_infor import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QBrush, QImage, QPainter, QPixmap, QWindow
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget

class Widget(QWidget):
    def __init__ (self, parent = None):
        super(Widget, self).__init__(parent)
        self.textQVBoxLayout = QVBoxLayout()
        self.textUpQLabel    = QLabel()
        self.textDownQLabel  = QLabel()
        self.textQVBoxLayout.addWidget(self.textUpQLabel)
        self.textQVBoxLayout.addWidget(self.textDownQLabel)
        self.allQHBoxLayout  = QHBoxLayout()
        self.iconQLabel      =  QLabel()
        self.allQHBoxLayout.addWidget(self.iconQLabel, 0)
        self.allQHBoxLayout.addLayout(self.textQVBoxLayout, 1)
        self.setLayout(self.allQHBoxLayout)
        
        
        # setStyleSheet
        self.textUpQLabel.setStyleSheet('''
            color: rgb(0, 0, 0);
        ''')
        self.textDownQLabel.setStyleSheet('''
            color: rgb(64, 64, 64);
        ''')

    def setTextUp (self, text):
        self.textUpQLabel.setText(text)

    def setTextDown (self, text):
        self.textDownQLabel.setText(text)

    def setIcon (self, imagePath):
        pixmap = QtGui.QPixmap(imagePath)
        pixmap = pixmap.scaled(64, 64, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.iconQLabel.setPixmap(pixmap)
    


class Mainmenu(object):
    def __init__(self, Form):
        self.bk = bk
        self.start_file = start_file
        Form.setObjectName("Form")
        Form.resize(701, 545)
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(30, 80, 621, 451))
        self.listWidget.setObjectName("listWidget")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(30, 10, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(30, 50, 301, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(350, 50, 89, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.update_list()
        self.listWidget.itemClicked.connect(self.listwidgetclicked)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Setting"))
        self.pushButton_2.setText(_translate("Form", "search"))
    def update_list(self):
        chatlist = self.read_chats(False, 'groups.txt')
        for i in chatlist:
            path = self.start_file 
            lastchat = self.read_chats(i, 'chat.txt')
            lastchat = lastchat[-1]
            self.add_widget(path + self.bk + 'files' + self.bk + i + self.bk + 'dependents' + self.bk + 'icon.png', i, lastchat)
    def read_chats(self, group, file):
        path = self.start_file + self.bk
        if str(group) != 'False':
            path += 'files' + self.bk + group + self.bk + file
        else:
            path += file
        chatf = open(path, 'r')
        chatlist = chatf.readlines()
        chatf.close()
        for i in range(len(chatlist)):
                
            if '\n' in chatlist[i]:
                chatlist[i] = chatlist[i][:-1]
        return chatlist
    def listwidgetclicked(self, item):
        self.group = item.group

    
    def add_widget(self, icon, name, index):
        myQCustomQWidget = Widget()
        myQCustomQWidget.setTextUp(name)
        myQCustomQWidget.setTextDown(index)
        myQCustomQWidget.setIcon(icon)
        # Create QListWidgetItem
        item = QtWidgets.QListWidgetItem(self.listWidget)
        # Set size hint
        item.setSizeHint(myQCustomQWidget.sizeHint())
        item.group = name
        # Add QListWidgetItem into QListWidget
        self.listWidget.addItem(item)
        self.listWidget.setItemWidget(item, myQCustomQWidget)
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Mainmenu(Form)

    Form.show()
 
    sys.exit(app.exec_())
