import socket

HOST = '2.177.19.97' 
PORT = 2020
done=False

while not done:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        enter=(input())
        entere=enter.encode()
        s.connect((HOST, PORT))
        s.sendall(bytes((enter),('UTF-8')))
        data = s.recv(1024)
    print('Received', repr(data))
