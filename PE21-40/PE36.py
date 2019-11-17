from time import time

def dec_to_binary(n):
    p = 0
    num = n
    while n>=2**p:
        p += 1
    p -= 1
    num_str = ''
    for i in range(p,-1,-1):
        if num-2**i>=0:
            num_str += '1'
            num -= 2**i
        else:
            num_str += '0'
    return num_str


def is_palindrome(num_str):
    result = False
    if num_str==num_str[::-1]:
        result = True
    return result

num = 0
l = []
for i in range(1,1000000):
    n = str(i)
    if is_palindrome(n):
        if is_palindrome(dec_to_binary(i)):
            num += i
            l.append([i,dec_to_binary(i)])

print(num)
for i in l:
    print(i)
