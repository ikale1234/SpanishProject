import csv
import sys
filename = '..\\jehle_verb_database.csv.txt'
biglist = []
with open(filename, newline='') as f:
    reader = csv.reader(f)
    try:
        for row in reader:
            biglist.append(row)
    except csv.Error as e:
        sys.exit('file {}, line {}: {}'.format(filename, reader.line_num, e))
biglist.pop(0)


def conjConvert(index, data):
    x = str(data[index][7:11]+data[index][12].split(' '))
    x = x.replace('[', '')
    x = x.replace(']', '')
    x = x.replace('\'', '')
    return x


def checkCount(count, num, diff):
    if count > num:
        difficulty = diff
        return difficulty
    else:
        return -1


diff = 0


def processWord(data, count):
    x = 0
    totext = []
    if (len(data) != 18):
        print("Got bad data", len(data))
    if (len(data) >= 14):
        totext.append(data[0][0])
        totext.append(data[0][1])
        totext.append(conjConvert(0, data))
        totext.append(conjConvert(3, data))
        totext.append(conjConvert(2, data))
        if count > 0:
            difficulty = "1"
        if count > 50:
            difficulty = "2"
        if count > 100:
            difficulty = "3"
        totext.append(difficulty)
        '''if x != -1:
            x = checkCount(count, 0, 1)
        if x != -1:
            x = checkCount(count, 0, 1)
        if x != -1:
            x = checkCount(count, 0, 1)
        if x != -1:
            x = checkCount(count, 0, 1)
        if x != -1:
            x = checkCount(count, 0, 1)
        if x != -1:
            x = checkCount(count, 0, 1)
        if x != -1:
            x = checkCount(count, 0, 1)'''

    return totext


textlist = []

count = 0
data = []
word = biglist[0][0]
for item in biglist:
    if item[0] != word:
        count += 1
        textlist.append(processWord(data, count))
        data = []
        word = item[0]
    data.append(item)

for item in textlist:
    if item != []:
        f = open("DataforSpanish\\" + item[0] + ".txt", "w")
        for element in item:
            f.write(element + '\n')
        f.close()
