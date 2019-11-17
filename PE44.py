import numpy as np
from PE44cy import pentagonNumber, reversePentagon, isPentagon

def findPenta(pentaList):
    num = -1
    for i in range(len(pentaList)):
        for j in range(i+2,len(pentaList)):
            tmpDiff = pentaList[j]-pentaList[i]
            tmpSum = pentaList[i]+pentaList[j]
            if isPentagon(tmpDiff) and isPentagon(tmpSum):
                if num == -1:
                    num = tmpDiff
                elif tmpDiff < num:
                    num = tmpDiff
    return num

if __name__=='__main__':
    pentaList = [pentagonNumber(i+1) for i in range(2167)]
    print(findPenta(pentaList))
'''
solution: 5482660
'''

# n(3n-1) + m(3m-1) = l(3l-1)
# n(3n-1) + (n+i)(3(n+i)-1) = (n+j)(3(n+j)-1)
# n(3n-1) + (n+i)(3n-1+3i)
# n(3n-1) + n(3n-1) + i(3n-1) + 3i(n+i) = n(3n-1) + j(3n-1) + 3j(n+j)
# n(3n-1) + n(3n-1) + i(3n-1) + 3i(n+i) = n(3n-1) + k(3n-1) + 3k(n+k)
# (n+i)(3(n+i)-1) - n(3n-1) = (n+k)(3(n+k)-1)
