CACHE = [0 for x in range(10**6)]
import itertools
def amic(n):
    if n == 1:
        return 1
    if CACHE[n] != 0:
        return CACHE[n]
    p = []
    i = 2
    ori = n
    while n > 1:
        while n % i == 0:
            n /= i
            p.append(i)
        i += 1
        if i*i > n:
            break
    if n!= 1:
        p.append(n)
    pi = itertools.groupby(p)
    s = 1
    for i, grp in pi:
        grp = list(grp)
        s *= (i**(len(grp)+1) - 1)/(i-1)

    CACHE[ori] = s - ori
    return s-ori

maxx = 0
best = []
for i in xrange(3, 10**6):
    enc = []
    n = i
    while n not in enc:
        enc.append(n)
        if n > 10**6:
            break
        n = amic(n)
    if enc[0] == n:
        if len(enc) > maxx:
            maxx = len(enc)
            best = enc
print best
