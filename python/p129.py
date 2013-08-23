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


start = 10**6
n = start
while A(n) < 10**6:
    n += 1

print n
