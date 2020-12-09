# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!

from zipfile import ZipFile

import os

from os.path import basename









def broadcast(msg, sender):
    global clients
    for i in clients:
        if i != sender:
            i.send(msg.encode())






















def client(conn, s, clients):
    while True:
        print('start')
        chatf = open('chatlist.txt', 'r')
        chatlist = chatf.readlines()
        chatf.close()
        for i in range(len(chatlist)):
            
            if '\n' in chatlist[i]:
                chatlist[i] = chatlist[i][:-1]


     

    
        
        msg = conn.recv(1024).decode()
        print(msg)
        if msg.split()[0] == 'chat':
            if msg.split()[1] in chatlist:
               
                path = '/home/sami/Documents/Computer/server_and_client/server/files/' + str(msg.split()[1]) + '/chat.txt'
                f = open(path, 'rb')
                

                ln = sum(1 for i in open(path))
               
                if ln > int(msg.split()[2]):
                    
               
                    for i in range(int(msg.split()[2])):
                        print(i)
                        a = f.readline()
                        
                    l = f.read()
                    
                    
                    while l:
                        conn.send(l)
                        l = f.read()
                        
                    conn.send('Done'.encode())
                       
                    
                   
                f.close()
                print('Group updated succesfully')

        elif msg.split()[0] == 'img':
            if msg.split()[2] in chatlist:
                if os.path.isfile(msg.split()[3]):
                    path = '/home/sami/Documents/Computer/server_and_client/server/files/' + str(msg.split()[2]) + '/'
                    m = 'True'
                    conn.send(m.encode())
                    f = open(path + '/chatlist.txt', 'w')
                    f.write(msg.split()[1] + ' img ' + msg.split()[3])
                    f.close()
                    filename = msg.split()[3].split('/')
                    print(filename)
                    filename = filename[-1]
                    f = open(path + filename, 'wb')
                    print('so')
                    data = conn.recv(1024)
                    while data != 'done'.encode():
                        f.write(data)
                       
                        data = conn.recv(1024)

                    print('file sent succesfully')
                    
                else:
                    conn.send('File name exists')
            else:
                conn.send('group not found')
                
        
                    





        
        else:

            broadcast(msg, conn)
        




from PyQt5 import QtCore, QtGui, QtWidgets
import socket
import threading

s = socket.socket()
ip = '127.0.0.1'
port = 2021

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

        
    


    

    
