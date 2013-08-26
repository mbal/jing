limit = int(100*10**6)
end = False

res = 0

from fractions import gcd

for m in xrange(2, int(limit**.5) + 1):
    for n in xrange(1, m):
        if (n + m) % 2 != 0 and gcd(m, n) == 1:
            a = 2*m*n
            b = m*m - n*n
            c = m*m + n*n
            p = a+b+c
            if p > limit:
                break
            if c % (b - a) == 0:
                res += limit / p

print res

#Same solution, much faster.
res = 0
p = 0
xn = 1
yn = 1
while p < limit:
    xnew = 3*xn + 4*yn
    ynew = 2*xn + 3*yn
    
    p = xnew + ynew
    if p > limit:
        break

    res += limit / p

    xn = xnew
    yn = ynew
    

print res
