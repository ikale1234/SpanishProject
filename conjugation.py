import os
import random
import verborganizer
import sys
points = 0


class Game:
    def __init__(self):
        self.points = 0
        self.listdata = []
        self.points = 0

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

    def getInput(self):
        self.guess = input("What is the "+self.tense+" tense of "+self.listdata[self.i]["Infinitive"]+" in the "+self.form+"? \nA: "+self.samplelist[0]+"\nB: "+self.samplelist[1] + "\nC: " +
                           self.samplelist[2] + "\nD: " + self.samplelist[3] + "\nE: " + self.samplelist[4]+"\nF: " + self.samplelist[5]+"\nG: " + self.samplelist[6]+"\nH: " + self.samplelist[7]+"\n")
        if self.right == self.samplelist[0]:
            self.let = "A"
        if self.right == self.samplelist[1]:
            self.let = "B"
        if self.right == self.samplelist[2]:
            self.let = "C"
        if self.right == self.samplelist[3]:
            self.let = "D"
        if self.right == self.samplelist[4]:
            self.let = "E"
        if self.right == self.samplelist[5]:
            self.let = "F"
        if self.right == self.samplelist[6]:
            self.let = "G"
        if self.right == self.samplelist[7]:
            self.let = "H"

    def checkIfRight(self):
        self.rightlist = ["Good Job! You got it right!", "Nice! That's right!", "That is the correct answer!",
                          "You are good at this!", "Wow! That was cool how you got it right!"]
        self.wronglist = ["You suck! That was the wrong answer!", "How did you miss that! That was easy!",
                          "That is the wrong answer.", "That is completely incorrect!", "Are you stupid? That was wrong!"]
        if self.guess == self.let or self.guess == self.let.lower():
            self.points += 1
            self.betweenStatements(random.choice(self.rightlist))
        else:
            self.betweenStatements(random.choice(self.wronglist))

    def runGame(self):
        self.getList()
        for a in range(10):

            self.getGameValues()

            self.getQuestionVals()

            self.getInput()

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
