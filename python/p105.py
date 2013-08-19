import itertools

def check_validity(nopt):
    l = len(nopt)
    nopt = set(nopt)
    for i in range(1, l):
        for B in itertools.combinations(nopt, i):
            s = sum(B)
            other = set.difference(nopt, B)
            for j in range(1, len(other)+1):
                for C in itertools.combinations(other, j):
                    if sum(C) == s:
                        return False
                    if i > j:
                        if not s > sum(C):
                            return False
    return True

f = open('sets.txt')

su = 0

for line in f:
    s = map(int, line.strip().split(','))
    if check_validity(s):
        su += sum(s)

print su
