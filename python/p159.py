def drss(n):
    return 1+(n-1)%9

LIMIT = 10**6
MDRS = [0 for x in xrange(LIMIT)]

for p in range(2, LIMIT):
    if MDRS[p] == 0:
        MDRS[p] = drss(p)
    n = p << 1
    k = 2
    while n < LIMIT:
        MDRS[n] = max(drss(n), MDRS[k] + MDRS[p], MDRS[n])
        n += p
        k += 1

print sum(MDRS)
