import time

start = time.time()

l = []
l.append(2)
for i in range(3,2000001):
	prime = True
	for j in l:
		if j**2>i:
			break
		elif i%j==0:
			prime = False
			break
	if prime:
		l.append(i)

sum = 0
for k in l:
	sum += k

# print(time.time()-start)
print(sum)
