import random


class consoleView:
    def __init__(self):
        self.rightlist = ["Good Job! You got it right!", "Nice! That's right!",
                          "That is the correct answer!", "You are good at this!", "Wow! That was cool how you got it right!"]
        self.wronglist = ["You suck! That was the wrong answer!", "How did you miss that! That was easy!",
                          "That is the wrong answer.", "That is completely incorrect!", "Are you stupid? That was wrong!"]
        self.turns = 0
        self.gameover = False

    def askDifficulty(self):
        self.level = input(
            "What is the difficulty of words you want? 1 for easiest, 10 for hardest: ")

    def betweenStatements(self, statement):
        print("\n")
        print(statement)
        input("\nPress Enter to Continue:")

    def getInput(self, english, samplelist, word):
        self.guess = input("What is the spanish word for " + english+"? \nA: " +
                           samplelist[0]+"\nB: " + samplelist[1] + "\nC: " + samplelist[2] + "\nD: " + samplelist[3] + "\nE: " + samplelist[4]+"\n\n")
        self.turns += 1
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

    def checkGameOver(self):
        if self.turns == 10:
            self.gameover == True

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
