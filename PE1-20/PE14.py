def even_num(n):
    return n/2

def odd_num(n):
    return 3*n+1

lst = []
dct = {}
for i in range(1,1000001):
    num = i
    count = 1
    while num != 1:
        if num in dct.keys():
            count += dct[num]
            break
        elif num%2==0:
            num = even_num(num)
            count += 1
        else:
            num = odd_num(num)/2
            count += 2
    lst.append(count)
    dct[i] = count

print(lst.index(max(lst))+1)
