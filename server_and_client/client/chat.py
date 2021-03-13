# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!

from get_path_infor import *
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
import magic
from show_movie import VideoPlayer
import pickle
import datetime  
    







class chat_window(object):
    
        
    def __init__(self, Form, s, username, group):
     
        self.start_file = start_file
        self.stop_recv = False
        self.s = s
        self.u = username
        self.group = group
        self.count = -1
        Form.setObjectName("Form")
        Form.resize(474, 300)
        self.bk = bk


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

        self.attach_file = Drop_button('Button', Form, self)
        self.attach_file.setGeometry(QtCore.QRect(340, 260, 21, 25))
        self.attach_file.setObjectName("attach_file")
        self.attach_file.first_geometry = QtCore.QRect(340, 260, 21, 25)
       

        
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
        self.attach_file.clicked.connect(self.Image_path)
        self.Stop_recording.clicked.connect(self.Hide_recording)

        
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        

    def retranslateUi(self, Form):
     
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.bsend.setText(_translate("Form", "send"))
        self.Voice_record.setText(_translate("Form", "V"))
        self.attach_file.setText(_translate("Form", "A"))
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
    
            self.s.send(data)
            data = f.read(1024)
        self.s.send('done'.encode())
        f.close()
        print('file ', file, ' sent succesfully')
   
        
    def send(self, Type):
        self.stop_recv = True
        if Type == 'msg':
            if self.sbox.text() != '':
                msg = 'msg' + ' ' + self.u + ' ' + self.sbox.text()
             

                self.s.send(msg.encode())
                self.add_chat('msg', 'You\n' + self.sbox.text(), True)
                self.sbox.setText('')
        
                
        elif Type == 'Attach':
            
        
            if os.path.isfile(self.attach_file.file):
                
                Format = magic.from_file(self.attach_file.file, mime='True')
                
                Format = Format.split(self.bk)[0]
                
                current_time = str(datetime.datetime.now())
                current_time = current_time.split()
                current_time = current_time[0] + '_' + current_time[1] + '.' + self.attach_file.file.split('.')[-1]
             
                msg = 'Attach' + ' ' + self.u[:-1] + ' ' + self.group + ' ' + current_time + ' ' + Format
                
                          
                self.s.send(msg.encode())
                nat = self.s.recv(1024).decode()
            
                if nat == 'True':
                
                    self.send_file(self.attach_file.file)
                else:
                    self.show_error(nat)
                    return False
                
                self.add_chat(Format, 'You\n' + self.attach_file.file, True)
        
        self.stop_recv = False        

            
    def add_chat(self, Type, msg, me):
        global Form
       
        
        if Type == 'msg':
            self.add_msg_chat(msg, me)
            

        if Type == 'video':
            
            self.add_chat('msg', msg.split('\n')[0], me) 
            self.add_video(msg.split('\n')[1], me)

        elif Type == 'image':
            
            self.add_chat('msg', msg.split('\n')[0], me) 
            self.add_image(msg.split('\n')[1], me)
            
            
    def add_msg_chat(self, msg, me):
     
        self.count = self.listWidget.count() 
        item = QtWidgets.QListWidgetItem()
        if me == True:
            item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.listWidget.addItem(item)
        _translate = QtCore.QCoreApplication.translate
        item = self.listWidget.item(self.count)
            
        item.setText(_translate("Form", msg))
    
    def recv_m(self):
    
        while True:
    
            while not self.stop_recv:
                msg = self.s.recv(1024).decode()
                msg = msg.split(' ')
                print(msg, 'recieved')
                print('____________________________________')
                if msg[0] == 'update-group':
                    self.stop_recv = True
                    print('start updating group')
                    self.open_group('s')
                    
                    
                    self.stop_recv = False

                    print('updated------------------------------------------------------------------')
                else:
                    nat = ''
                    for i in msg[1:]:
                        nat += i + ' '
                        
                    self.add_chat(msg[0], nat, False)
                
                    


    def recv_file(self, path):
        f = open(path, 'wb')
   
        data = self.s.recv(1024)
        while data[-4:] != 'done'.encode():

            f.write(data)
            data = self.s.recv(1024)
          
        
        data = data[:-4]
        f.write(data)

        f.close()
        print('file ', path, ' recieved succesfully')



    def read_chats(self, group, file):
        path = self.start_file 
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
        

    def update_chats(self):
        self.stop_recv = True
        chats = self.read_chats(self.group, 'chat.txt')
       
        for i in chats:
       
            self.update_listwidget(i)
       
        self.stop_recv = False
            
    def update_listwidget(self, i):
        i = i.split()
        me = False
     
        if i[0] == self.u[:-1]:
            me = True
        if i[1] == 'Attach':
            path = self.start_file  + 'files' + self.bk + self.group + self.bk + i[2]
           
            if not os.path.isfile(path):
               
                msg = 'recv' + ' ' + self.u[:-1] + ' ' + self.group + ' ' + i[2]           
                self.s.send(msg.encode())        
                nat = self.s.recv(1024).decode()
                if nat == 'True':
                    self.recv_file(path)
                else:
                    self.show_error(nat)
                    return 0
                
            path = self.start_file + 'files' + self.bk + self.group + self.bk + i[2] 
            Format = magic.from_file(path, mime='True')
                
            Format = Format.split(self.bk)[0]
            if me == True:
                i[0] = 'You'
            print(Format, i[0] + '\n' + path, '---------------------Format')
            self.add_chat(Format, i[0] + '\n' + path, me)
        elif i[1] == 'msg':
            self.add_chat('msg', i[0] + '\n' + msg, me)

               
        
        
    def open_group(self, name):

        self.listWidget.clear()
        self.stop_recv = True
        
        path = self.start_file + 'files' + self.bk + str(name) + self.bk + 'chat.txt'
        if not os.path.isfile(path):
       
            return 0
        
        f = open(path, 'ab')
        

        ln = sum(1 for i in open(path))
        
        

        msg = 'chat' + ' ' + name + ' ' + str(ln) + ' ' + self.u[:-1]

        

        self.s.send(msg.encode())


        

        data = self.s.recv(1024)
    
        while data != b'done':            
            f.write(data)
      
            data = self.s.recv(1024)
            


        f.close()
            

        self.stop_recv = False
        self.update_chats()


    def Show_recording(self, Form):
        
        self.Stop_recording.show()
        self.Lrecording.show()

        self.Voice_record.hide()
        self.sbox.hide()
        self.bsend.hide()
        self.attach_file.hide()
        thread = threading.Thread(target=self.Record_audio)
        thread.start()

      
      
      

    def Hide_recording(self):

        self.Voice_record.show()
        self.sbox.show()
        self.bsend.show()
        self.attach_file.show()

        self.Stop_recording.hide()
        self.Lrecording.hide()
        
        

      
        self.record_audio.stop = True










    def Image_path(self):
        file = askopenfilename()
     
        self.attach_file.file = file
        self.send('Attach')










        
    def playsound(self, file):
        
        playsound(file)




    def add_image(self, file, me):
        print(self.listWidget.count(), 'count', self.count)
        self.count = self.listWidget.count()
        itemN = QtWidgets.QListWidgetItem()
        if me == True:
            itemN.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)

        # Create widget
        widget = QtWidgets.QWidget()
        widgetLabel = QtWidgets.QLabel("")
        
        print(file)
        widgetLabel.setPixmap(QtGui.QPixmap(file))
      
        
        widgetLayout = QtWidgets.QHBoxLayout()
        if me == True:
            widgetLayout.addWidget(widgetLabel, alignment=QtCore.Qt.AlignRight)
        else:
            widgetLayout.addWidget(widgetLabel)
            
            
      
        
        print(1)
##        widgetLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        widget.setLayout(widgetLayout)
        itemN.setSizeHint(widget.sizeHint())

        self.listWidget.addItem(itemN)
        self.listWidget.setItemWidget(itemN, widget)
        print('done')
     
        
    def add_video(self, filepath, me):
        self.count = self.listWidget.count()
        widget = QtWidgets.QWidget()
        itemN = QtWidgets.QListWidgetItem(self.listWidget)
        if me == True:
            itemN.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)


    


        
            
        player = VideoPlayer(filepath)
    
        
      
        
       
    
      
        itemN.setSizeHint(QtCore.QSize(300, 200))


        self.listWidget.addItem(itemN)
        self.listWidget.setItemWidget(itemN, player)
        

    def get_users(self):
        self.users = []
        msg = 'get_users' + ' ' + self.group
        self.s.send(msg.encode())
        nat = self.s.recv(1024).decode()
        if nat == 'True':
            users = self.s.recv(1024).decode()
            users = pickle.loads(users)
            return 1
        else:
            self.show_error(nat)
            return 0

##    def get_user_info(self, u):
##        msg = 'get_user_info' + ' ' + u
##        inf = []
##        icon_name = self.s.recv(1024).decode()
##        path = self.start_file + 'files' + self.bk + self.group + self.bk + 'users_info' + self.bk + icon_name
##        inf = [path]
##        self.recv_file(path)
##
##        bio = self.s.recv(1024).decode()
##        inf = [path, bio]
        
        
        
        
        
       
        



    



        

if __name__ == "__main__":
    import sys
##    username = input() + '\n'
    username = 'sami\n'
    s = socket.socket()
    ip = '127.0.0.1'

    port = 12346

    s.connect((ip, port))
    
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = chat_window(Form, s, username, 's')
    ui.open_group('s')
    
    Form.show()
 
    recv = threading.Thread(target=ui.recv_m)
    recv.start()
    sys.exit(app.exec_())

