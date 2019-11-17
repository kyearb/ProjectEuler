from useful import prime_list, div_list

# primes = prime_list()
# def div_list(n):
#     div = []
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             div.append(i)
#             div.append(n // i)

#     div = set(div)
#     div = list(div)
#     div.sort()
#     return div

if __name__=='__main__':
    primes = prime_list(1000000)
    found = False
    x = int(2*3*5*7)
    lst = []
    lst.append([i for i in div_list(x) if i in primes])
    lst.append([i for i in div_list(x+1) if i in primes])
    lst.append([i for i in div_list(x+2) if i in primes])
    x += 3
    while not found:
        lst.append([i for i in div_list(x) if i in primes])
        if len(lst[3])==4 and len(lst[2])==4 and len(lst[1])==4 and len(lst[0])==4:
            print(x-3)
            found = True
        else:
            lst.pop(0)
            x += 1