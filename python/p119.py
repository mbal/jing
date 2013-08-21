DIGITS = 21
KMAX = 10
l = []

def sumDigits(n):
    s = 0
    while n > 0:
        s += n%10
        n /= 10
    return s

import time

t= time.time()

for i in range(2, 9*(DIGITS + 1)):
    for e in range(2, KMAX):
        n = i**e
        if sumDigits(n) == i:
            l.append(n)

l = sorted(list(set(l)))
for i, v in enumerate(l, start=1):
    print i, v
