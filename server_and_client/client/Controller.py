from chat import *
from mainmenu import Mainmenu
from PyQt5 import QtWidgets
import socket
import threading

username = 'sami' + '\n'
s = socket.socket()
ip = '127.0.0.1'

port = 2021

s.connect((ip, port))

class Controller:
    def __init__(self, s, username):
        self.u = input() + '\n'
        self.s = s
        pass
    def show_mainmenu(self):
       
    
        self.Form = QtWidgets.QWidget()
        self.mainmenu = Mainmenu(self.Form)
       
        self.mainmenu.listWidget.itemClicked.connect(self.mainmenu.listwidgetclicked)
        self.mainmenu.listWidget.itemClicked.connect(self.show_chat)
        self.Form.show()
    def show_chat(self):
        
        self.Form = QtWidgets.QWidget()
        self.chat = chat_window(self.Form, self.s, self.u, self.mainmenu.group)
        self.chat.open_group(self.mainmenu.group)
        
        self.Form.show()
        print(1)
        recv = threading.Thread(target=self.chat.recv_m)
        recv.start()
        print(1240)
   






if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    ui = Controller(s, username)
    ui.show_mainmenu()

    
 
    sys.exit(app.exec_())
