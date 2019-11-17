from math import sqrt
from time import time

def exact_solution(p):
    a = 1.0
    b = 1.0
    count = 0
    while a <= b and a<p/3:
        b = a
        c = 0.0
        while c < p:
            c = sqrt(a ** 2 + b ** 2)
            if c != int(c):
                b += 1
                continue
            num = a + b + c
            if num == p:
                count += 1
            b += 1

        a += 1
    return count

start = time()
highest = 0
num = 0
for i in range(1,1001):
    sol = exact_solution(i)
    if sol>highest:
        highest = sol
        num = i

print(num)
print(highest)
print(time()-start)
