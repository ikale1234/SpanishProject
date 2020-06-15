import os
import random
import verborganizer
import sys
import socket
import pickle


class Game:
    def __init__(self):
        self.HOST = '127.0.0.1'  # The server's hostname or IP address
        self.PORT = 2020    # The port used by the server

    def get_score(self):
        self.servsend = pickle.dumps(35)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.HOST, self.PORT))
            s.send(self.servsend)
            self.data = s.recv(1024)
            self.data = pickle.loads(self.data)
            self.right = self.data[0]
            self.done = self.data[1]
        return self.right, self.done

    def getChoices(self):
        self.servsend = pickle.dumps("gq")
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.HOST, self.PORT))
            s.send(self.servsend)
            self.data = s.recv(1024)
            self.data = pickle.loads(self.data)
            s.close()
        self.english = self.data[0]
        self.samplelist = self.data[1]

        return self.english, self.samplelist

    def stage0(self):
        self.name = input("Enter name: ")
        self.servsend = pickle.dumps(self.name)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.HOST, self.PORT))
            s.send(self.servsend)
            self.data = s.recv(1024)
            self.num = pickle.loads(self.data)
            s.close()
        return self.num

    def get_difficulty(self, level):
        self.servsend = pickle.dumps(level)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as d:
            d.connect((self.HOST, self.PORT))
            d.send(self.servsend)
            d.close()

    def check_answer(self, guess):

        self.servsend = pickle.dumps(guess)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as d:
            d.connect((self.HOST, self.PORT))
            d.send(self.servsend)
            self.val = d.recv(1024)
            self.thing = pickle.loads(self.val)
            d.close()
        return self.thing

    def play_again(self):
        self.servsend = pickle.dumps("new")
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as d:
            d.connect((self.HOST, self.PORT))
            d.send(self.servsend)
            d.close()
