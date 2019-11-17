from time import time


def is_9pandigital(num_str):
    boolean = False
    lst = list(num_str)
    lst.sort()
    newstring = ''
    for i in lst:
        newstring += i
    if newstring=='123456789':
        boolean = True
    return boolean


def concatanate(num):
    mult = 1
    string = ''
    while len(string)<9:
        string += str(num*mult)
        mult += 1
    return string


start = time()
limit = 10**4-1
result = False
while not result:
    l = concatanate(limit)
    if len(l)==9:
        result = is_9pandigital(l)
    if not result:
        limit -= 1


print(limit)
print(l)
print(time() - start)
