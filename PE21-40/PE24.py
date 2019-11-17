from time import time
from functools import reduce

num = '0123456789'

def fact(n):return reduce(lambda x,y:x*y,[1]+list(range(1,n+1)))

def perm(n):
	indicies = []
	for x in range(9,-1,-1):
		indicies.append(n//fact(x))
		n = n%fact(x)
	numbers = list(range(10))
	result = ''
	for i in indicies:
		result += str(numbers.pop(i))
	return result

print(perm(999999))

"""
my method, very inefficient

def combine_list(str_list):
	for i in range(len(str_list)):
		if i==0:
			nstr = str_list[i]
		else:
			nstr += str_list[i]
	return nstr

def move_index(str_list,index1,index2):
	count = 0
	temp = ''
	new_list = ''
	for i in str_list:
		if count==index1:
			temp = i
		elif count!=index2:
			new_list += i
		elif count==index2:
			new_list += i+temp
		count += 1
	return new_list

start = time()

num_list = []
num_list.append(num)

#switch n! times total
#for j in range(0,):
j = 0
for i in range(fact(10)+1):
	temp_list = num_list[i+j]
	if i%fact(3)==0 and i!=0:
		num_list.append(move_index(temp_list,6,9))
		j += 1
		temp_list = num_list[i+j]
	if i%fact(4)==0 and i!=0:
		num_list.append(move_index(temp_list,5,9))
		j += 1
		temp_list = num_list[i+j]
	if i%fact(5)==0 and i!=0:
		num_list.append(move_index(temp_list,4,9))
		j += 1
		temp_list = num_list[i+j]
	if i%fact(6)==0 and i!=0:
		num_list.append(move_index(temp_list,3,9))
		j += 1
		temp_list = num_list[i+j]
	if i%fact(7)==0 and i!=0:
		num_list.append(move_index(temp_list,2,9))
		j += 1
		temp_list = num_list[i+j]
	if i%fact(8)==0 and i!=0:
		num_list.append(move_index(temp_list,1,9))
		j += 1
		temp_list = num_list[i+j]
	if i%fact(9)==0 and i!=0:
		num_list.append(move_index(temp_list,0,9))
		j += 1
		temp_list = num_list[i+j]
	if i%2==0:
		num_list.append(move_index(temp_list,8,9))
	else:
		num_list.append(move_index(temp_list,7,8))

final_set = set(num_list)
final_list = map(lambda x:int(x),list(final_set))
final_list.sort()
for i in final_list:
	print i

print ''
print '%s seconds to complete' %(time()-start)
print final_list[999999]
"""
