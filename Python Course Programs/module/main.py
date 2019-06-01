#import hesaban
from hesaban import jam, zarb

n1 = input('Enter Number 1: ')
n1 = int(n1)

n2 = input('Enter Number 2: ')
n2 = int(n2)

addNumbers = jam(n1, n2)
mulNumbers = zarb(n1, n2)

print ('N1 + N2 = %i & N1 * N2 = %i ' %(addNumbers, mulNumbers))