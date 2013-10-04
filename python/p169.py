CACHE = {}
def f(n):
    if n in CACHE:
        return CACHE[n]
    if n == 0 or n == 1:
        return 1
    if n % 2 != 0:
        res = f(n/2)
        CACHE[n] = res
        return res
    else:
        res = f(n/2) + f(n/2 - 1)
        CACHE[n] = res
        return res

print f(10**25)
