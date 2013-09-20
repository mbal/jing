CACHE = {}
def count(length, n):
    if (length, n) in CACHE:
        return CACHE[(length, n)]
    if n > length:
        return 1
    c = 1
    for i in range(0, length+1):
        for j in range(n, length-i+1):
            res = count(length - i - j - 1, n)
            c+=res
    CACHE[(length, n)] = c
    return c

print count(168, 50)


