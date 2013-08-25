def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

def radicals(limit):
    ra = [Radical(x, 1) for x in xrange(limit)]
    for i in xrange(2, limit):
        if ra[i].value == 1:
            ra[i].value = i
            for j in xrange(2*i, limit, i):
                ra[j].value *= i
    return ra

class Radical:
    def __init__(self, number, value):
        self.number = number
        self.value = value
    def __cmp__(self, other):
        v = cmp(self.value, other.value)
        if v == 0:
            return cmp(self.number, other.number)
        return v
    def __repr__(self):
        return "R(%i, %i)" %(self.number, self.value)

summ = 0
rad = radicals(120001)
srad = sorted(rad[:])
limit = 120000

for c in range(3, limit+1):
    radc = rad[c].value
    clim = c / 2
    for a in srad:
        if a.value * radc > clim:
            break
        if a.number >= clim:
            continue
        b = c - a.number
        if a.value*rad[b].value*radc < c:
            if gcd(a.number, b) == 1:
                summ += c
print summ
#
#
#for a in range(60000):
#    for c, r in enumerate(rad):
#        b = c - a
#        rd = rad[a] * rad[b] * r
#        if rd < c:
#            if gcd(a, b) == 1:
#                summ += c
#
#print summ
#
#
#
#
#print "ok"
#for a in xrange(60000):
#    for b in xrange(a+1, 120000-a+1):
#        if a + b > 120000:
#            break
#        rd = rad[a]* rad[b]* rad[a+b]
#        if rd < (a+b):
#            if gcd(a,b) == 1: # and gcd(a, a+b) == 1 and gcd(b, a+b) == 1:
#                summ += a+b
#
#print summ
