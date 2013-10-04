def trib(mod):
    a, b, c = 1, 1, 1
    while True:
        a, b, c = b, c, (a+b+c) % mod
        yield a

def nth_non_divisor(n):
    k = 27
    c = 1

    while c < n - 1:
        k += 2
        prev = []
        for i in trib(k):
            prev.append(i)
            if i == 0:
                break
            if len(prev) > 3:
                del prev[0]
            if prev == [1, 1, 1]:
                c += 1
                break
    return k

print nth_non_divisor(125)
