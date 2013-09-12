def sieve(n):
    m = (n-1) // 2
    b = [True]*m
    i,p,ps = 0,3,[2]
    while p*p < n:
        if b[i]:
            ps.append(p)
            j = 2*i*i + 6*i + 3
            while j < m:
                b[j] = False
                j = j + 2*i + 3
        i+=1; p+=2
    while i < m:
        if b[i]:
            ps.append(p)
        i+=1; p+=2
    return ps

primes = sieve(10**5)

def factor(n):
    f = set()
    for i in xrange(1, int(n**.5) + 1):
        if n % i == 0:
            f.add(i)
            f.add(n/i)
    return f

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

def gen_factors(n):
    f = set([1])
    for a in xrange(0, 2*n+1):
        for b in xrange(0, 2*n+1):
            f.add(2**a * 5**b)
    return f

# the primitive solutions are the solution for 1/a + 1/b = 1/10**n
# To solve this:
# 1/a + 1/b = 1/10**n ==> 1/b = 1/10**n - 1/a ==>
# 1/b = (a - 10**n) / (10**n * a)
# Moreover, a is in the form 10**n + x, where x = 2**i * 5**j
def get_primitives(n):
    res = []
    for a in gen_factors(n):
        ac = (10**n + a)
        b = (10**n)*ac / a
        if b >= ac:
            res.append((ac, b))
    return res

def count_solutions(n):
    return sum(map(len, map(factor, map(lambda a:gcd(*a), get_primitives(n)))))

print sum(count_solutions(x) for x in range(1, 10))
