import socket
import pickle
wordlist = []
HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 2004      # The port used by the server

for i in range(7):

servsend = pickle.loads(data)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.send(servsend)
    data = s.recv(1024)

print('Received', repr(data))
