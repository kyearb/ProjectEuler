num = 600851475143
x = 2
while x < num:
	if num % x == 0:
		num = num/x
	else:
		x += 1

print("The answer is")
print(x)
