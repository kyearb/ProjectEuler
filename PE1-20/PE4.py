def palindrome(number):
	num_str=str(number)
	if num_str==num_str[::-1]:
		return True
	else:
		return False

pal = []
for x in range(100,1000):
	for y in range(x,1000):
		num = x*y
		if palindrome(num):
			pal.append(num)

print(max(pal))
