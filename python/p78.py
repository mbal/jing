import time
t = time.time()
pt = [1]
def gen2(n):
    r, i, j, k = 0, 0, 0, 1
    while k <= n:
        r += (pt[n-k] if (i & 3 < 2) else -pt[n-k])
        r = r % (10**6)
        i += 1
        j = (i >> 1) + 1 if i & 1 == 0 else -(i >> 1)-1
        k = j * (3*j-1) >> 1
    r = r % (10**6)
    pt.append(r)
    return r

for i in xrange(1, 10**5):
    n = gen2(i)
    if n == 0:
        print i, n
        break
print time.time()-t
