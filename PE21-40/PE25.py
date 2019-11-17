from time import time

def fib(list):
	i = len(list)
	if i<2:
		return 1
	else:
		return list[i-2]+list[i-1]


start = time()

num = 0
fib_list = []
while num//(10**999)<1:
	fib_list.append(fib(fib_list))

	num = fib_list[-1]

print(fib_list)
print(fib_list.index(fib_list[-1])+1)
