#ex3

import random


x=random.randint(1,10)
print(x)

found=0

while found==0:
        guess=int(input("Guess a Number:"))
        if guess == x:
                found=1
print("right")
 
                

