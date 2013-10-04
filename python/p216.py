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

def non_residue(prime):
    for p in primes:
        if p > prime:
            break
        if pow(p, (prime-1)/2, prime) == prime-1:
            return p
    return 0

def shanks_tonelli(n, p):
    # returns x such that x^2 = n (mod p)
    # factor out powers of 2 from p - 1
    S = 0
    Q = p - 1
    while not Q & 1:
        Q >>= 1
        S += 1
    # p - 1 = Q * 2^S
    if S == 1:
        sol = pow(n, ((p+1)/4), p)
        return [sol, p-sol]
    # select a z such that (z/p) = -1
    z = non_residue(p)
    c = pow(z, Q, p)
    R = pow(n, ((Q+1)/2), p)
    t = pow(n, Q, p)
    M = S
    while t % p != 1:
        tmp = t
        i = 0
        while tmp % p != 1:
            tmp = pow(tmp, 2, p)
            i += 1
        if i >= M:
            return []
        b = pow(c, 2**(M - i - 1), p)
        R = (R * b) % p
        bb = b*b
        t = (t * bb) % p
        c = bb % p
        M = i
    return [R, p-R]

LIM = int(1.43 * 50 * 10**6 + 1)
MAX = 50*10**6 + 1
primes = sieve(LIM)
# Currently, this version takes about 220 seconds. The problem is: a lot of
# time is wasted in the for, without doing any hard computation, since
# shanks-tonelli takes 15 seconds (+ ~90 for the pow operations), and the
# primes are computed in 25 seconds. I think I'm gonna try in C.
v = [True] * MAX
inv = set()
for p in primes[1:]:
    sols = shanks_tonelli((p+1)/2, p)
    for s in sols:
        k = -1
        t = 2*s*s - 1
        if t == p:
            k = p
        elif t % p == 0:
            k = 0
        if k >= 0:
            while k + s < MAX:
                v[k+s] = False
                k += p

print sum(v) - 2 #2 accounts for 0 and 1

