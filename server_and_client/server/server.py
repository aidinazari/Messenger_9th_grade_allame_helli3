# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!

from zipfile import ZipFile

import os

from os.path import basename

import pickle








def broadcast(msg, sender):
    global clients
    for i in clients:
        if i != sender:
            print(i, msg, '-----------')
            msg = pickle.dumps(msg)
            i.send(msg)








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
    done = False
    while not done:
        


     

    
        
        msg = conn.recv(1024)
        msg = pickle.loads(msg)
        print(msg)
        if len(msg) == 0:
            done = True
        elif msg[0] == 'chat':
            if msg[1] in chatlist:
                users = get_chatlist(msg[1], 'users.txt')
                print(users)
                if msg[3] in users:
                    print('start')
               
                    path = '/home/sami/Documents/Computer/server_and_client/server/files/' + str(msg[1]) + '/chat.txt'
                    f = open(path, 'rb')
                    

                    ln = sum(1 for i in open(path))
                   
                    if ln > int(msg[2]):
                        
                   
                        for i in range(int(msg[2])):
                            print(i)
                            a = f.readline()
                            
                        l = f.read()
                        
                        
                        while l:
                            conn.send(l)
                            l = f.read()
                    print('Done')  
                    conn.send('Done'.encode())
                    
                        
                           
                        
                       
                    f.close()
                    
                    print('Group updated succesfully')

        elif msg[0] == 'Attach':
            if msg[2] in chatlist:
                users = get_chatlist(msg[2], 'users.txt')
                print(users)
                if msg[1] in users:
                    if os.path.isfile(msg[3]):
                        print('go')
                        path = '/home/sami/Documents/Computer/server_and_client' + '/server/files/' + str(msg[2]) + '/'
                        
                        m = 'True'
                        conn.send(m.encode())
                        
                        filename = msg[3].split('/')
                        filename = filename[-1]

                        recv_file(path, filename)
                        
                        add_chat(msg[1] + ' ' + msg[0] + ' ' + filename + '\n', msg[2]) 




                                 
                    else:
                        conn.send('File name exists'.encode())
                else:
                    conn.send('You are not in group'.encode())
                    
            else:
                conn.send('group not found'.encode())
                
        
        elif msg[0] == 'recv':
            if msg[2] in chatlist:
                users = get_chatlist(msg[2], 'users.txt')
                print(users)
                if msg[1] in users:
                    path = '/home/sami/Documents/Computer/server_and_client/' + 'server/files/' + msg[2] + '/' + msg[3]
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
    loc = clients.index(conn)
    del clients[loc]




from PyQt5 import QtCore, QtGui, QtWidgets
import socket
import threading

s = socket.socket()
ip = '127.0.0.1'
port = 2020

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

        
    


    

    
