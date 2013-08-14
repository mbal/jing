def approx(i):
    S = i
    m0 = 0.0
    d0 = 1.0
    a0 = int(S**.5)
    an = a0

    p = [a0]

    stop = []

    while (m0, d0, an) not in stop:
        stop.append((m0, d0, an))
        m0 = d0 * an - m0
        d0 = (S - m0**2) / d0
        an = int((a0 + m0)/d0)
        p.append(an)
    del p[-1]

    return p

def solve(D):
    b = approx(D)
    An = [1, b[0]]
    Bn = [0, 1]
    del b[0]
    j = 0
    ev = An[-1]*An[-1] - D*Bn[-1]*Bn[-1]
    while ev != 1:
        tmp = An[-1]
        An[-1] = b[j]*An[-1] + An[-2]
        An[-2] = tmp

        tmp = Bn[-1]
        Bn[-1] = b[j] * Bn[-1] + Bn[-2]
        Bn[-2] = tmp
        ev = An[-1]*An[-1] - D*Bn[-1]*Bn[-1]
        j += 1
        j %= len(b)
    return An[-1], Bn[-1]

maxx = 0
maxin = 0
for i in range(2, 1001):
    if int(i**.5) == i**.5:
        continue
    x = solve(i)[0]
    if x > maxx:
        maxx = x
        maxin = i

print maxx
print maxin
