def sieve(n):
    m = (n-1) // 2
    b = [True]*m
    i,p,ps = 0,3,[2]
    while p*p < n:
        if b[i]:
            ps.append(p)
            j = 2*i*i + 6*i + 3
            while j < m:
                b[j] = False
                j = j + 2*i + 3
        i+=1; p+=2
    while i < m:
        if b[i]:
            ps.append(p)
        i+=1; p+=2
    return ps

#def sigma2(n):
#    i = 0
#    l = []
#    L = len(primes)
#    while i < L and primes[i] <= n:
#        c = 0
#        while n % primes[i] == 0:
#            c += 1
#            n /= primes[i]
#        if c > 0:
#            l.append((primes[i], c))
#        i += 1
#    if l == []:
#        l.append((n, 1))
#    # list comprehension / reduce
#    def f((p, n)):
#        return (p**(2*(n + 1)) - 1) / (p*p  - 1)
#    return reduce(__mul__, map(f, l))
#

LIMIT = 64*1000
sigma2 = [0 for x in xrange(LIMIT)]
perfect_squares = set(x*x for x in xrange(10**5))
c = 0
MAXS = 10**10

primes = sieve(int(LIMIT**.5) + 1)
for p in primes:
    for i in range(p*p, LIMIT, p):
        sigma2[i] = p

sigma2[1] = 1
for i in xrange(2, LIMIT):
    if sigma2[i] == 0:
        sigma2[i] = i * i + 1
    else:
        p = sigma2[i]
        k = i / p
        e = 2
        while k % p == 0:
            k /= p
            e += 1
        sigma2[i] = int(sigma2[k] * (p**(2*e) - 1) / float(p*p - 1))

perfect_squares = set(x*x for x in xrange(10**5))
MAXS = 10**10
for i in xrange(LIMIT):
    if sigma2[i] in perfect_squares:
        c += i
    else:
        if sigma2[i] >= MAXS:
            sq = sigma2[i]**.5
            if int(sq) == sq:
                c += i
print c
