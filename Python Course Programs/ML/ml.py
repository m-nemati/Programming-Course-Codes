import  csv
from sklearn import tree

x = []
y = []

with open('/media/mnemati/T/Python Course Programs/ML/mydataset.csv', 'r') as csvfile:
    data = csv.reader(csvfile)
    for line in data:
        x.append(line[0:2])
        y.append(line[2])

clf = tree.DecisionTreeClassifier()
clf = clf.fit(x, y)

new_data = [[192, 90], [153, 55]]
answer = clf.predict(new_data)
print (answer[0])
print (answer[1])