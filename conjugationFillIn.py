import random


class consoleView:
    def __init__(self):
        self.rightlist = ["Good Job! You got it right!", "Nice! That's right!",
                          "That is the correct answer!", "You are good at this!", "Wow! That was cool how you got it right!"]
        self.wronglist = ["You suck! That was the wrong answer!", "How did you miss that! That was easy!",
                          "That is the wrong answer.", "That is completely incorrect!", "Are you stupid? That was wrong!"]

    def betweenStatements(self, statement):
        print("\n")
        print(statement)
        input("\nPress Enter to Continue:")

    def getInput(self, tense, listdata, samplelist, right, i, form):
        self.guess = input("What is the "+tense+" tense of " +
                           listdata[i]["Infinitive"]+" in the "+form+"?" + "\n")
        self.let = right

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
