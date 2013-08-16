def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

limit = 50
solutions = limit*limit*3
for x in range(1, limit+1):
    for y in range(1, limit+1):
        a, b = -y/gcd(y, x), x/gcd(y, x)
        i = x+a
        j = y+b
        # this can be transformed in a closed form,
        while i >= 0 and j >= 0 and i <= limit and j <= limit:
            solutions += 1
            i += a
            j += b
        i = x-a
        j = y-b
        while i >= 0 and j >= 0 and i <= limit and j <= limit:
            solutions += 1
            i -= a
            j -= b
print solutions
