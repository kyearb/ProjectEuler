from functools import reduce
# def factorial(n):return reduce(lambda x,y:x*y,[1]+list(range(1,n+1)))

def factorial(num):
    if num > 1:
        return num*factorial(num-1)
    else:
        return 1


n = str(factorial(100))

print(sum([int(n[i]) for i in range(len(n))]))
