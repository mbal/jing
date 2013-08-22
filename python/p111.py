import itertools

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

def isprime(n):
    i = 0
    if n == 1:
        return False
    while primes[i]*primes[i] <= n:
        if n % primes[i] == 0:
            return False
        i+=1
    return True

primes = sieve(10**6)

s = 0
seen = set()
# 0 is different from the other numbers
for i in range(1, 10):
    for j in range(1, 10):
        n = str(i) + '00000000' + str(j)
        if int(n) in seen:
            continue
        seen.add(int(n))
        if isprime(int(n)):
            print int(n)
            s += int(n)
L = 10
for i in range(1, 10):
    ones = 0
    c = L - 1
    while ones == 0:
        for comb in itertools.combinations_with_replacement(range(0, 10), L-c):
            for indices in itertools.product(*[range(0, L+1)]*(L-c)):
                n = list(str(i)*c)
                for k in range(L-c):
                    n.insert(indices[k], comb[k])
                if n[0] == 0:
                    continue
                number = int(''.join(map(str, n)))
                if number in seen:
                    continue
                seen.add(number)
                if isprime(number):
                    s += number
                    ones+=1
        c -= 1
        if c <= 0:
            break
print s
