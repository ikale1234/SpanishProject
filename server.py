import socket
import pickle
host = '127.0.0.1'
port = 2004
x = 1
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if x == 1:
                wordlist = pickle.loads(data)
                print(wordlist)
                x = 0
            if not data:
                break
            conn.sendall(data)
