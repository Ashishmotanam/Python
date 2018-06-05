import math
import random
Rnum = random.randint(0, 9)

while (1):
    Gnum = int(input('Enter a number between 0-9'))
    if(Rnum == Gnum):
        print('Your number is matched with random number')
        break
    elif(Rnum < Gnum) :
        print (' your number is greater than random number')
    elif(Rnum > Gnum) :
        print (' your number is less than random number')
