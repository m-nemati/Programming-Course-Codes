import random
javab = random.randint(1, 99)

hads = input('Hads Bezan: ')
hads = int(hads)

while hads != javab:
    if hads < javab:
        print ('Lower Than Javab')
    else:
        print ('grater than Javab')
    hads = input('Hada Bezan Dobare: ')
    hads = int(hads)

print ("WOOOOOOOWW!!!")