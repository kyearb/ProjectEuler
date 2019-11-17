import numpy as np
from useful import is_prime

if __name__=='__main__':
    found = False
    n = 35
    x = 1
    while not found:
        x = 1
        found = True
        p = n-2*x*x
        while p > 0:
            if is_prime(p):
                found = False
                break
            else:
                x += 1
                p = n-2*x*x
        if not found:
            n += 2
            while is_prime(n):
                n += 2
    print(n)
