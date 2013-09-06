def count(sheets):
    res = 0

    if sheets == [0 for x in sheets[:-1]] + [1]:
        return 0

    if sum(sheets) == 1:
        res += 1

    for i, v in enumerate(sheets):
        nsheets = []
        if v >= 1:
            nsheets = sheets[:]
            nsheets[i] = sheets[i] - 1
            for j in range(i+1, len(nsheets)):
                nsheets[j] = nsheets[j] + 1
            res += v * count(nsheets)
    return res/float(sum(sheets))

SHEETS = [1, 1, 1, 1]
print count(SHEETS[:])
