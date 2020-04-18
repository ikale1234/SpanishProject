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

def convertlist(verbs, nouns, z):
    for a in range(len(z["Verbs"])):
        verbs.append(z["Verbs"][a]["Infinitive"])
    for a in range(len(z["Nouns"])):
        nouns.append(z["Nouns"][a]["Spanish"])

# listdata = getlist()
# convertlist(vlist, nlist, listdata)
# print(nlist)
# quit()
def getgamevalues():
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


def getuserguess():
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

def checkifright():
    global points
    if guess == let or guess == let.lower():
        points+=1
        print("\n\n")
        print("You got a point.")
        input("\n\nPress Enter to Continue:")
    else:
        print("\n\n")
        print("You got that question wrong.")
        input("\n\nPress Enter to Continue:")
# game
listdata = getlist()
convertlist(vlist, nlist, listdata)

for e in range(10):
    word, eng, r = getgamevalues()
    
    let, guess = getuserguess()

    checkifright()
  
print("You got", points, "/ 10 right.")

if points == 10:
    print("Good Job! You are great at this.")
elif points > 7:
    print("You did good but it could be better.")
elif points > 3:
    print("You suck, and should study more.")
else: 
    print("Call your local doctor to check you for a mental disability.")