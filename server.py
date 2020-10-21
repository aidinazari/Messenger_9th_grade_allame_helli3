# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!
def broadcast(msg, sender):
    global clients
    for i in clients:
        if i != sender:
            i.send(msg.encode())

def client(conn, s, clients):
    while True:
        print('start')
        msg = conn.recv(1024).decode()
        print(msg)
        broadcast(msg, conn)
        
from PyQt5 import QtCore, QtGui, QtWidgets
import socket
import threading
s = socket.socket()
ip = '127.0.0.1'
port = 1233
s.bind((ip, port))
s.listen()
clients = []
print('waiting for connection', ip, port)
while True:
    conn, addr = s.accept()
    print(conn, addr)
    clients += [conn]
    thread = threading.Thread(target=client, args=(conn, s, clients))
    thread.start()

        
    


    

    
