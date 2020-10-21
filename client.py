# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import socket
import threading
username = input() + '\n'
s = socket.socket()
ip = '127.0.0.1'
port = 1233
s.connect((ip, port))


class Ui_Form(object):
    def setupUi(self, Form, s, username):
        self.s = s
        self.u = username
        self.count = -1
        Form.setObjectName("Form")
        Form.resize(400, 300)

        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(30, 30, 331, 221))
        self.listWidget.setObjectName("listWidget")

        self.bsend = QtWidgets.QPushButton(Form)
        self.bsend.setGeometry(QtCore.QRect(308, 260, 61, 25))
        self.bsend.setObjectName("send")

        self.sbox = QtWidgets.QLineEdit(Form)
        self.sbox.setGeometry(QtCore.QRect(30, 260, 261, 25))
        self.sbox.setObjectName("sbox")

        self.bsend.clicked.connect(self.send)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.bsend.setText(_translate("Form", "send"))
        
    def send(self):
        if self.sbox.text() != '':
            msg = self.u + self.sbox.text()
            self.s.send(msg.encode())
            self.add_chat('You\n' + self.sbox.text(), True)
            self.sbox.setText('')
    def add_chat(self, msg, me):
        global Form
        self.count += 1
        item = QtWidgets.QListWidgetItem()
        if me == True:
            item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.listWidget.addItem(item)
        _translate = QtCore.QCoreApplication.translate
        item = self.listWidget.item(self.count)
        
        item.setText(_translate("Form", msg))
    
    def recv_m(self):
        
        while True:
            msg = self.s.recv(1024).decode()
            self.add_chat(msg, False)
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form, s, username)
    Form.show()
    recv = threading.Thread(target=ui.recv_m)
    recv.start()
    sys.exit(app.exec_())

