CACHE = {}

def factor(n, k=2):
    if n in CACHE:
        return CACHE[n]
    result = []
    while k*k <= n:
        if n % k == 0:
            tmp = factor(n/k, k)
            for l in tmp:
                result.append([k] + l)
        k += 1
    result.append([n])
    CACHE[n] = result
    return result

def magic(number, k):
    f = factor(number)
    for fs in f:
        l = len(fs)
        if l > k or l == 1:
            continue
        if number - sum(fs) == k - l:
            return True
    return False

s = []
for k in xrange(2, 12000):
    mini = 2*k+1
    for N in xrange(k, 2*k+1):
        if magic(N, k):
            mini = N
            break
    s.append(mini)


print sum(set(s))
