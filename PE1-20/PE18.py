import time

num = []
num.append([75])
num.append([95, 64])
num.append([17, 47, 82])
num.append([18, 35, 87, 10])
num.append([20, 4, 82, 47, 65])
num.append([19, 1, 23, 75,3, 34])
num.append([88, 2, 77, 73, 7, 63, 67])
num.append([99, 65, 4, 28, 6, 16, 70, 92])
num.append([41, 41, 26, 56, 83, 40, 80, 70, 33])
num.append([41, 48, 72, 33, 47, 32, 37, 16, 94, 29])
num.append([53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14])
num.append([70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57])
num.append([91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48])
num.append([63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31])
num.append([4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23])

"""each number has a preference, left or right
start at the bottom, add to top number depending on the preference
keep adding to higher number until the top is reached"""

def largest_path(num):
	for i in range(len(num)-1):
		for j in range(len(num)-1-i):
			num[len(num)-2-i][j] += max(num[len(num)-1-i][j],num[len(num)-1-i][j+1])
	return num[0][0]

start = time.time()

print(largest_path(num))
