import itertools
from functools import reduce
from time import time

def prime_numbers(limit=1000000):
    '''Prime number generator. Yields the series
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29 ...
    using Sieve of Eratosthenes.
    '''
    yield 2
    sub_limit = int(limit**0.5)
    flags = [True, True] + [False] * (limit - 2)
    # Step through all the odd numbers
    for i in range(3, limit, 2):
        if flags[i]:
            continue
        yield i
        # Exclude further multiples of the current prime number
        if i <= sub_limit:
            for j in range(i*i, limit, i<<1):
                flags[j] = True
"""
start = time()
num = []
for p in prime_numbers(1000000):
    num.append(p)
l = []
l.append(2)
for i in num:
    for j in str(i):
        if int(i)%2==0 or i==5:
            l.append(i)
            break

for i in l:
    num.remove(i)

l = []
total = 0
for n in num:
    result = True
    lst = [n]
    ns = list(str(n))
    ns.append(ns.pop(0))
    n2 = reduce(lambda x,y:int(x)*10+int(y),ns)
    count = 0
    while not n2 == n and n>9:
        if n2 not in num:
            result = False
        else:
            lst.append(num.pop(num.index(n2)))
            count += 1
        ns.append(ns.pop(0))
        n2 = reduce(lambda x,y:int(x)*10+int(y),ns)
    if result:
        total += 1
        l += lst

l = list(set(l))
l.sort()
print(l)
print(len(l))
print(total)
print(time()-start)
"""


start = time()
num = []
for p in prime_numbers(1000000):
    num.append(p)
l = []
total = 0
for n in num:
    result = True
    lst = [n]
    ns = list(str(n))
    ns.append(ns.pop(0))
    n2 = reduce(lambda x,y:int(x)*10+int(y),ns)
    count = 0
    while not n2 == n and n>9:
        if n2 not in num:
            result = False
        else:
            lst.append(num.pop(num.index(n2)))
            count += 1
        ns.append(ns.pop(0))
        n2 = reduce(lambda x,y:int(x)*10+int(y),ns)
    if result:
        total += 1
        l += lst

l = list(set(l))
l.sort()
print(l)
print(len(l)) # answer
print(total)
print(time()-start)
