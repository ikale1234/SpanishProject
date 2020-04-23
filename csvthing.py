import csv, sys
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

def processWord(data):

    totext = []
    if (len(data) != 18):
        print("Got bad data", len(data))
    totext.append(data[0][0])
    totext.append(data[0][1])
    totext.append(conjConvert(0, data))
    totext.append(conjConvert(3, data))
    totext.append(conjConvert(2, data))
    
    return totext

   

textlist = []

count = 0
data = []
word = biglist[0][0]
for item in biglist:
    if item[0] != word:
        textlist.append(processWord(data))
        data = []
        word = item[0]
        count += 1
    data.append(item)
    if (count > 10):
        break



for item in textlist:
    f= open("DataforSpanish\\" + item[0] + ".txt","w")
    for element in item:
        f.write(element + '\n')
    f.close()