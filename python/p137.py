# This took a while to solve.
ns = []

for (mn, nn) in ((-1, 0), (1, 0), (-2, -1), (2, -1)):
    for i in range(12):
        mnew = -9*mn + -20*nn - 4
        nnew = -4*mn - 9*nn - 2
        
        if nnew > 0:
            ns.append(nnew)

        mn = mnew
        nn = nnew

print sorted(set(ns))[15]
