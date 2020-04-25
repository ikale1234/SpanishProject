# initialization
import os
import random
import verborganizer
import sys


# functions


class Game:

    def __init__(self):
        self.listdata = []
        self.level = 0
        self.vlist = []
        self.nlist = []
        self.level = input(
            "What is the difficulty of words you want? 1 for easiest, 3 for hardest: ")
        self.points = 0

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
        if self.level == "1":
            self.num = 1
        if self.level == "2":
            self.num = 2
        if self.level == "3":
            self.num = 3
        return self.num

    def convertList(self):
        for verb in self.listdata["Verbs"]:
            if self.getDifficulty(self.level) == verb["Difficulty"]:
                self.vlist.append(verb["Infinitive"])
        for noun in self.listdata["Nouns"]:
            if self.getDifficulty(self.level) == noun["Difficulty"]:
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

    def getUserGuess(self):
        self.guess = input("What is the spanish word for " + self.english+"? \nA: " +
                           self.samplelist[0]+"\nB: " + self.samplelist[1] + "\nC: " + self.samplelist[2] + "\nD: " + self.samplelist[3] + "\nE: " + self.samplelist[4]+"\n\n")
        if self.word == self.samplelist[0]:
            self.let = "A"
        if self.word == self.samplelist[1]:
            self.let = "B"
        if self.word == self.samplelist[2]:
            self.let = "C"
        if self.word == self.samplelist[3]:
            self.let = "D"
        if self.word == self.samplelist[4]:
            self.let = "E"

    def checkIfRight(self):
        self.rightlist = ["Good Job! You got it right!", "Nice! That's right!", "That is the correct answer!",
                          "You are good at this!", "Wow! That was cool how you got it right!"]
        self.wronglist = ["That was the wrong answer! Nice try though.", "How did you miss that! That was easy!",
                          "That is the wrong answer.", "That is completely incorrect!", "That was wrong!"]
        if self.guess == self.let or self.guess == self.let.lower():
            self.points += 1
            print("\n")
            self.betweenStatements(random.choice(self.rightlist))
        else:
            self.betweenStatements(random.choice(self.wronglist))

    def runGame(self):

        self.listdata = self.getList()
        self.convertList()
        for e in range(10):

            self.getGameValues()

            self.getUserGuess()

            self.checkIfRight()

        print("You got", self.points, "/ 10 right.")

        if self.points == 10:
            print("Good Job! You are great at this.")
        elif self.points > 7:
            print("You did good but it could be better.")
        elif self.points > 3:
            print("You suck, and should study more.")
        else:
            print("Call your local doctor to check you for a mental disability.")


game = Game()
game.runGame()
