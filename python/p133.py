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

primes = sieve(10**5)

s = 0
import time

t = time.time()

for p in primes:
    if p in (2,3,5,7,13,19,23,29,31,37):
        s += p
        continue
    if p > 10**5:
        break
    for n in range(1, 17):
        if pow(10, 10**n, p) == 1:
            break
    else:
        s += p

print s
print time.time()-t
