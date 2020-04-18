import csv, sys
filename = 'C:\\Users\\vadog\\Work\\Work\\SpanishWords\\jehle_verb_database.csv.txt'
biglist = []
with open(filename, newline='') as f:
    reader = csv.reader(f)
    try:
        for row in reader:
            biglist.append(row)
    except csv.Error as e:
        sys.exit('file {}, line {}: {}'.format(filename, reader.line_num, e))
biglist.pop(0)
data = []
for item in biglist[0:11466:18]:
    x = str(item[7:11]+item[12].split(' '))
    x = x.replace('[', '')
    x = x.replace(']', '')
    x = x.replace('\'', '')
    data.append([item[0], item[1], x])
c = -1
for item in biglist[3:11466:18]:
    c+=1
    x = str(item[7:11]+item[12].split(' '))
    x = x.replace('[', '')
    x = x.replace(']', '')
    x = x.replace('\'', '')
    data[c].append(x)
c = -1
for item in biglist[2:11466:18]:
    c+=1
    x = str(item[7:11]+item[12].split(' '))
    x = x.replace('[', '')
    x = x.replace(']', '')
    x = x.replace('\'', '')
    data[c].append(x)
for item in range(len(data)):
    f= open("C:\\Users\\vadog\\Work\\Work\\DataforSpanish\\"+data[item][0]+".txt","w")
    for i in range(5):
        f.write(data[item][i]+'\n')
    f.close()