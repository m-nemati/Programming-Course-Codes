import hashlib
import csv

rainbowTable = dict()
detectPass = dict()

for i in range(0, 999):
    string = str(i)
    hashValue = hashlib.sha256(string).hexdigest()
    rainbowTable[hashValue] = i

with open('/home/mnemati/Desktop/hack/data.txt', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if row[1] in rainbowTable.keys():
            detectPass[row[0]] = rainbowTable[row[1]]

for name in detectPass:
    print ('Account Name: %s && Password: %s' %(name, detectPass[name]))
