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

primes = sieve(10**3)

def factor(n, d=False):
    i = 2
    res = []
    if n in primes:
        return [(n, 1)]
    for i in primes:
        if i * i > n:
            if n > 1:
                res.append((n, 1))
            return res
        c = 0
        while n % i == 0:
            c+=1
            n /= i
        if c != 0:
            res.append((i, c))
    if d:
        print n
    if n > 1:
        res.append((n, 1))
    return res

def divisors(n):
    pri_fact = factor(n)
    r = 1
    for (p, n) in pri_fact:
        r *= 2*n+1
    return r

for n in xrange(10**6, 10**8):
    count = (divisors(n)+1)
    if count > 4*10**6:
        print n, count/2
        break

