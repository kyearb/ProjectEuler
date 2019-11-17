def triangle_number(number):
	total = 0
	for i in range(1,number+1):
		total += i
	return total

prime_list = []
prime_list.append(2)
for i in range(3,10000):
	prime = True
	for j in prime_list:
		if j**2>i:
			break
		elif i%j==0:
			prime = False
			break
	if prime:
		prime_list.append(i)

def num_divisors(number,prime_list):
	count = 1
	for i in prime_list:
		if i>number:
			break
		pow = 0
		num_sub = number
		while num_sub%i==0:
			pow += 1
			num_sub /= i
		if pow>0:
			pow += 1
			count *= pow
	if count==1:
		count = 2
	return count

x = 1
num_div = 0
while num_div<=500:
	tri_num = triangle_number(x)
	num_div = num_divisors(tri_num,prime_list)
	x += 1

print(tri_num)
