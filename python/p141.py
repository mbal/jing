limit = int(1e12)
summ = 0

def issquare(n):
    return n**.5 == int(n**.5)

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)


seen = set()

for a in xrange(1, 10**4):
    for b in xrange(1, a):
        if a**3 * b + b*b > limit:
            break
        if gcd(a, b) != 1:
            continue

        k = 1
        while True:
            v = a**3 * b * k**2 + b**2 * k
            if v > limit:
                break
            if issquare(v) and v not in seen:
                print v
                seen.add(v)
            k += 1

print sum(seen)
