import math

def c(n, k):
    return math.factorial(n) / (math.factorial(k) * math.factorial(n-k))

def f(d, l):
    if d == 0:
        return 0
    elif l < 4:
        return d**l
    else:
        return f(d-1, l) + l*f(d-1, l-1) + c(l, 2) * f(d-1, l-2) + c(l, 3) * f(d-1, l-3)

print f(10, 18) * 9 / 10
