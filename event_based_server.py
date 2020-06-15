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
        self.numright = 0
        self.numdone = 0
        self.samplelist = [1, 2, 3, 4, 5]

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
        self.data.append(self.english)
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


host = '127.0.0.1'
port = 2020
x = 1
running = True
count = 0
options = [1, 2, 3, 4, 5, 6, 7, 8]
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))
    while True:
        try:
            s.listen()
            conn, addr = s.accept()
            with conn:
                print('Connected by', addr)
                data = conn.recv(1024)
                getq = pickle.loads(data)
                if count == 0:
                    name = getq
                    game = Game()
                    game.get_difficulty(1)
                    count += 1
                    end = 0
                    points = 10
                    conn.send(pickle.dumps(points))
                if count != 0:
                    if getq == 35:
                        vals = [game.numright, game.numdone]
                        thing = pickle.dumps(vals)
                        conn.send(thing)
                    if getq == "gq":
                        gamedata = game.getChoices()
                        gd = pickle.dumps(gamedata)
                        conn.send(gd)
                    elif getq in options:
                        if game.samplelist[getq] == game.word:
                            val = 1
                            game.numright += 1
                        else:
                            val = 0
                        game.numdone += 1
                        if game.numdone == points:
                            end = 1

                        values = [val, end, game.numright,
                                  game.numdone, game.word]
                        lis = pickle.dumps(values)
                        conn.send(lis)
                    elif getq != name:
                        game = Game()
                        name = getq
                        game.get_difficulty(1)

                        end = 0
                        points = 10
                        conn.send(pickle.dumps(points))
                    else:
                        points = 10
                        conn.send(pickle.dumps(points))
        except KeyboardInterrupt:
            break
