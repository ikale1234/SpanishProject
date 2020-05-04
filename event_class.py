import os
import random
import verborganizer
import sys


class Game:
    def __init__(self):
        self.vlist = []
        self.nlist = []
        self.listdata = []
        self.thelist = []

    def get_list(self):
        if len(sys.argv) == 1:
            self.listdata = verborganizer.build("SpanishWords")
        elif len(sys.argv) == 2:
            try:
                self.listdata = verborganizer.build(sys.argv[1])
            except FileNotFoundError:
                print("That is an invalid directory.")
                quit()

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
        return self.english, self.word, self.samplelist

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
