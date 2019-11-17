limit = 1000
sum = 0
for x in range(limit):
	if x % 3 == 0:
		sum += x
	elif x % 5 == 0:
		sum += x

print("The answer is")
print(sum)
