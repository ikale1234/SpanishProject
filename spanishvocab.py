# initialization
import os
import random
import verborganizer
import sys


# functions


class consoleView:
    def __init__(self):
        self.rightlist = ["Good Job! You got it right!", "Nice! That's right!",
                          "That is the correct answer!", "You are good at this!", "Wow! That was cool how you got it right!"]
        self.wronglist = ["You suck! That was the wrong answer!", "How did you miss that! That was easy!",
                          "That is the wrong answer.", "That is completely incorrect!", "Are you stupid? That was wrong!"]

    def askDifficulty(self):
        self.level = input(
            "What is the difficulty of words you want? 1 for easiest, 3 for hardest: ")

    def betweenStatements(self, statement):
        print("\n")
        print(statement)
        input("\nPress Enter to Continue:")

    def getInput(self, english, samplelist, word):
        self.guess = input("What is the spanish word for " + english+"? \nA: " +
                           samplelist[0]+"\nB: " + samplelist[1] + "\nC: " + samplelist[2] + "\nD: " + samplelist[3] + "\nE: " + samplelist[4]+"\n\n")
        if word == samplelist[0]:
            self.let = "A"
        if word == samplelist[1]:
            self.let = "B"
        if word == samplelist[2]:
            self.let = "C"
        if word == samplelist[3]:
            self.let = "D"
        if word == samplelist[4]:
            self.let = "E"

    def displayResult(self, correct):
        if correct:
            self.betweenStatements(random.choice(self.rightlist))
        else:
            self.betweenStatements(random.choice(self.wronglist))

    def whenGameOver(self, points):
        print("You got", points, "/ 10 right.")
        if points == 10:
            print("Good Job! You are great at this.")
        elif points > 7:
            print("You did good but it could be better.")
        elif points > 3:
            print("You suck, and should study more.")
        else:
            print("Call your local doctor to check you for a mental disability.")


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
        if level == "1":
            self.num = 1
        if level == "2":
            self.num = 2
        if level == "3":
            self.num = 3
        return self.num

    def convertList(self):
        for verb in self.listdata["Verbs"]:
            if self.getDifficulty(self.view.level) == verb["Difficulty"]:
                self.vlist.append(verb["Infinitive"])
        for noun in self.listdata["Nouns"]:
            if self.getDifficulty(self.view.level) == noun["Difficulty"]:
                self.nlist.append(noun["Spanish"])
        print(self.vlist)

    def getGameValues(self):
        self.lchoice = random.choice([self.vlist, self.nlist])
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

        self.view.whenGameOver(self.points)


view = consoleView()
game = Game(view)
game.runGame()
