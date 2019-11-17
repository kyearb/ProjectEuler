import numpy as np
import dask.array as ds
import numba
import h5py
import pdb, time
from itertools import takewhile, count
from prime import primeSieve

divList = {1:[1]}
divList_jit = {1:[1]}
divLen = {}

# def generator():
#     """returns a generator that yields an infinite list of primes"""
#     return filter(
#         lambda n, Primes=[]:
#             all(n%p for p in
#                 takewhile(lambda p, s=n**0.5: p <= s, Primes)
#             ) and not Primes.append(n),
#         count(2)
#     )

def primes(n):
    p = h5py.File('primes.h5', 'a')
    if p.keys() != None:
        sieve = da.from_array(p['sieve'])
        prime = da.from_array(p['prime'])
    else:
        sieve = da.from_array(p.create_dataset('sieve', (10**12,), dtype='bool', chunks=True))
        prime = da.from_array(p.create_dataset('prime', dtype='i8'))
        sieve[:] = True
        sieve[:2] = False
        prime[0] = 2
        for j in range(2, h5py.get_vlen(sieve)):
            sieve[2*j] = False

    if n < prime[-1]:
        return sieve[:n]
    else:
        for i in range(2,n):
            if sieve[i]:
                j = i + 1
                while j < n:
                    array[j] = False
                    j += i

@numba.njit('b1(i8,i8[:])')
def isPrime(n, primeList):
    for prime in primeList:
        if prime**2 > n:
            return True
        elif n%prime == 0:
            return False
    return True

def divisorLen(m):
    i = 2
    length = 1
    count = 1
    while m%i == 0:
        m //= i
        count += 1
    length *= count
    count = 1
    i += 1
    while i <= m:
        if m%i == 0:
            m //= i
            count += 1
        else:
            length *= count
            count = 1
            i += 2
    length *= count
    return length

global primeList
primeList = primeSieve(10**7)

def divisorLenPrimes(m):
    i = 0
    length = 1
    count = 1
    prime_len = len(primeList)
    prime = primeList[i]
    while prime <= m:
        if m%prime == 0:
            m //= prime
            count += 1
        else:
            length *= count
            count = 1
            i += 1
            if i >= prime_len:
                prime += 2 # use every odd number
            else:
                prime = primeList[i]
    length *= count
    return length

# @numba.jit
# def divisorList_jit(m):
#     if m in divList_jit.keys():
#         l = divList_jit[m]
#     else:
#         l = []
#         l.append(1)
#         l.append(m)
#         for i in range(2,m):
#             if i**2 > m:
#                 break
#             if m%i==0:
#                 l.append(i)
#                 if i != m//i:
#                     l.append(m//i)
#         divList_jit[m] = l
#     return l

def divisorList(m):
    if m in divList.keys():
        l = divList[m]
    else:
        l = []
        l.append(1)
        l.append(m)
        for i in range(2,m):
            if i**2 > m:
                break
            if m%i==0:
                l.append(i)
                if i != m//i:
                    l.append(m//i)
                if m//i in divList.keys():
                    [l.append(d) for d in divList[m//i] if not d in l]
                    [l.append(i*d) for d in divList[m//i] if not d in l]
                    break
        divList[m] = l
    return l

@np.vectorize
def sigma(n):
    if n in divLen.keys():
        length = divLen[n]
    else:
        length = divisorLenPrimes(n)
        divLen[n] = length
    return length

def D(m,n, mod=0):
    ret = 0
    d = np.array(divisorList(m)).reshape((-1,1))
    k = np.array(range(n)).reshape(1,-1) + 1
    dk = (d*k).ravel()
    ret = np.sum(sigma(dk))
    # for n in range(len(dk)):
    #     ret += sigma(dk[n])
    #     if mod != 0 and ret >= mod:
    #         ret -= mod
    return ret

def factorial(n):
    if n > 1:
        return n*factorial(n-1)
    else:
        return 1

if __name__=="__main__":
    # print(len(str(10**12)))
    # a = factorial(200)*10**12
    # print(a)
    # vfunc = np.vectorize(sigma)
    # print(sigma(np.array([21003, 337])))
    # print(len(divisorList(20130)))
    # print(divisorLen(factorial(200)*10**12))
    # print(divisorLen(10**12))
    # print(isPrime(25, np.array([2,3,5,7,11,13,17,19,23,29])))
    # n = [factorial(i) for i in range(200)]
    # print(len(primeSieve(5761456)))
    # print(primeSieve(5761456))


    print(D(factorial(3), 10**2))
    # print(D(factorial(4), 10**6))
    # num = D(factorial(200), 10**12)
    # ret = num % (10**9 + 7)
    # print(num)
    # print(ret)
