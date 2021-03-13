# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!

from get_path_infor import *

from zipfile import ZipFile

import os

from os.path import basename

import pickle










def broadcast(msg, sender):
    global clients
    for i in clients:
        if i != sender:
            
            i.send(msg.encode())
            print(msg, 'sent')








def send_file(path):
    f = open(path, 'rb')
  
    data = f.read(1024)
    while data:
        conn.send(data)
        data = f.read(1024)

    conn.send('done'.encode())
    f.close()
    print('file', path, ' sent succesfully')
 
    


def recv_file(path, filename):
    print(path + filename)
    f = open(path + filename, 'wb')
                  
    data = conn.recv(1024)

    while data[-4:] != 'done'.encode():
                           
        f.write(data)               
        data = conn.recv(1024)
                    
                       
    data = data[:-4]
    f.write(data)


    f.close()
    print('file', path, ' recieved succesfully')






def add_chat(msg, group):
    f = open(start_file + 'files' + bk + group + bk + 'chat.txt', 'a')
    f.write(msg )
    f.close()




def get_chatlist(group, file):
    path = start_file
    if str(group) != 'False':
        path += 'files' + bk + group + bk + file
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

    chatlist = get_chatlist(False, 'chatlist.txt')

    done = False
    while not done:
        


     

    
        
        __msg = conn.recv(1024).decode()
        msg = __msg.split()
        
        if len(msg) == 0:
            done = True
        elif msg[0] == 'chat':
            if msg[1] in chatlist:
                users = get_chatlist(msg[1], 'users.txt')
                
                if msg[3] in users:
             
               
                    path = start_file + 'files' + bk + str(msg[1]) + bk + 'chat.txt'
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
       
                    conn.send('done'.encode())
                    
                        
                           
                        
                       
                    f.close()
                    
                    print('Group updated succesfully')

        elif msg[0] == 'Attach':
            if msg[2] in chatlist:
                users = get_chatlist(msg[2], 'users.txt')
           
                if msg[1] in users:
                    
                 
                    path = start_file + 'files' + bk + str(msg[2]) + bk
                    
                    m = 'True'
                    conn.send(m.encode())
                        
                    filename = msg[3].split(bk)
                    filename = filename[-1]
                    

                    recv_file(path, filename)
                        
                    add_chat(msg[1] + ' ' + msg[0] + ' ' + filename + '\n', msg[2]) 
                    print(msg, 'will be sent from x attach y')
                    broadcast('update-group', conn)



                                 
                    
                else:
                    conn.send('You are not in group'.encode())
                    
            else:
                conn.send('group not found'.encode())
                
        
        elif msg[0] == 'recv':
            if msg[2] in chatlist:
                users = get_chatlist(msg[2], 'users.txt')
           
                if msg[1] in users:
                    path = start_file + 'files' + bk + msg[2] + bk + msg[3]
                    if os.path.isfile(path):
                       
                        conn.send('True'.encode())
                        print('path to send file ', path)
                        send_file(path)
                    

                    
                    else:
                        conn.send('File name exists'.encode())
                else:
                    conn.send('You are not in group'.encode())
                        
            else:
                conn.send('group not found'.encode())

        elif msg[0] == 'get_users':
            if msg[1] in chatlist:
                users = get_chatlist(msg[1], 'users.txt')
                conn.send('True')
                users = pickle.dumps(users)
                conn.send(users)
            else:
                conn.send('group not found'.encode())

##        elif msg[0] == 'get_user_info':
##            users = get_chatlist('False', 'users.txt')
##            if msg[1] in users:
##                
##            else:
##                conn.send('user not found'.encode())





        
        else:
         
            nat = ''
            for i in msg[2:]:
                nat += i + ' '
          
            __msg = msg[0] + ' ' + msg[1] + '\n' + nat
            print()
            print(__msg)
            broadcast(__msg, conn)
    loc = clients.index(conn)
    del clients[loc]










from PyQt5 import QtCore, QtGui, QtWidgets
import socket
import threading

s = socket.socket()
ip = '127.0.0.1'
port = 12345

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

        
    


    

    
