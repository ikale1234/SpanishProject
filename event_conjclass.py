import os
import random
import verborganizer
import sys


class Game:
    def __init__(self):

        self.listdata = []
        self.thelist = []

    def get_list(self):
        if len(sys.argv) == 1:
            self.alldata = verborganizer.build("SpanishWords")
            self.listdata = self.alldata["Verbs"]
        elif len(sys.argv) == 2:
            try:
                self.listdata = verborganizer.build(sys.argv[1])
            except FileNotFoundError:
                print("That is an invalid directory.")
                quit()
        else:
            print("That is an invalid directory.")
            quit()

    def get_game_values(self):
        self.samplelist = []
        for idx in range(3):
            if idx == 0:
                self.i = random.randrange((len(self.listdata)))
                self.k = random.randrange(0, 5)
                self.j = "Present"
                self.infinitive, self.rform = self.listdata[self.i]["Infinitive"], self.k
            if idx == 1:
                self.j = "Preterite"
            if idx == 2:
                self.j = "Imperfect"
            self.samplelist.append(self.listdata[self.i][self.j][self.k])
        if self.samplelist[0] == self.samplelist[1]:
            self.samplelist = self.samplelist.pop(0)

        for idx in range(8-len(self.samplelist)):
            self.k = random.randrange(0, 5)
            self.j = random.choice(["Present", "Preterite", "Imperfect"])
            while self.listdata[self.i][self.j][self.k] in self.samplelist:
                self.k = random.randrange(0, 5)
                self.j = random.choice(["Present", "Preterite", "Imperfect"])
            self.samplelist.append(self.listdata[self.i][self.j][self.k])
        # checks repeating

        self.right = self.samplelist[random.randrange(3)]
        if self.right == self.samplelist[0]:
            self.rtense = "Present"
        if self.right == self.samplelist[1]:
            self.rtense = "Preterite"
        if self.right == self.samplelist[2]:
            self.rtense = "Imperfect"

        random.shuffle(self.samplelist)
        return self.infinitive, self.right, self.samplelist

    def get_question_vals(self):
        if self.rtense == "Present":
            self.tense = "present"
        if self.rtense == "Preterite":
            self.tense = "preterite"
        if self.rtense == "Imperfect":
            self.tense = "imperfect"
        if self.rform == 0:
            self.form = "yo"
        if self.rform == 1:
            self.form = "tu"
        if self.rform == 2:
            self.form = random.choice(["el", "ella", "usted"])
        if self.rform == 3:
            self.form = "nosotros"
        if self.rform == 4:
            self.form = random.choice(["ellos", "ellas", "ustedes"])
        return self.form, self.tense

    def check_answer(self, guess, let):
        if guess == let or guess == let.lower():
            self.right = True
        else:
            self.right = False
        return self.right
