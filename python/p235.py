def s(r):
    def u(k):
        return (300 - k)*r**(k-1)
    return sum(u(k) for k in xrange(1, 5001))


def solve(f, error, s, e):
    midpoint = (s+e)/2.0
    while midpoint - s > error:
        v = f(midpoint)
        if v > -2e11:
            s = midpoint
        if v < -2e11:
            e = midpoint
        midpoint = (s+e)/2.0
    return midpoint


print "%.15f" %solve(s, 1e-17, 1, 1.2)
