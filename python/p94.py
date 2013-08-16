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
        d0 = (S - m0**2) / float(d0)
        an = int((a0 + m0)/float(d0))
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

sol = 0
# this is the principal solution
x, y = solve(3)
x1, y1 = x, y
print x1, y1
# the next solutions are given through the recurrence:
# x(k+1) = x1 * x(k) + n*y1*y(k)
# y(k+1) = x1 * y(k) + y1*x(k)

while True:
    am = (2*x - 1)
    Am3 = y*(x-2)
    if am > 10**9:
        break
    if am > 0 and Am3 > 0 and am % 3 == 0 and Am3 % 3 == 0:
        a = am/3
        sol += 3 * a -1

    am = (2*x + 1)
    Am3 = y*(x+2)
    if am > 0 and Am3 > 0 and am % 3 == 0 and Am3 % 3 == 0:
        a = am/3
        sol += 3 * a +1

    nx = 2 * x + 3 * y
    ny = 2 * y + x 

    x = nx
    y = ny

print sol
