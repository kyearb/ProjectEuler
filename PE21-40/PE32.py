from time import time

def num_to_str(num):
    lst = []
    count = 0
    while num%10!=0:
        lst.append(num%10)
        num //= 10
    return lst

def pandigital(num1,num2):
    result = False
    nums = range(1,10)
    num3 = num1*num2
    lst = num_to_str(num1) + num_to_str(num2) + num_to_str(num3)
    if len(lst)==9:
        try:
            lst.remove(0)
        except ValueError:
            if len(set(lst))==9:
                result = True
    return result

start = time()

l = []
for i in range(1,100):
    if len(num_to_str(i))!=len(set(num_to_str(i))):
        continue
    if i//10==0:
        num_max = 10000
        num_min = 1000
    else:
        num_max = 1000
        num_min = 100
    for j in range(num_min,num_max):
        if pandigital(i,j):
            try:
                l.index(i*j)
            except ValueError:
                l.append(i*j)

print(sum(l))
print(time()-start)

#method 2 from comments
start = time()
sols = set()

for i in range(1000,10000):
    for j in range(2,100):
        if i % j == 0:
            k = i // j
            s = str(i) + str(j) + str(k)
            if len(s) == 9 and ''.join(sorted(s)) == '123456789':
                sols.add(i)


print(sum(sols))
print(time()-start)
