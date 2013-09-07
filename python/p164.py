CACHE = {}
def f(length, a, b, maxD):
    if ((length, a, b) in CACHE):
        return CACHE[(length, a, b)]
    if (a + b) > 9:
        return 0

    if length == maxD:
        return 1

    count = 0
    for c in range(0, 10 - (a + b)):
        count += f(length + 1, b, c, maxD)
    CACHE[(length, a, b)] = count
    return count

s = 0
for a in range(1, 10):
    for b in range(10 - a - 0):
        s += f(2, a, b, 20)
print s


