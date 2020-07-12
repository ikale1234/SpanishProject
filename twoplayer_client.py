import os
import random
import verborganizer
import sys
import socket
import pickle


class Game:
    def __init__(self):
        self.HOST = '127.0.0.1'  # The server's hostname or IP address
        self.PORT = 2021    # The port used by the server

    def get_score(self):
        self.list_send = self.list_send = [35, self.token]
        self.serv_send = pickle.dumps(self.list_send)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.HOST, self.PORT))
            s.send(self.serv_send)
            self.data = s.recv(1024)
            self.data = pickle.loads(self.data)
            self.right = self.data[0]
            self.done = self.data[1]
        return self.right, self.done

    def getChoices(self):
        self.list_send = self.list_send = [36, self.token]
        self.serv_send = pickle.dumps(self.list_send)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.HOST, self.PORT))
            s.send(self.serv_send)
            self.data = s.recv(1024)
            self.data = pickle.loads(self.data)
            s.close()
        self.english = self.data[0]
        self.samplelist = self.data[1]

        return self.english, self.samplelist

    def stage0(self, username, password):
        self.name = [username, password, 1]
        self.serv_send = pickle.dumps(self.name)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.HOST, self.PORT))
            s.send(self.serv_send)
            self.data = s.recv(1024)
            self.list_data = pickle.loads(self.data)
            self.num = self.list_data[0]
            self.token = self.list_data[1]
            self.good = self.list_data[2]
            self.waiting = self.list_data[3]
            s.close()
        return self.num, self.good, self.waiting

    def get_difficulty(self, level):
        self.list_send = [level, self.token]
        self.serv_send = pickle.dumps(self.list_send)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as d:
            d.connect((self.HOST, self.PORT))
            d.send(self.serv_send)
            d.close()

    def check_answer(self, guess):
        self.list_send = [guess, self.token]
        self.serv_send = pickle.dumps(self.list_send)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as d:
            d.connect((self.HOST, self.PORT))
            d.send(self.serv_send)
            self.val = d.recv(1024)
            self.result = pickle.loads(self.val)
            d.close()
        return self.result

    def play_again(self):
        self.list_send = ["new", self.token]
        self.serv_send = pickle.dumps(self.list_send)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as d:
            d.connect((self.HOST, self.PORT))
            d.send(self.serv_send)
            d.close()
