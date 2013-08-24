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

primes = sieve(10**7)
i = 1 
primes.insert(0, 0)
maxx = 10**10
while True:
    sqp = primes[i]*primes[i]
    r = (pow(primes[i] - 1, i, sqp) + pow(primes[i] + 1, i, sqp)) % sqp
    if r >= maxx:
        print i
        break
    i+=1
