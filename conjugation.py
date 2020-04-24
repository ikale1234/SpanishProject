import os
import random
import verborganizer
import sys
points = 0


def betweenStatements(statement):
    print("\n")
    print(statement)
    input("\nPress Enter to Continue:")


def getList():
    if len(sys.argv) == 1:
        alldata = verborganizer.build("SpanishWords")
        listdata = alldata["Verbs"]
    elif len(sys.argv) == 2:
        try:
            listdata = verborganizer.build(sys.argv[1])
        except FileNotFoundError:
            print("That is an invalid directory.")
            quit()
    else:
        print("That is an invalid directory.")
        quit()
    return listdata


listdata = getList()


def getGameValues(listdata):
    samplelist = []
    for idx in range(3):
        if idx == 0:
            i = random.randrange((len(listdata)))
            k = random.randrange(0, 5)
            j = "Present"
            doc, form = i, k
        if idx == 1:
            j = "Preterite"
        if idx == 2:
            j = "Imperfect"
        samplelist.append(listdata[i][j][k])
    if samplelist[0] == samplelist[1]:
        samplelist = samplelist.pop(0)

    for idx in range(8-len(samplelist)):
        k = random.randrange(0, 5)
        j = random.choice(["Present", "Preterite", "Imperfect"])
        while listdata[i][j][k] in samplelist:
            k = random.randrange(0, 5)
            j = random.choice(["Present", "Preterite", "Imperfect"])
        samplelist.append(listdata[i][j][k])

    # checks repeating

    right = samplelist[random.randrange(3)]
    if right == samplelist[0]:
        tense = "Present"
    if right == samplelist[1]:
        tense = "Preterite"
    if right == samplelist[2]:
        tense = "Imperfect"

    random.shuffle(samplelist)

    return doc, tense, form, samplelist, right


def getQuestionVals(j, k):
    if j == "Present":
        tense = "present"
    if j == "Preterite":
        tense = "preterite"
    if j == "Imperfect":
        tense = "imperfect"
    if k == 0:
        form = "yo"
    if k == 1:
        form = "tu"
    if k == 2:
        form = random.choice(["el", "ella", "usted"])
    if k == 3:
        form = "nosotros"
    if k == 4:
        form = random.choice(["ellos", "ellas", "ustedes"])
    return tense, form


def getInput(tense, right, samplelist, listdata, idx, form):
    guess = input("What is the "+tense+" tense of "+listdata[idx]["Infinitive"]+" in the "+form+"? \nA: "+samplelist[0]+"\nB: "+samplelist[1] + "\nC: " +
                  samplelist[2] + "\nD: " + samplelist[3] + "\nE: " + samplelist[4]+"\nF: " + samplelist[5]+"\nG: " + samplelist[6]+"\nH: " + samplelist[7]+"\n")
    if right == samplelist[0]:
        let = "A"
    if right == samplelist[1]:
        let = "B"
    if right == samplelist[2]:
        let = "C"
    if right == samplelist[3]:
        let = "D"
    if right == samplelist[4]:
        let = "E"
    if right == samplelist[5]:
        let = "F"
    if right == samplelist[6]:
        let = "G"
    if right == samplelist[7]:
        let = "H"
    return guess, let


def checkIfRight(guess, let):
    global points
    rightlist = ["Good Job! You got it right!", "Nice! That's right!", "That is the correct answer!",
                 "You are good at this!", "Wow! That was cool how you got it right!"]
    wronglist = ["You suck! That was the wrong answer!", "How did you miss that! That was easy!",
                 "That is the wrong answer.", "That is completely incorrect!", "Are you stupid? That was wrong!"]
    if guess == let or guess == let.lower():
        points += 1
        betweenStatements(random.choice(rightlist))
    else:
        betweenStatements(random.choice(wronglist))


for a in range(10):

    idx, j, k, samplelist, right = getGameValues(listdata)

    tense, form = getQuestionVals(j, k)

    guess, let = getInput(tense, right, samplelist, listdata, idx, form)

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
