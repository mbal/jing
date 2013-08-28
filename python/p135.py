counts = [0 for x in xrange(10**6+1)]
for n in xrange(2, 10**6):
    for k in xrange(n/4+1, n):
        v = n*(4*k - n)
        if v > 10**6:
            break
        counts[v] += 1

print len([x for x in counts if x == 10])
