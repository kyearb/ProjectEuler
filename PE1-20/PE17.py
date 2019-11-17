numbers = {0:'',\
1:"one",\
2:'two',\
3:'three',\
4:'four',\
5:'five',\
6:'six',\
7:'seven',\
8:'eight',\
9:'nine',\
10:'ten',\
11:'eleven',\
12:'twelve',\
13:'thirteen',\
14:'fourteen',\
15:'fifteen',\
16:'sixteen',\
17:'seventeen',\
18:'eighteen',\
19:'nineteen',\
20:'twenty',\
30:'thirty',\
40:'forty',\
50:'fifty',\
60:'sixty',\
70:'seventy',\
80:'eighty',\
90:'ninety',\
100:'hundred',\
1000:'onethousand'
}

def letter_count(num):
	total = 0
	hundreds = num//100
	tens = num//10 - hundreds*10
	ones =  num%10
	if tens==1:
		total += len(numbers[ones+tens*10])
	else:
		total += len(numbers[tens*10])+len(numbers[ones])
	if hundreds!=0:
		total += len(numbers[hundreds])+len(numbers[100])
		if tens!=0 or ones!=0:
			total += 3
	return total

count = 0
for i in range(0,1001):
	if i==1000:
		count += len(numbers[1000])
	else:
		count += letter_count(i)


print(count)
