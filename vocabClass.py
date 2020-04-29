import os
import random
import verborganizer
import sys


class Game:

    def __init__(self, view):
        self.listdata = []
        self.level = 0
        self.vlist = []
        self.nlist = []
        self.points = 0
        self.view = view

    def betweenStatements(self, statement):
        print("\n")
        print(statement)
        input("\nPress Enter to Continue:")

    def getList(self):
        if len(sys.argv) == 1:
            self.listdata = verborganizer.build("SpanishWords")
        elif len(sys.argv) == 2:
            try:
                self.listdata = verborganizer.build(sys.argv[1])
            except FileNotFoundError:
                print("That is an invalid directory.")
                quit()
        return self.listdata

    def getDifficulty(self, level):
        self.numlist = []
        self.num = int(level)
        for i in range(self.num):
            self.numlist.append(i+1)
        return self.numlist

    def convertList(self):
        for i in self.getDifficulty(self.view.level):
            for verb in self.listdata["Verbs"]:
                if i == verb["Difficulty"]:
                    self.vlist.append(verb["Infinitive"])
        for i in self.getDifficulty(self.view.level):
            for noun in self.listdata["Nouns"]:
                if i == noun["Difficulty"]:
                    self.nlist.append(noun["Spanish"])

    def getGameValues(self):
     # change later      self.lchoice = random.choice([self.vlist, self.nlist])
        # CHANGE BELOW LATER
        self.lchoice = self.vlist
        # CHANGE ABOVE LATER
        self.samplelist = random.sample(self.lchoice, 5)

        self.word = random.choice(self.samplelist)
        if self.lchoice == self.vlist:
            for verb in self.listdata["Verbs"]:
                if self.word == verb["Infinitive"]:
                    self.english = verb["English"]
        if self.lchoice == self.nlist:
            for noun in self.listdata["Nouns"]:
                if self.word == noun["Spanish"]:
                    self.english = noun["English"]

    def checkIfRight(self):
        if self.view.guess == self.view.let or self.view.guess == self.view.let.lower():
            self.points += 1
            print("\n")
            self.correct = True
        else:
            self.correct = False

    def runGame(self):

        self.view.askDifficulty()
        self.listdata = self.getList()
        self.convertList()
        for e in range(10):

            self.getGameValues()

            self.view.getInput(self.english, self.samplelist, self.word)

            self.checkIfRight()

            self.view.displayResult(self.correct)

            self.view.checkGameOver()

        self.view.whenGameOver(self.points)
