def isSunday(day):
	retVal = False
	if day%7==0:
		retVal = True
	return retVal

def isLeapYear(year):
	retVal = False
	if year%400==0 or (year%4==0 and year%100!=0):
		retVal = True
	return retVal

def firstofMonth(year):
	leapYear = isLeapYear(year)
	feb = 28
	if leapYear:
		feb += 1
	first_list = [1, 32, 32+feb, 63+feb, 93+feb, 124+feb, 154+feb, 185+feb, 216+feb, 246+feb, 277+feb, 307+feb]
	return first_list


day = 365
count = 0
for year in range(1901,2001):
	l = firstofMonth(year)
	for i in l:
		if isSunday(i+day):
			count += 1
	day += 365
	if isLeapYear(year):
		day += 1

print(count)
