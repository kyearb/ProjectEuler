from time import time


def prime_numbers(limit=1000000):
    '''Prime number generator. Yields the series
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29 ...
    using Sieve of Eratosthenes.
    '''
    yield 2
    sub_limit = int(limit**0.5)
    flags = [True, True] + [False] * (limit - 2)
    # Step through all the odd numbers
    for i in range(3, limit, 2):
        if flags[i]:
            continue
        yield i
        # Exclude further multiples of the current prime number
        if i <= sub_limit:
            for j in range(i*i, limit, i<<1):
                flags[j] = True


def is_truncatable(n):
    result = True
    num1 = n
    num2 = n
    power = len(str(n))-1
    if power==0:
        result = False
    while len(str(num1))>1:
        num1 = num1%(10**power)
        num2 //= 10
        if num1 in primeset and num2 in primeset:
            pass
        else:
            result = False
            break
        power -= 1
    return result


primes = []
for prime in prime_numbers(1000000):
    primes.append(prime)

primeset = set(primes)
l = []

for i in primes:
    result = is_truncatable(i)
    if result:
        l.append(i)

print(sum(l))
print(len(l))
print(l)
