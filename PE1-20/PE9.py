import math
a = 0
b = 1
c = 0
while a+b+c!=1000:
	a += 1
	if a>499:
		b += 1
		a = b
	c = math.sqrt(a**2+b**2)
	if b>499:
		print("Failed Test")
		break

print(a+b+c)
print(a*b*c)
