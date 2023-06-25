import socket

HOST = '127.0.0.1'
PORT = 50007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
data = 'Hello'
s.send(data.encode('UTF-8'))
print('Send[1]: ', data)
data = s.recv(1024)
s.close()
print('Received[4]: ', data)
