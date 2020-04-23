# initialization
import os
import random
import verborganizer
import sys
vocablist = []
vlist = []
nlist = []
points= 0

# functions

def betweenStatements(statement):
    print("\n")
    print(statement)
    input("\nPress Enter to Continue:")

def getList():
    if len(sys.argv) == 1:
        listdata = verborganizer.build("SpanishWords")
    elif len(sys.argv) == 2:
        print ()
        try:
            listdata = verborganizer.build(sys.argv[1])
        except FileNotFoundError:
            print("That is an invalid directory.")
            quit()
    return listdata

def getDifficulty(level):
    if level == "1":
        num = 1
    if level == "2":
        num = 2
    if level == "3":
        num = 3
    return num

def convertList(verbs, nouns, listdata, level):
    for verb in listdata["Verbs"]:
        if getDifficulty(level) ==  verb["Difficulty"]:
            verbs.append(verb["Infinitive"])
    for noun in listdata["Nouns"]:
        if getDifficulty(level) ==  noun["Difficulty"]:
            nouns.append(noun["Spanish"])

def getGameValues(vlist, listdata):
    lchoice = random.choice([vlist, nlist])
    samplelist = random.sample(lchoice, 5)

    word = random.choice(samplelist)
    if lchoice == vlist:
        for verb in listdata["Verbs"]:
            if word == verb["Infinitive"]:
                english = verb["English"]
    if lchoice == nlist:
        for noun in listdata["Nouns"]:
            if word == noun["Spanish"]:
                english = noun["English"]
    return word, english, samplelist


def getUserGuess(eng, samplelist, word):
    guess = input("What is the spanish word for "+eng+"? \nA: "+samplelist[0]+"\nB: "+samplelist[1]+ "\nC: "+ samplelist[2]+ "\nD: "+ samplelist[3]+ "\nE: "+ samplelist[4]+"\n\n")
    if word == samplelist[0]:
        let = "A"
    if word == samplelist[1]:
        let = "B"
    if word == samplelist[2]:
        let = "C"
    if word == samplelist[3]:
        let = "D"
    if word == samplelist[4]:
        let = "E"
    return let, guess

def checkIfRight(guess, let):
    rightlist = ["Good Job! You got it right!", "Nice! That's right!", "That is the correct answer!", "You are good at this!", "Wow! That was cool how you got it right!"]
    wronglist = ["That was the wrong answer! Nice try though.", "How did you miss that! That was easy!", "That is the wrong answer.", "That is completely incorrect!", "That was wrong!"]
    global points
    if guess == let or guess == let.lower():
        points+=1
        print("\n")
        betweenStatements(random.choice(rightlist))
    else:
        betweenStatements(random.choice(wronglist))

listdata = getList()
level = input ("What is the difficulty of words you want? 1 for easiest, 3 for hardest: ")
convertList(vlist, nlist, listdata, level)
print (vlist)

for e in range(10):

    word, eng, samplelist = getGameValues(vlist, listdata)
    
    let, guess = getUserGuess(eng, samplelist, word)

    checkIfRight(guess, let)
  
print("You got", points, "/ 10 right.")

if points == 10:
    print("Good Job! You are great at this.")
elif points > 7:
    print("You did good but it could be better.")
elif points > 3:
    print("You suck, and should study more.")
else: 
    print("Call your local doctor to check you for a mental disability.")