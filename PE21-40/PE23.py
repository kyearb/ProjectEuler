from math import floor
from math import sqrt

def div_list(n):
    div = []
    div.append(1)
    for i in range(2,int(floor(sqrt(n))+1)):
        if n%i==0:
            div.append(i)
            div.append(n//i)
    retList = list(set(div))
    return retList

def abundant(n):
    return n<sum(div_list(n))

l = [i for i in range(1,28124) if abundant(i)]
print("l done")

l2 = []
for i in range(0,len(l)):
    for j in range(i,len(l)):
        if l[i]+l[j]>28124:
            continue
        l2.append(l[i]+l[j])
l2.sort()
l2s = set(l2)
print("l2 done")

l1s = set(range(1,28124))

l3 = l1s-l2s

print(sum(l3))
