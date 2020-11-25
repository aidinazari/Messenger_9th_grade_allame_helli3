
from socket import *

server = socket(AF_INET , SOCK_STREAM)
server.bind(("192.168.1.109" , 2000))
server.listen(50)

while True:
    (cSock , cAddr) = server.accept()
    a = cSock.recv(10000)
    cSock.send(bytes('sended!' , 'UTF-8'))
    print(cAddr , ':' , (a))
    cSock.close()

server.close()
