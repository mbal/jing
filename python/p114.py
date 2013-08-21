CACHE = [0 for x in range(51)]
def count(length):
    if CACHE[length] != 0:
        return CACHE[length]
    if 3 > length:
        return 1
    c = 1
    for i in range(3, length+1):
        for j in range(0, length-i+1):
            res = count(length - i - j - 1)
            c+=res
    CACHE[length] = c
    return c

print count(5)
