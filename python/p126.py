k = 30000

def f(a, b, c, n):
    return 2*(a*c+a*b+b*c) + 4*(a+b+c+n-2)*(n - 1)

counts = [0 for x in range(k+1)]
for a in range(1, k):
    for b in range(a, k):
        for c in range(b, k):
            n = 1
            while True:
                r = f(a,b,c,n)
                if r > k:
                    break
                counts[r] += 1
                n += 1
            if f(a,b,c,1) > k:
                break
        if f(a,b,1,1) > k:
            break
    if f(a,1,1,1) > k:
        break

for k, i in enumerate(counts):
    if i == 1000:
        print i, k
        break


