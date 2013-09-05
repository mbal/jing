
# equivalent to kadane's algorithm. Using a while loop was too slow, 
# so I translated it to a reduce.
def max_subseq(values, current=0, line_max=0):
    def f((a, b), x):
        t = max(a + x, 0)
        return (t, max(b, t))

    return reduce(f, values, (0, 0))[1]

def lines(m):
    for i in m:
        yield i

def columns(m):
    j = 0
    for i in m:
        c = []
        for k in m:
            c.append(k[j])
        yield c
        j += 1

def diag1(m):
    L = len(m)
    for i in xrange(L-1, -1, -1):
        d = []
        for j in xrange(L - i):
            d.append(m[j][i+j])
        yield d
    for i in xrange(0, L):
        d = []
        for j in xrange(L - i):
            d.append(m[i+j][j])
        yield d

def diag2(m):
    L = len(m)
    for i in xrange(0, L):
        d = []
        for j in xrange(0, i+1):
            d.append(m[i-j][j])
        yield d
    for i in xrange(L - 1, -1, -1):
        d = []
        for j in xrange(L - i):
            d.append(m[L- 1-j][i+j])
        yield d


cache = {}
def gen(k):
    if 1 <= k <= 55:
        res = ((100003 - 200003*k + 300007*k**3) % 10**6) - 500000
        cache[k] = res
        return res
    elif 56 <= k <= 4000000:
        cache[k] = ((cache[k-24] + cache[k-55]) % 1000000) - 500000
        return cache[k]

m = []

for i in xrange(2000):
    t = []
    for j in xrange(1, 2001):
        t.append(gen(i*2000+j))
    m.append(t)

print "OK"
tmpm = 0

for l in lines(m):
    tmpm = max(tmpm, max_subseq(l))

for l in columns(m):
    tmpm = max(tmpm, max_subseq(l))

for l in diag1(m):
    tmpm = max(tmpm, max_subseq(l))

for l in diag2(m):
    tmpm = max(tmpm, max_subseq(l))

print tmpm

