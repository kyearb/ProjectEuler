from time import time
from functools import reduce

def factorial(n):
    return reduce(lambda x,y:x*y,[1]+list(range(1,n+1)))

def fact(n):
    if n > 1:
        return n*fact(n-1)
    else:
        return 1


l = []
for i in range(10,10**7):
    num = 0
    sub = i
    # while not ending in 0
    if i%10 != 0:
        for char in str(sub): # loop though each digit
            num += fact(int(char))
        if num==i:
            l.append(i)

for i in l:
    print(i)

print(sum(l))
