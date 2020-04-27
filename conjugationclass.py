import os
import random
import verborganizer
import sys


class Game:
    def __init__(self, view):
        self.points = 0
        self.listdata = []
        self.points = 0
        self.view = view

    def betweenStatements(self, statement):
        print("\n")
        print(statement)
        input("\nPress Enter to Continue:")

    def getList(self):
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

    def getGameValues(self):
        self.samplelist = []
        for idx in range(3):
            if idx == 0:
                self.i = random.randrange((len(self.listdata)))
                self.k = random.randrange(0, 5)
                self.j = "Present"
                self.doc, self.rform = self.i, self.k
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

    def getQuestionVals(self):
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

    def checkIfRight(self):

        if self.view.guess == self.view.let or self.view.guess == self.view.let.lower():
            self.points += 1
            self.correct = True
        else:
            self.correct = False

    def runGame(self):
        self.getList()
        for a in range(10):

            self.getGameValues()

            self.getQuestionVals()

            self.view.getInput(self.tense, self.listdata,
                               self.samplelist, self.right, self.i, self.form)

            self.checkIfRight()

            self.view.displayResult(self.correct)

        self.view.whenGameOver(self.points)
