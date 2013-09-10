import time
LIM = 10**6
s = 0
s2 = 0
def gcd(a, b):
    while b != 0:
        a, b = b, a%b
    return a

t = time.time()
MAX = int(LIM**.5) + 1
# this is too slow to run. The same code (in C) runs in about 16 seconds
# (without optimization) and 11 with -O2
c = sum(i*(LIM/i) for i in xrange(1, LIM+1))
a = 1
while a < MAX:
    m1 = a * a
    for b in xrange(1, a+1):
        if gcd(a, b) != 1:
            continue
        j = 1
        m = m1 + b*b
        if m > LIM:
            break
        val = a<<1 if a == b else (a+b)*2
        while j * m <= LIM:
            c += val*j * (LIM / (j * m))
            j += 1
    a += 1

print c
print time.time() - t

t = time.time()
# This solution could be faster, but it's still too slow. (in some test with
# the other solution, it's about 2x faster), unfortunately, f(L) takes more
# than 20 seconds when L = 10**8, so this can't really be optmized.
def f(n):
    s = 0
    for i in xrange(1, n+1):
        s += (n/i) * i
    return s

s = f(LIM) + 2 * f(LIM / 2)
a = 1
while a*a <= LIM:
    b = a + 1
    blim = LIM - a*a
    while b*b <= blim:
        if gcd(a, b) == 1:
            s += 2*(a+b) * f(LIM/(a*a+b*b))
        b += 1
    a += 1
print s
print time.time() - t
