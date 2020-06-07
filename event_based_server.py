import os
import random
import verborganizer
import sys
import socket
import pickle


class Game:
    def __init__(self):

        self.listdata = []
        self.thelist = []
        if len(sys.argv) == 1:
            self.listdata = verborganizer.build("SpanishWords")
        elif len(sys.argv) == 2:
            try:
                self.listdata = verborganizer.build(sys.argv[1])
            except FileNotFoundError:
                print("That is an invalid directory.")
                quit()
        self.vlist = []
        self.nlist = []

    def getChoices(self):
        # change later      lchoice = random.choice([vlist, nlist])
        # CHANGE BELOW LATER
        self.lchoice = self.vlist
        # CHANGE ABOVE LATER
        self.samplelist = random.sample(self.lchoice, 8)

        self.word = random.choice(self.samplelist)
        if self.lchoice == self.vlist:
            for verb in self.listdata["Verbs"]:
                if self.word == verb["Infinitive"]:
                    self.english = verb["English"]
        if self.lchoice == self.nlist:
            for noun in self.listdata["Nouns"]:
                if self.word == noun["Spanish"]:
                    self.english = noun["English"]
        self.data = []
        print(self.english)
        print(self.samplelist)
        self.data.append(self.english)
        self.data.append(self.word)
        self.data.append(self.samplelist)

        return self.data

    def get_difficulty(self, level):

        for i in range(level):
            self.thelist.append(i+1)

            for i in self.thelist:
                for verb in self.listdata["Verbs"]:
                    if i == verb["Difficulty"]:
                        self.vlist.append(verb["Infinitive"])
            for i in self.thelist:
                for noun in self.listdata["Nouns"]:
                    if i == noun["Difficulty"]:
                        self.nlist.append(noun["Spanish"])

    def check_answer(self, guess, let):
        if guess == let or guess == let.lower():
            self.right = True
        else:
            self.right = False
        return self.right


game = Game()
host = '127.0.0.1'
port = 20012
x = 1
levels = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))
    while True:
        s.listen()
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            data = conn.recv(1024)
            getq = pickle.loads(data)
            if getq == "gq":
                gamedata = game.getChoices()
                gd = pickle.dumps(gamedata)
                conn.send(gd)
            if getq in levels:
                game.get_difficulty(getq)
