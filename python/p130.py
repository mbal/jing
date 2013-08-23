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

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

def A(n):
    if gcd(n, 10) != 1:
        return 0
    rep = 1
    c = 1
    while rep:
        c += 1
        rep = (rep * 10 + 1)%n
    return c


c = 0
s = 0
primes = sieve(10**6)
n = 90
while c < 25:
    n += 1
    while n in primes:
        n += 1
    an = A(n)
    if an != 0:
        if (n-1) % A(n) == 0:
            s += n
            c += 1

print s
