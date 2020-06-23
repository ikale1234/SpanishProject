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


userlist = []
userfile = open(os.path.join("SpanishWords", "users.txt"), "r")
for i in range(3):
    userlist.append(userfile.readline())
for i in range(len(userlist)):
    if userlist[i][-1:] == "\n":
        userlist[i] = userlist[i][:-1]
    userlist[i] = userlist[i].split()

host = '127.0.0.1'
port = 2020
x = 1
running = True
count = 0
valid = 0
game_list = []
name_list = []
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
                iflist = pickle.loads(data)
                if len(iflist) == 3:
                    username = iflist[0]
                    password = iflist[1]
                    for i in userlist:
                        if i[0] == username:
                            if i[1] == password:
                                valid = 1
                    if count == 0:
                        if valid == 1:
                            name_list.append(username)
                            game_list.append(Game())
                            game_list[0].get_difficulty(1)
                            count += 1
                            good = 1
                            valid = 0
                        else:
                            good = 0
                        points = 10
                        token = 0
                        sendlist = [points, token, good]
                        conn.send(pickle.dumps(sendlist))
                    elif username not in name_list:
                        if valid == 1:
                            game_list.append(Game())
                            name = username
                            game_list[count].get_difficulty(1)
                            token = count
                            count += 1
                            valid = 0
                            good = 1
                        else:
                            good = 0
                            token = -1
                        points = 10
                        sendlist = [points, token, good]
                        conn.send(pickle.dumps(sendlist))
                    else:
                        points = 10
                        conn.send(pickle.dumps(points))
                if len(iflist) == 2:
                    getq = iflist[0]
                    num = iflist[1]
                    if getq == 35:
                        vals = [game_list[num].numright,
                                game_list[num].numdone]
                        val_bytes = pickle.dumps(vals)
                        conn.send(val_bytes)
                    if getq == "gq":
                        gamedata = game_list[num].getChoices()
                        gd_bytes = pickle.dumps(gamedata)
                        conn.send(gd_bytes)
                    elif getq in options:
                        if game_list[num].samplelist[getq] == game_list[num].word:
                            val = 1
                            game_list[num].numright += 1
                        else:
                            val = 0
                        game_list[num].numdone += 1
                        if game_list[num].numdone == points:
                            end = 1
                        elif game_list[num].numdone < points:
                            end = 0

                        values = [val, end, game_list[num].numright,
                                  game_list[num].numdone, game_list[num].word]
                        val_list = pickle.dumps(values)
                        conn.send(val_list)
        except KeyboardInterrupt:
            break
