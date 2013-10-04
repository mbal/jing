from math import e, log

def terminating(n, k):
    nu = k / gcd(n, k)
    while nu % 5 == 0 and nu != 0:
        nu /= 5
    while nu % 2 == 0 and nu != 0:
        nu /= 2
    return nu > 1

def gcd(a, b):
    while b != 0:
        a, b = b, a % b 
    return a

s = 0

for N in xrange(5, 10001):
    maxm = 0
    rep = False
    # In this particular case, k is always round(N/e, 0), however
    # we don't have any proof of this statement, and doing this for
    # loop to check the two possibilities isn't going to kill the
    # performances.
    around = int(N/e)
    for k in xrange(max(around-1, 1), around+2):
        num = k*(log(N) - log(k))
        if num > maxm:
            maxm = num
            rep = terminating(N, k)
    s += N * (1 if rep else -1)

print s
