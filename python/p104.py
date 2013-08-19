def last10fibo():
    a, b = 0, 1
    i = 0
    while True:
        a, b = b, (a+b)%10**10
        i += 1
        yield a, i

def ispand(n):
    return set('123456789') == set(str(n))

from math import sqrt, log

def first10(i):
    phi = (1 + sqrt(5))/2
    logf = i*log(phi, 10) - 0.5*log(5, 10)
    return int(10**(logf - int(logf)+8))


for a, i in last10fibo():
    if ispand(a) and ispand(first10(i)):
        print i
        break
