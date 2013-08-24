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

# (10^k - 1) / 9 = 0 (mod p)
# (10^k - 1) = 0 (mod p)
# 10^k = 1 (mod p)

primes = sieve(10**6)

c = 0
s = 0
i = 2
while c < 40:
    if pow(10, 10**9, primes[i]) == 1:
        c += 1
        print primes[i]
        s += primes[i]
    i += 1

print s

