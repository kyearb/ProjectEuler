import numpy as np
d = range(1,1001)

lst = []
for i in d:
	x = str(int(10**10000)//i)
	l = x[100:105]
	for num in range(105,len(x)-5):
		if l==x[num:num+5]:
			lst.append([i,num-100])
			break

for i in range(len(lst)):
	print(lst[i][0], lst[i][1])

result = 0
max_length = 0
for i in range(len(lst)):
	if lst[i][1]>max_length:
		result = lst[i][0]
		max_length = lst[i][1]

print(result)
