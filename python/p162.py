CACHE = {}
def create(length, zero, one, a):
    if (length, zero, one, a) in CACHE:
        return CACHE[(length, zero, one, a)]
    if length == 0:
        if zero == 0 or one == 0 or a == 0:
            return 0
        else:
            return 1
    res = 0
    for i in range(0, 16):
        if i == 0:
            res += create(length - 1, zero + 1, one, a)
        elif i == 1:
            res += create(length - 1, zero, one + 1, a)
        elif i == 10:
            res += create(length - 1, zero, one, a + 1)
        else:
            res += create(length - 1, zero, one, a)
    CACHE[(length, zero, one, a)] = res
    return res
            
c = 0
for length in range(3, 17):
    for i in range(1, 16):
        one = 0
        a = 0
        if i == 1:
            one = 1
        if i == 10:
            a = 1
        c += create(length - 1, 0, one, a)
print c
print hex(c).upper()[2:]
