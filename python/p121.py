import itertools
# there's probably a better way, using Stirling numbers of the First kind
# P(n) = sum(S(n+1, k), for k in ((n+1)/2+1, n+1])
probs = [1.0/(x+1) for x in range(1, 16)]

res = 0

for i in range(8, 16):
    for c in itertools.combinations(range(15), i):
        p = 1
        for index in c:
            p *= probs[index]
        for index in set.difference(set(range(15)), set(c)):
            p*=float(index+1)/(index+2)
        res += p

print int(1/res)
