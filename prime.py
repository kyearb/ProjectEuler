import numpy as np
import numba
import pdb

@numba.njit()
def primeList(lim):
    numlst = np.arange(lim)
    plst = np.full(lim, True)
    plst[0:2] = False
    for i in range(lim):
        if plst[i]:
            for j in range((lim//i)-2):
                plst[(j+2)*i] = False
    return numlst[plst]

@numba.njit
def isPrime(num):
    if num == 2:
        return True
    elif num <2:
        False
    else:
        for i in range(2,np.int(np.sqrt(num))):
            if num % i == 0:
                return False
        return True

@numba.njit
def primeSieve(n):
    sieve = np.ones(n//2, dtype=np.int8) # allocate enough space for all odd numbers
    for i in range(3,n,2): # i is the number that is checked
        if sieve[i//2]: # i is stored in i/2
            j = i*i//2 # next non-prime is at i^2; before that is redundant
            while j < n:
                sieve[j//2] = 0 # set to false
                j += i # next number
    primes = sieve.nonzero()[0]*2+1 # convert indices to primes
    primes[0] = 2 # change first prime from 1 to 2
    return primes

def primeWheel(n, primes=[2,3, 5]):
    wheelSize = 1
    i = 0
    primes = np.array(primes)
    wheelSize = np.product(primes)
    # while wheelSize+1 <= primes[-1]:
    #     wheelSize *= primes[i]
    #     i += 1
    basis = len(primes)
    wheel = np.ones(wheelSize+2, dtype=np.int8) # create wheel from 0 to wheelsize + 1
    wheel[:2] = 0
    # sieve
    for i in range(2,wheelSize+2):
        j = i*i
        if j > wheelSize:
            break
        elif wheel[i]:
            while j < wheelSize+1:
                wheel[j] = 0
                j += i
    # get primes
    wheelprimes = wheel.nonzero()[0][basis:]
    pdb.set_trace()
    # diff = np.concatenate((np.diff(wheelprimes), [wheelSize]))
    cols = len(wheelprimes)
    rows = wheelprimes[0] # or n//wheelSize
    # relativePrimes = np.full((rows,cols), wheelSize) * np.array([range(rows), range(rows)]).T + primes
    relativePrimes = np.ones(rows*cols, dtype=np.int8)
    maxPrime = (rows-1)*wheelSize+wheelprimes[cols-1]
    for i in range(rows*cols):
        j = i//cols*wheelSize + wheelprimes[i%cols]
        k = j*j
        if k > maxPrime:
            break
        elif relativePrimes[i]:
            while k < maxPrime:
                if (k%primes!=0).all():
                    tmp = (k-k%wheelSize)//wheelSize*cols + np.where(wheelprimes==k%wheelSize)[0][0]
                    print(tmp//cols*wheelSize + wheelprimes[tmp%cols])
                    relativePrimes[(k-k%wheelSize)//wheelSize*cols + np.where(wheelprimes==k%wheelSize)[0][0]] = 0
                k += j

    # for i in range(rows):
    #     for j in range(cols):
    #         candidate = i*wheelSize + wheelprimes[j]
    #         k = candidate*candidate
    #         if k > (rows-1)*wheelSize+wheelprimes[-1]:
    #             break
    #         if relativePrimes[i,j]:
    #             primes.append(candidate)
    #             while k < ((rows-1)*wheelSize + wheelprimes[cols-1]):
    #                 if k%wheelSize!=0:
    #                     relativePrimes[k//wheelSize-1, np.where(wheelprimes==k%wheelSize)] = 0
    #                 k += candidate
    #             print(candidate)
    indices = relativePrimes.nonzero()
    return indices[0]//cols*wheelSize + wheelprimes[indices[0]%cols]
    # return wheelSize*indices[0] + wheelprimes[indices[1]]



if __name__=='__main__':
    a = primeWheel(10)
    print(a)
