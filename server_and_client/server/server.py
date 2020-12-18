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
            print(i, msg, '-----------')
            i.send(msg.encode())








def send_file(path):
    f = open(path, 'rb')
    print(path)
    data = f.read(1024)
    while data:
        conn.send(data)
        data = f.read(1024)
    conn.send('done'.encode())
    f.close()
    print('file sent succesfully')
    


def recv_file(path, filename):
    f = open(path + filename, 'wb')
                  
    data = conn.recv(1024)

    while data[-4:] != 'done'.encode():
                           
        f.write(data)               
        data = conn.recv(1024)
                    
                       
    data = data[:-4]
    f.write(data)

    print('file recvied succesfully')
    f.close()






def add_chat(msg, group):
    f = open('/home/sami/Documents/Computer/server_and_client/server/files/' + group + '/chat.txt', 'a')
    f.write(msg )
    f.close()




def get_chatlist(group, file):
    path = './'
    if str(group) != 'False':
        path += 'files/' + group + '/' + file
    else:
        path += file
    chatf = open(path, 'r')
    chatlist = chatf.readlines()
    chatf.close()
    for i in range(len(chatlist)):
            
        if '\n' in chatlist[i]:
            chatlist[i] = chatlist[i][:-1]
    return chatlist
    
        


def client(conn, s, clients):
    print('start')
    chatlist = get_chatlist(False, 'chatlist.txt')
    print(chatlist)
    while True:
        


     

    
        
        msg = conn.recv(1024).decode()
        print(msg)
        if msg.split()[0] == 'chat':
            if msg.split()[1] in chatlist:
                users = get_chatlist(msg.split()[1], 'users.txt')
                print(users)
                if msg.split()[3] in users:
               
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

        elif msg.split()[0] == 'Attach':
            if msg.split()[2] in chatlist:
                users = get_chatlist(msg.split()[2], 'users.txt')
                print(users)
                if msg.split()[1] in users:
                    if os.path.isfile(msg.split()[3]):
                        print('go')
                        path = '/home/sami/Documents/Computer/server_and_client' + '/server/files/' + str(msg.split()[2]) + '/'
                        
                        m = 'True'
                        conn.send(m.encode())
                        
                        filename = msg.split()[3].split('/')
                        filename = filename[-1]

                        recv_file(path, filename)
                        
                        add_chat(msg.split()[1] + ' ' + msg.split()[0] + ' ' + filename + '\n', msg.split()[2]) 




                                 
                    else:
                        conn.send('File name exists'.encode())
                else:
                    conn.send('You are not in group'.encode())
                    
            else:
                conn.send('group not found'.encode())
                
        
        elif msg.split()[0] == 'recv':
            if msg.split()[2] in chatlist:
                users = get_chatlist(msg.split()[2], 'users.txt')
                print(users)
                if msg.split()[1] in users:
                    path = '/home/sami/Documents/Computer/server_and_client/' + 'server/files/' + msg.split()[2] + '/' + msg.split()[3]
                    if os.path.isfile(path):
                        print('-----------')
                        conn.send('True'.encode())
                        send_file(path)
                    

                    
                    else:
                        conn.send('File name exists'.encode())
                else:
                    conn.send('You are not in group'.encode())
                        
            else:
                conn.send('group not found'.encode())





        
        else:
            print(msg)
            msg = msg[4:]
            broadcast(msg, conn)
        




from PyQt5 import QtCore, QtGui, QtWidgets
import socket
import threading

s = socket.socket()
ip = '127.0.0.1'
port = 2025

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

        
    


    

    
