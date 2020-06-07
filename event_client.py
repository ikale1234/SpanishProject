import os
import random
import verborganizer
import sys
import socket
import pickle


class Game:
    def __init__(self):
        self.HOST = '127.0.0.1'  # The server's hostname or IP address
        self.PORT = 20012      # The port used by the server

    def getChoices(self):
        self.servsend = pickle.dumps("gq")
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.HOST, self.PORT))
            s.send(self.servsend)
            self.data = s.recv(1024)
            self.data = pickle.loads(self.data)
            s.close()
        self.english = self.data[0]
        self.word = self.data[1]
        self.samplelist = self.data[2]

        return self.english, self.word, self.samplelist

    def get_difficulty(self, level):
        self.servsend = pickle.dumps(level)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as d:
            d.connect((self.HOST, self.PORT))
            d.send(self.servsend)
            d.close()

    def check_answer(self, guess, let):
        if guess == let or guess == let.lower():
            self.right = True
        else:
            self.right = False
        return self.right
