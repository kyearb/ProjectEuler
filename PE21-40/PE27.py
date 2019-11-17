
def prime_list(n):
	prime_list = []
	prime_list.append(2)
	for i in range(3,n+1,2):
		prime = True
		for j in prime_list:
			if j**2>i:
				break
			elif i%j==0:
				prime = False
				break
		if prime:
			prime_list.append(i)
	return prime_list


primelist = set(prime_list(10000))
nmax = 0
prod = 0
for a in range(-999,1000):
	for b in range(-999,1000):
		if b not in primelist:
			continue
		prime = True
		n = 0
		while prime:
			result = n**2+n*a+b
			if result not in primelist:
				prime = False
			else:
				n += 1
		if n>nmax:
			nmax = n
			prod = a*b

print(prod)
