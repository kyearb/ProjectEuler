import numpy as np

def triangle(n):
    return n*(n+1) # n^2+n

def pentagon(n):
    return n*(3*n-1) # 3n^2-n

def hexagon(n):
    return n*(2*n-1)*2 # 4n^2-2n

def quad(a, b, c):
    return (-b + np.sqrt(b*b - 4*a*c))/(2*a)

def reverseTri(x):
    return quad(1, 1, -x)

def reversePent(x):
    return quad(3, -1, -x)

def reverseHex(x):
    return quad(4, -2, -x)

if __name__=='__main__':
    i = 285
    # tri = triangle(285)
    # print(tri)
    # print(reversePent(tri))
    # print(reverseHex(tri))

    while True:
        i += 1
        tri = triangle(i)
        rPent = reversePent(tri)
        rHex = reverseHex(tri)
        if rPent==np.round(rPent) and rHex==np.round(rHex):
            break

    print('Triangle number is: {:d}'.format(tri//2))
