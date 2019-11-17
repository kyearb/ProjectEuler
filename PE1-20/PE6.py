def sum_of_squares(n):
	sum = 0
	for x in range(1,n+1):
		sum += x**2
	return sum

def square_of_sums(n):
	sum = (n**2+n)/2
	sum = sum**2
	return sum

dif = square_of_sums(100)-sum_of_squares(100)
print(dif)
