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

# It's the simplest algorithm written in http://arxiv.org/pdf/1107.4890v1.pdf
def squaresieve(n):
    mu = [1 for x in xrange(n+1)]
    primes = sieve(n)
    for p in primes:
        p2 = p * p
        k = p2
        while k < n+1:
            mu[k] = 0
            k += p2
        k = p
        while k < n+1:
            mu[k] = -mu[k]
            k += p
    return mu


N = 2**50

mu = squaresieve(int(N**.5) + 1)
# Not using explicit loops speeds up considerabily, but it's still slow.
print sum(mu[d] * int(N/(d*d)) for d in xrange(1, int(N**.5)))
# It takes about 80 seconds, which is good, considering the magnitude of the
# result. However, 30 seconds are spent in the line above, while ~40 are
# really useful to solve the problem (namely generate the primes, and compute
# the moebius function).
