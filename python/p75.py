import time

t = time.time()
triples = []
def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a%b)

for a in range(1, 1000):
    for b in range(a+1, 1000):
        if a%2 == b%2:
            continue
        if gcd(a,b) == 1:
            triples.append((b**2-a**2, 2*a*b, a**2+b**2))

print triples[2]
print sum(triples[2])
l = [0]*int(400) #1.5*10**6)
for t in triples:
    s = sum(t)
    if s < 400: #1.5*10**6:
        l[s] += 1

cop = l[:]

for i in xrange(1, len(l)):
    if l[i] >= 1:
        s = 2*i
        if l[i] != 0:
            while s < 400: #1.5*10**6:
                cop[s] += l[i]
                s += i
print filter(lambda a: a[1] == 1, enumerate(cop))
print len(filter(lambda x : x == 1, cop))



