import itertools
maxi = 0
best = None

for c in itertools.combinations(('0.0', '1.0', '2.0', '3.0', '4.0', '5.0',
'6.0', '7.0', '8.0', '9.0'), 4):
    prev = []
    for o1 in '+*-/':
        for o2 in '+*-/':
            for o3 in '+*-/':
                for inds in itertools.permutations(range(4)):
                    for i in range(0, 9, 2):
                        for j in range(i+2, 9, 2):
                            d = [c[inds[0]] , o1 , c[inds[1]] , o2 , c[inds[2]] , o3 , c[inds[3]]]
                            d.insert(i, '(')
                            d.insert(j, ')')
                            try:
                                prev.append(eval(''.join(d)))
                            except ZeroDivisionError:
                                pass
    count = 0

    prev = filter(lambda x: x == int(x), sorted(list(set(prev))))
    if 1 in prev:
        i = prev.index(1)
        while i < len(prev)-1 and prev[i] == prev[i+1] - 1:
            count += 1
            i+=1
        if count > maxi:
            maxi = count
            best = c

print best



