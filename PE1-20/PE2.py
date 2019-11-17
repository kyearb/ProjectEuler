fib1 = 1
fib2 = 2
sum = fib2

while fib2 <= 4000000:
	x = fib2
	fib2 += fib1
	fib1 = x

	if fib2 % 2 == 0:
		sum += fib2

print("The answer is")
print(sum)
