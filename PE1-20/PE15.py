def fact(num):
    product = 1
    for i in range(1,num+1):
        product *= i
    return product

def recfact(num):
    if num > 1:
        return num*quickfact(num-1)
    else:
        return 1


ans = fact(40)/(fact(20)**2)

print(ans)
