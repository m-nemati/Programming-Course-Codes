import random

javab = input('Enter a Number Between 1 to 99: ')
javab = int(javab)
a= 1
b = 99
hads = random.randint(a, b)

while hads != javab:
    if hads > javab:
        print (hads)
        print ('Hads is Grater')
        b = hads
        hads = random.randint(a , b)
    else:
        print (hads)
        print ('Hads is Lower')
        a = hads
        hads = random.randint(a , b)
print ("wwwooooowwww")
print (hads)