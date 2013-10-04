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


def modcnr(n, r, m):
    p = 1
    d = 1
    for i in range(r):
        p = (p * (n - i)) % m
        d = (d * r) % m
    return p / d

def base(n, b, pad=0):
    res = []
    while n > 0:
        n, r = divmod(n, b)
        res.append(r)
    if len(res) < pad:
        res.extend([0] * (pad - len(res)))
    return res

def count_carries(add1, add2, base):
    carry_count = 0
    carry = 0
    res = []
    for i, v in enumerate(add1):
        val = (v + carry + add2[i])
        if carry:
            carry -= 1
        if val >= base:
            carry_count += 1
            carry += val / base
        res.append(val % base)
    return carry_count + (carry >= base)

def E(n, k, p):
    r = 0
    e = 0
    if k > n/2:
        k = n - k
    if p > n-k:
        return 1
    if p > n/2:
        return 0
    f = n**.5
    if p > f:
        if n % p < k % p:
            return 1
        return 0
    while n:
        a = n % p
        n /= p
        b = k%p + r
        k /=p
        if a < b:
            e += 1
            r = 1
        else:
            r = 0
    return e
# I'm using Kummer's Theorem
primes = sieve(2*10**7)
s = 0
m = 20000000
n = 15000000
ds = 20
for p in primes:
    if p > m:
        break
    #ds = int(log(max(m - n, n), p)) + 1
    #l1 = base(m - n, p, ds)
    #l2 = base(n, p, ds)
    #c = count_carries(l1, l2, p)
    # Using E(m, n, p) from http://www.numbertheory.org/php/binomial.html
    # (basically a smart version of the four lines above).
    c = E(m, n, p)
    if c > 0:
        s += p*c
print s
