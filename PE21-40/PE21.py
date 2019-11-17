def div_list(n):
	return [i for i in range(1,n) if n%i==0]

def amicable(n):
	retVal = False
	num = sum(div_list(n))
	if n==sum(div_list(num)) and n!=num:
		retVal = True
	return retVal

l = []
for i in range(1,10000):
	try:
		l.index(i)
		continue
	except ValueError:
		if amicable(i):
			l.append(i)
			l.append(sum(div_list(i)))

print(sum(l))
print(l)
