num = 2*3*5*7*11*13*17*19
found = False
while not found:
	if num%16==0 and num%9==0 and num%5==0 and num%7==0 and num%11==0 and num%13==0 and num%17==0 and num%19==0:
		found = True
	else:
		num += 1

print(num)

#multiplying greatest powers of primes is a lot faster/easier
