cycles = [-1] * 10**8

facts = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

def fact(n):
    s = 0
    while n > 0:
        s += facts[n % 10]
        n /= 10
    return s


def get_length(n):
    ad = []
    c = n
    l = 0
    while c not in ad:
        ad.append(c)
        #ns = map(int, list(str(c)))
        #c = fact(ns) #sum(map(factorial, ns))
        c = fact(c)
        if c < 10**8:
            if cycles[c] != -1:
                l += cycles[c] + 1
                return l
        l += 1
    cycles[n] = l
    return l



c = 0
for i in xrange(1000000):
    cyclen = get_length(i)
    if cyclen == 60:
        c += 1

print c
