def blumseq():
    prev = 290797
    i = 0
    while i < 20000:
        r = []
        for j in range(4):
            prev = pow(prev, 2, 50515093)
            r.append(prev%500)
        i += 4
        yield r

# In this problem the most difficult thing to get, beside decent performance
# is enough accurancy. Using stdlib's decimal/fractions is a no-no, since
# they worsen the runtime by a factor of 30. (using fractions this algorithm
# runs for about 1400 seconds, without it takes 40 secs).
# To improve performance I inlined all the calls to utilities
# in this function (such as cross), which, alone, accounts for almost 17
# seconds.
# Avoiding tuples is also a big help.
# In order to preserve precision, I avoided division until the last moment
# and, even then, I used a simple algebraical manipulation to avoid
# too much loss of precision.

def cross(a, b, c, d):
    return a*d - c*b

def intersection(p1, p2):
    (x1, y1, x2, y2) = p1
    (x3, y3, x4, y4) = p2

    qmp0 = (x3 - x1)
    qmp1 = (y3 - y1)

    r0 = x2 - x1
    r1 = y2 - y1
    s0 = x4 - x3
    s1 = y4 - y3
    det = r0 * s1 - r1 * s0 #cross(r0, r1, s0, s1)
    if det == 0:
        return False
    t = (qmp0 * s1 - qmp1* s0)
    u = (qmp0 * r1 - qmp1* r0)

    if u > 0 and u < det and t > 0 and t < det:
        return (x1*det + t*r0)/ float(det), (y1*det + t*r1)/ float(det)
    if u < 0 and u > det and t < 0 and t > det:
        return (x1*det + t*r0)/ float(det), (y1*det + t*r1)/ float(det)
    return False

segments = [p for p in blumseq()]

inters = set()
for i, line in enumerate(segments):
    for line2 in segments[i+1:]:
        v = intersection(line, line2)
        if v:
            inters.add(v)

print len(inters)
