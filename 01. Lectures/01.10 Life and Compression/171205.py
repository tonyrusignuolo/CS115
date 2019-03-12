def euler1():
    total = 0
    for x in range(1000):
        if x % 3 == 0 or x % 5 == 0:
            total += x
    return total

def euler2():
    a = 1
    b = 2
    c = 3
    total = 2
    while c < 4000000:
        a = b
        b = c
        c = a + b
        if c % 2 == 0:
            total += c
    return total

def primeFactor(n):
    i = 2
    maxFactor = n ** .5
    pfList = []
    while i <= maxFactor:
        if n % i == 0:
            pfList.append(i)
            n //= i
            maxFactor = n ** .5
        else:
            i += 1
    pfList.append(n)
    return pfList