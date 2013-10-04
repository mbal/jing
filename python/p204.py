def primes(limit):
    p = [2, 3, 5, 7]
    for i in xrange(3, limit, 2):
        for k in xrange(3, int(limit**.5) + 1):
            if i % k == 0:
                break
        else:
            p.append(i)
    return p

LIMIT = 10**9
factors = primes(100)
prev = [1]
c = 1

while True:
    new = set()
    for item in prev:
        for f in factors:
            if item * f <= LIMIT:
                new.add(item * f)
    c += len(new)
    prev = list(new)[:]
    if not prev:
        break

print c
