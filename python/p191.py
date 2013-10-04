# Easy, once you get the trick.
# In this case, we ignore the L result, at first, and we generate strings 
# with A and O. Listing the first few cases we can guess a formula that links
# the f(n) with f(n-1), and we use it to compute the answer. Then, We add
# the single L in every possible position.
CACHE = [0 for x in range(100)]
def f(n):
    if n < 4:
        return [1, 2, 4, 7][n]
    if CACHE[n] != 0:
        return CACHE[n]
    else:
        res = f(n-1) * 2 - f(n-4)
        CACHE[n] = res
        return res

# Listing out the possible cases is helpful.
# For example, with n = 4:
# XXXX f(n)
# LXXX f(n-1)
# XXXL f(n-1)
# XXLX f(n-1)
# XLXX f(n-2)*f(n-3)

def G(n):
    tmp = f(n) + 2 * sum(f(i) * f(n - i - 1) for i in range(0, n/2))
    if n % 2 == 0:
        return tmp
    else:
        return tmp + f(n/2)**2

print G(30)

