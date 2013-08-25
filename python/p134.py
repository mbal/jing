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


import math
primes = sieve(10**6+10)

c = 0

for i in xrange(2, len(primes)-1):
    p1 = primes[i]
    p2 = primes[i+1]

    lenp1 = int(math.log(p1, 10)) + 1
    mod = 10**lenp1

    S = ((p2 - p1)*pow(10, lenp1*(p2 - 2), p2)) % p2
    c += S*mod + p1

print c
