import os
import random
import verborganizer
import sys
points= 0

def getlist():
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

listdata = getlist()

def getgamevalues(listdata):
    r = []
    a = -1
    for b in range (6):
        if b == 0:
            i = random.randrange((len(listdata)))
        j = random.choice(["Present", "Preterite", "Imperfect"])
        if b > a:
            k = random.randrange(0,5)
        word = listdata[i][j][k]
        
        
        if b == 0:
                x, y, z = i, j, k
                if word[-4:] == "amos":
                    a = 1
                else:
                    a = 2
        # checks repeating
        restart = True
        while restart:
            restart = False
            for c in range(len(r)):
                while word == r[c]:
                    j = random.choice(["Present", "Preterite", "Imperfect"])
                    if b > a:
                        k = random.randrange(0,5)
                    word = listdata[i][j][k]
    
        
            r.append(word)
    right = r[0]
    random.shuffle(r)
    
    return x, y, z, r, right

def getquestionvals():
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
        form = random.choice(["ellos","ellas","ustedes"])
    return tense, form

def getinput(tense, right, r, listdata, i, form):
    guess = input("What is the "+tense+" tense of "+listdata[i]["Infinitive"]+" in the "+form+"? \nA: "+r[0]+"\nB: "+r[1]+ "\nC: "+ r[2]+ "\nD: "+ r[3]+ "\nE: "+ r[4]+"\nF: "+ r[5]+"\n")
    if right == r[0]:
        let = "A"
    if right == r[1]:
        let = "B"
    if right == r[2]:
        let = "C"
    if right == r[3]:
        let = "D"
    if right == r[4]:
        let = "E"
    if right == r[5]:
        let = "F"
    return guess, let

def checkifright(guess, let):
    global points
    rightlist = ["Good Job! You got it right!", "Nice! That's right!", "That is the correct answer!", "You are good at this!", "Wow! That was cool how you got it right!"]
    wronglist = ["You suck! That was the wrong answer!", "How did you miss that! That was easy!", "That is the wrong answer.", "That is completely incorrect!", "Are you stupid? That was wrong!"]
    if guess == let or guess == let.lower():
        points+=1
        print("\n\n")
        print(random.choice(rightlist))
        input("\n\nPress Enter to Continue:")
    else:
        print("\n\n")
        print(random.choice(wronglist))
        input("\n\nPress Enter to Continue:")
for a in range(10):
 
    i, j, k, r, right = getgamevalues(listdata)
    
    tense, form = getquestionvals()
    
    guess, let = getinput(tense, right, r, listdata, i, form)
    
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

