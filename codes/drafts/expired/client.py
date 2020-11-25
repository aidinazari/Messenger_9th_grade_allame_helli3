
from socket import *

while True:
    i = (input())
    mySock = socket(AF_INET , SOCK_STREAM)
    mySock.connect(("192.168.1.109" , 2000))
    mySock.send(bytes(str(i) , 'UTF-8'))
    print('server said:' , mySock.recv(10000))
    mySock.close()
