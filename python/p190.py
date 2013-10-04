# Using lagrange's multipliers, we get that the first term in the sequence
# is 2/(n+1), the second is 4/(n+1) and so on.
def xs(n):
    res = []
    for i in range(1, n+1):
        res.append(i*2.0/(n+1))
    return res

def maximum(vals):
    return int(reduce(lambda a, b: a*b, map(lambda (a, b): b**(a+1),
        enumerate(vals))))

s = 0
for i in range(2, 16):
    s += maximum(xs(i))

print s


