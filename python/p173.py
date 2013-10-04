# I tried other 2 approaches, other than this, both unsuccessful. 
# The first one was based on factorization of n into integers, and
# sieving the invalid. The whole thing was/is quite elegant, but it's too
# slow, and scales really badly. (i.e. 10**5 takes 20 secs, while 10**4 takes
# only 0.15 sec). The other approach was significantly dumber, and it
# consisted of generating the numbers using two nested for cycles. 
# This scaled even worse. The first solution is available in J.
# This solution, however, has one more pro, since it solves even problem 174.
MAX = 10**6
cont = [0 for x in range(MAX + 2)]
limit = MAX/4

for i in xrange(1, limit+2):
    n = 4*i + 4
    o = n
    while n <= MAX:
        cont[n] += 1
        o += 8
        n += o

print "173:", sum(cont)
print "174:", sum(cont.count(x) for x in range(1, 11))

# another (smarter) solution. Doesn't work for 174.
def f(N):
    s = 0
    for t in xrange(1, int((1+(1+N)**.5) / 2) + 1):
        s += N / (4 * t) - t
    return s

print f(10**6)
