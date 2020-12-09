# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import socket
import threading
from zipfile import ZipFile
import os
from recording_voice import *
from easygui import msgbox
import threading
import time
from tkinter.filedialog import askopenfilename
from playsound import playsound
from drop_button import Drop_button
from PyQt5.QtWidgets import  QMessageBox



##username = input() + '\n'
username = 'x' + '\n'
s = socket.socket()
ip = '127.0.0.1'

port = 2021

s.connect((ip, port))


class window(object):
    def setupUi(self, Form, s, username):
        self.s = s
        self.u = username
        self.group = 's'
        self.count = -1
        Form.setObjectName("Form")
        Form.resize(474, 300)

        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(30, 30, 411, 221))
        self.listWidget.setObjectName("listWidget")
        
        self.bsend = QtWidgets.QPushButton(Form)
        self.bsend.setGeometry(QtCore.QRect(370, 260, 61, 25))
        self.bsend.setObjectName("bsend")
        
        self.sbox = QtWidgets.QLineEdit(Form)
        self.sbox.setGeometry(QtCore.QRect(30, 260, 261, 25))
        self.sbox.setObjectName("sbox")

        self.Voice_record = QtWidgets.QPushButton(Form)
        self.Voice_record.setGeometry(QtCore.QRect(300, 260, 31, 25))
        self.Voice_record.setObjectName("Voice_record")

        self.image_attach = Drop_button('Button', Form, self)
        self.image_attach.setGeometry(QtCore.QRect(340, 260, 21, 25))
        self.image_attach.setObjectName("image_attach")
        self.image_attach.file = '/home/sami/Pictures/download.png'
        

        self.Lrecording = QtWidgets.QLabel(Form)
        self.Lrecording.setGeometry(QtCore.QRect(30, 260, 81, 17))
        self.Lrecording.setObjectName("Lrecording")
        self.Lrecording.hide()
        
        self.Stop_recording = QtWidgets.QPushButton(Form)
        self.Stop_recording.setGeometry(QtCore.QRect(340, 260, 89, 25))
        self.Stop_recording.setObjectName("Stop_recording")
        self.Stop_recording.hide()

   

        
        self.retranslateUi(Form)
        

        self.bsend.clicked.connect(lambda : self.send('msg'))
        self.Voice_record.clicked.connect(self.Show_recording)
##        self.Voice_record.clicked.connect(self.record_audio)
        self.image_attach.clicked.connect(self.Image_path)
        self.Stop_recording.clicked.connect(self.Hide_recording)

        
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        

    def retranslateUi(self, Form):
     
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.bsend.setText(_translate("Form", "send"))
        self.Voice_record.setText(_translate("Form", "V"))
        self.image_attach.setText(_translate("Form", "I"))
        self.Lrecording.setText(_translate("Form", "Recording..."))
        self.Stop_recording.setText(_translate("Form", "Stop"))




    def show_error(self, text):
        
        
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Error")

        msg.setInformativeText(text)
        msg.setWindowTitle("Error")
        msg.exec_()

    def send_file(self, file):
        f = open(file, 'rb')
        data = f.read(1024)
        while data:
            print(data)
            self.s.send(data)
            data = f.read(1024)
        self.s.send('done'.encode())
        f.close()
        print('file sent succesfully')
        
    def send(self, Type):
        
        if Type == 'msg':
            if self.sbox.text() != '':
                msg = 'msg' + self.u + self.sbox.text()
                self.s.send(msg.encode())
                self.add_chat('msg', 'You\n' + self.sbox.text(), True)
                self.sbox.setText('')
                
        if Type == 'img':
            if os.path.isfile(self.image_attach.file):
                print('go')
                msg = 'img ' + self.u[:-1] + ' ' + self.group + ' ' + self.image_attach.file
                
                self.s.send(msg.encode())
                nat = self.s.recv(1024).decode()
                if nat == 'True':
                
                    self.send_file(self.image_attach.file)
                else:
                    self.show_error(nat)
                    return False
                self.add_chat('img', 'You\n' + self.image_attach.file, True)
        

            
    def add_chat(self, Type, msg, me):
        global Form
        if Type == 'msg':
            self.count += 1
            item = QtWidgets.QListWidgetItem()
            if me == True:
                item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
            self.listWidget.addItem(item)
            _translate = QtCore.QCoreApplication.translate
            item = self.listWidget.item(self.count)
            
            item.setText(_translate("Form", msg))

        if Type == 'img':
            f = 1
            

    
    def recv_m(self):    
        while True:
            msg = self.s.recv(1024).decode()
            self.add_chat(msg, False)





            
    def open_group(self, name):
        print('start recving file')
        
        path = '/home/sami/Documents/Computer/server_and_client/client/files/' + str(name) + '/chat.txt'
        if not os.path.isfile(path):
            print("Doesnot group exist")
            return 0
        
        f = open(path, 'ab')
        

        ln = sum(1 for i in open(path))
        
        

        msg = 'chat ' + name + ' ' + str(ln)

        

        self.s.send(msg.encode())
        print('msg sent')

        

        data = self.s.recv(1024)
        print(data, 4)
        while data != b'Done':            
            f.write(data)
            print(3)
            data = self.s.recv(1024)
            print(data == True)
            print(data)


        f.close()
            
        print('file sent succesfully')

    def Record_audio(self):
        print('so')
##        filename = msgbox(msg=('write your file name'), title = "filename")
        filename = 'test'
        
        self.record_audio = record_audio('./' + self.group + '/' + filename)
        self.record_audio.start()
    def Show_recording(self, Form):
        
        self.Stop_recording.show()
        self.Lrecording.show()

        self.Voice_record.hide()
        self.sbox.hide()
        self.bsend.hide()
        self.image_attach.hide()
        thread = threading.Thread(target=self.Record_audio)
        thread.start()
##        self.retranslateUi(Form)
      
      
        print('hi')

    def Hide_recording(self):

        self.Voice_record.show()
        self.sbox.show()
        self.bsend.show()
        self.image_attach.show()

        self.Stop_recording.hide()
        self.Lrecording.hide()
        
        

        print(self.record_audio.stop)
        self.record_audio.stop = True










    def Image_path(self):
        file = askopenfilename()
        print(file)
        self.image_attach.file = file
        self.send('img')










        
    def playsound(self, file):
        
        playsound(file)




    def add_widget(self):
        itemN = QtWidgets.QListWidgetItem()
        # Create widget
        widget = QtWidgets.QWidget()
        widgetText = QtWidgets.QLabel("")
        widgetText.setPixmap(QtGui.QPixmap(file))
       
        widgetLayout = QtWidgets.QHBoxLayout()
    
        widgetLayout.addWidget(widgetText)
      
        widgetLayout.addStretch()

        widgetLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        widget.setLayout(widgetLayout)
        itemN.setSizeHint(widget.sizeHint())


        self.listWidget.addItem(itemN)
        self.listWidget.setItemWidget(itemN, widget)








        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = window()
    ui.setupUi(Form, s, username)
    ui.send('img')
    
    Form.show()
 
    recv = threading.Thread(target=ui.recv_m)
    recv.start()
    sys.exit(app.exec_())

