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

def isprime(n):
    i = 0
    if n == 1:
        return False
    while primes[i]*primes[i] <= n:
        if n % primes[i] == 0:
            return False
        i+=1
    return True

primes = sieve(10**6)

z = 1
c = 0
while True:
    n = (1+z)**2 +  z**2 + (1+z)*z
    if n > 10**6:
        break
    if n in primes:
        c += 1
    z+=1


print c
