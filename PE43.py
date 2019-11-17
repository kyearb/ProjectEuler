import numpy as np
import numba
from itertools import permutations
from prime import primeList

def isPanDigital(num):
    numStr = str(num).sort()
    retVal = True
    for i in range(len(numStr)):
        if i != int(numStr[i]):
            retVal = False
            break
    return retVal

if __name__=='__main__':
    panDigitalListGen = permutations(range(10))
    panDigitalList = []
    plst = primeList(18)
    for gen in panDigitalListGen:
        if gen[0] != 0:
            panDigitalList.append(''.join([str(i) for i in gen]))

    panSum = 0
    for panDig in panDigitalList:
        addPan = True
        for i in range(1,8):
            if int(panDig[i:i+3]) % plst[i-1] == 0:
                pass
            else:
                addPan = False
                break
        if addPan:
            panSum += int(panDig)

    print(panSum)
