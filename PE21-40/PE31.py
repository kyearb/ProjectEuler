coins = [1,2,5,10,20,50,100,200]

count = 0
value = 200

def coin_recursion(num,total):
	if num==0: return 1
	answer = 0
	i = total/coins[num]
	for i in range(total//coins[num],-1,-1):
		answer += coin_recursion(num-1,total-i*coins[num])
	return answer

count = coin_recursion(len(coins)-1,200)

#
# num200 = value/coins[7]
# while True:
# 	value = 200 - num200*coins[7]
# 	num100 = value/coins[6]
# 	while True:
# 		value = 200 - num200*coins[7] - num100*coins[6]
# 		num50 = value/coins[5]
# 		while True:
# 			value = 200 - num200*coins[7] - num100*coins[6] - num50*coins[5]
# 			num20 = value/coins[4]
# 			while True:
# 				value = 200 - num200*coins[7] - num100*coins[6] - num50*coins[5] - num20*coins[4]
# 				num10 = value/coins[3]
# 				while True:
# 					value = 200 - num200*coins[7] - num100*coins[6] - num50*coins[5] - num20*coins[4] - num10*coins[3]
# 					num5 = value/coins[2]
# 					while True:
# 						value = 200 - num200*coins[7] - num100*coins[6] - num50*coins[5] - num20*coins[4] - num10*coins[3] - num5*coins[2]
# 						num2 = value/coins[1]
# 						while True:
# 							value = 200 - num200*coins[7] - num100*coins[6] - num50*coins[5] - num20*coins[4] - num10*coins[3] - num5*coins[2] - num2*coins[1]
# 							if num200>-1 and num100>-1 and num50>-1 and num20>-1 and num10>-1 and num5>-1 and num2>-1:
# 								count += 1
# 							if num2>=0:
# 								num2 -= 1
# 							else: break
# 						if num5>=0:
# 							num5 -= 1
# 						else: break
# 					if num10>=0:
# 						num10 -= 1
# 					else: break
# 				if num20>=0:
# 					num20 -= 1
# 				else: break
# 			if num50>=0:
# 				num50 -= 1
# 			else: break
# 		if num100>=0:
# 			num100 -= 1
# 		else: break
# 	if num200>=0:
# 		num200 -= 1
# 	else: break

print(count)
