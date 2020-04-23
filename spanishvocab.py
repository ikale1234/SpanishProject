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
def getlist():
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

def getDifficulty(x):
    if x == "1":
        num = "1"
    if x == "2":
        num = "2"
    if x == "3":
        num = "3"
    return num
def convertlist(verbs, nouns, z, x):
    for a in range(len(z["Verbs"])):
        if getDifficulty(x) ==  z["Verbs"][a]["Difficulty"]:
            verbs.append(z["Verbs"][a]["Infinitive"])
    for a in range(len(z["Nouns"])):
        if getDifficulty(x) ==  z["Nouns"][a]["Difficulty"]:
            nouns.append(z["Nouns"][a]["Spanish"])

# listdata = getlist()
# convertlist(vlist, nlist, listdata)
# print(nlist)
# quit()
def getgamevalues(vlist, listdata):
    x = random.choice([vlist, nlist])
    r = random.sample(x, 5)

    word = random.choice(r)
    if x == vlist:
        for i in range(len(listdata["Verbs"])):
            if word == listdata["Verbs"][i]["Infinitive"]:
                english = listdata["Verbs"][i]["English"]
    if x == nlist:
        for i in range(len(listdata["Nouns"])):
            if word == listdata["Nouns"][i]["Spanish"]:
                english = listdata["Nouns"][i]["English"]
    return word, english, r


def getuserguess(eng, r, word):
    guess = input("What is the spanish word for "+eng+"? \nA: "+r[0]+"\nB: "+r[1]+ "\nC: "+ r[2]+ "\nD: "+ r[3]+ "\nE: "+ r[4]+"\n")
    if word == r[0]:
        let = "A"
    if word == r[1]:
        let = "B"
    if word == r[2]:
        let = "C"
    if word == r[3]:
        let = "D"
    if word == r[4]:
        let = "E"
    return let, guess

def checkifright(guess, let):
    rightlist = ["Good Job! You got it right!", "Nice! That's right!", "That is the correct answer!", "You are good at this!", "Wow! That was cool how you got it right!"]
    wronglist = ["You suck! That was the wrong answer!", "How did you miss that! That was easy!", "That is the wrong answer.", "That is completely incorrect!", "Are you stupid? That was wrong!"]
    global points
    if guess == let or guess == let.lower():
        points+=1
        print("\n\n")
        print(random.choice(rightlist))
        input("\n\nPress Enter to Continue:")
    else:
        print("\n\n")
        print(random.choice(wronglist))
        input("\n\nPress Enter to Continue:")
# game
listdata = getlist()
x = input ("What is the difficulty of words you want? 1 for easiest, 3 for hardest: ")
convertlist(vlist, nlist, listdata, x)
print (vlist)

for e in range(10):

    word, eng, r = getgamevalues(vlist, listdata)
    
    let, guess = getuserguess(eng, r, word)

    checkifright(guess, let)
  
print("You got", points, "/ 10 right.")

if points == 10:
    print("Good Job! You are great at this.")
elif points > 7:
    print("You did good but it could be better.")
elif points > 3:
    print("You suck, and should study more.")
else: 
    print("Call your local doctor to check you for a mental disability.")