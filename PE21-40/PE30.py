def sum_digit_powers(n):
	result = 0
	num = n
	while n!=0:
		result += (n%10)**5
		n //= 10
	if num==result:
		return True
	else:
		return False

#find rough max
for i in range(1,10):
	if (9**5)*i<10**i:
		max_val = (9**5)*i
		break

l = []
for i in range(2,max_val):
	if sum_digit_powers(i):
		l.append(i)

print(sum(l))
