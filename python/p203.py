# Are we sure? Yep. C(n, k) is divisible only by primes <= n.
# A sieve is a bit of an overkill, though.
sqprimes = [x*x for x in 
        [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]]
ssqprimes = set(sqprimes)

import math

def C(n, k):
    return math.factorial(n) / (math.factorial(k) * math.factorial(n-k))

def squarefree(n):
    i = 0
    if n in ssqprimes:
        return False
    while i < len(sqprimes) and sqprimes[i] <= n:
        if n % sqprimes[i] == 0:
            return False
        i += 1
    return True

c = 0
lines = 51
sqfree = set([1])
for i in range(lines+1):
    for n in range(i):
        for k in range(1, n/2 + 2):
            try:
                cnk = C(n, k)
            except:
                continue
            if squarefree(cnk):
                sqfree.add(cnk)

print sum(sqfree)
