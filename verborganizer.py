import os

def build(dir):
    verbbank = []
    nounbank = []
    wordbank = {}
    verbs =  os.listdir(dir+"\\Verbs")
    nouns = os.listdir(dir+"\\Nouns")

    #  verbs
    for i in range(len(verbs)):
        curfile = open(dir+"\\Verbs\\"+verbs[i], "r")
        pol = []
        templist = {}
        for j in range(6):
            pol.append(curfile.readline())
            if pol[j][-1:] == "\n":
                pol[j] = pol[j][:-1]
            if j == 0:
                templist["Infinitive"] = pol[j]
            if j == 1:
                templist["English"] = pol[j]
            if j == 2:
                pol[j] = pol[j].split(",")
                templist["Present"] = pol[j]
            if j == 3:
                pol[j] = pol[j].split(",")
                templist["Preterite"] = pol[j]
            if j == 4:
                pol[j] = pol[j].split(",")
                templist["Imperfect"] = pol[j]
            if j == 5:
                templist["Difficulty"] = pol[j]

        curfile.close()
        #check


        good = False          
        if len(templist["Present"]) == len(templist["Preterite"]) == len(templist["Imperfect"]) == 5:
            good = True
        if good:
            verbbank.append(templist)

    # nouns
    for i in range(len(nouns)):
        curfile = open(dir+"\\Nouns\\"+nouns[i], "r")
        templist = {}
        x = curfile.readline()
        y = curfile.readline()
        z = curfile.readline()
        if x[-1:] == "\n":
            x = x[:-1]
        if y[-1:] == "\n":
            y = y[:-1]  
        if z[-1:] == "\n":
            z = z[:-1]
        curfile.close()
        templist["Spanish"] = x
        templist["English"] = y
        templist["Difficulty"] = z
        nounbank.append(templist)
    wordbank["Verbs"] = verbbank
    wordbank["Nouns"] = nounbank
    return wordbank

