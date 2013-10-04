def translate(inp):
    # T(a, b, c, d, e, f) ==> T(b, c, d, e, f, a^b&c)
    return inp[1:] + [(inp[0] ^ inp[1] & inp[2])]

def base(n, b, l):
    res = []
    while n > 0:
        n, r = divmod(n, b)
        res.append(r)
    if len(res) < l:
        res.extend([0] * (l - len(res)))
    res.reverse()
    return res

CACHE = {1:1, 2:3}
def bnc(n):
    if n in CACHE:
        return CACHE[n]
    else:
        res = bnc(n-1) + bnc(n-2)
        CACHE[n] = res
        return res

def cyclic_group(n):
    groups = []
    numbers = [base(x, 2, n) for x in xrange(2**n)]
    while numbers:
        tmp = []
        current = numbers[0]
        while current not in tmp:
            tmp.append(current)
            numbers.remove(current)
            current = translate(current)
        groups.append(tmp)
    return groups

# This problem was quite nice. Writing out the small cases (n = 2 and
# partially n = 3 was really helpful).
import operator
print reduce(operator.__mul__, map(lambda x: bnc(len(x)), cyclic_group(6)))
