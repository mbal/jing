
def lengthis4(x):
    if len(x) == 4:
        return True
    return False

tri = filter(lengthis4, map(str, [x*(x+1)/2 for x in range(10000)]))
squ = filter(lengthis4, map(str, [x*x for x in range(10000)]))
pen = filter(lengthis4, map(str, [x * (3 * x - 1)/2 for x in range(10000)]))
hex = filter(lengthis4, map(str, [x * (2 *x -1) for x in range(10000)]))
hep = filter(lengthis4, map(str, [x*(5*x-3)/2 for x in range(10000)]))
oct = filter(lengthis4, map(str, [x * (3*x-2) for x in range(10000)]))

alln = [tri, squ, pen, hex, hep, oct]

import itertools

prev = set([x[-2:] for x in tri])
prev0 = prev 

for permutation in itertools.permutations([squ, pen, hex, hep, oct]):
    prev = prev0
    res = [tri]
    for seq in permutation:
        prev2 = []
        tmp = []
        for number in seq:
            if number[:2] in prev:
                prev2.append(number[-2:])
                tmp.append(number)

        res.append(tmp)
        prev = set(prev2)

    for i in res[0]:
        inter = [i]
        prev = i
        for j in range(1, len(res)+1):
            for js in res[j%len(res)]:
                if prev[-2:] == js[:2]:
                    prev = js
                    inter.append(js)
                    break
        if len(inter) == len(res)+1 and inter[-1] == inter[0]:
            print inter, sum(map(int, inter[:-1]))

