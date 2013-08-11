from fractions import Fraction

def e(prev, i, k, limit=10):
    if i == limit:
        return Fraction(1)
    if prev[1:] == [1,1]:
        return Fraction(2*k) + Fraction(1.0) / Fraction(e([1, 1, 2*k], i+1, k+1, limit))
    else:
        return Fraction(1) + Fraction(1.0) / Fraction(e([prev[-2], prev[-1], 1], i+1, k, limit))

a = (Fraction(2) + Fraction(1.0) / Fraction(e([1,1], 0, 1, 98)))
print a.numerator
print dir(a)

print float(a)

print sum(map(int ,list(str(a.numerator))))

