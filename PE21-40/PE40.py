from time import time


numstr = ''
for i in range(1000000):
    numstr += str(i)

l = list(numstr)

sol = 1
for i in range(7):
    sol *= int(l[10**i])

print(sol)
