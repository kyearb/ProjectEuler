import numpy as np
import numba

def isPrime(num):
	prime = True
	i = 2
	while prime and i<num:
		if num%i!=0:
			i += 1
		else:
			prime = False
	return prime

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

if __name__=="__main__":
    # count = 0
    # i = 2
    # while count<10001:
    # 	if isPrime(i):
    # 		num = i
    # 		count += 1
    # 	i += 1
    num = primeList(1000000)[10000]

    print(num)
