count = 0
for i in xrange(2, 10000+1):
    if int(i**.5) == i**.5:
        continue
    S = i
    m0 = 0.0
    d0 = 1.0
    a0 = int(S**.5)
    an = a0

    p = []

    stop = []

    while (m0, d0, an) not in stop:
        stop.append((m0, d0, an))
        m0 = d0 * an - m0
        d0 = (S - m0**2) / d0
        an = int((a0 + m0)/d0)
        p.append(an)
    del p[-1]

    if len(p) % 2 != 0:
        count += 1
print count
