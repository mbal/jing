# Once solved p137, this is quite easy, since it can be solved in the same way
# The only difficult thing is to get the generating function for the series
# In this case, it's 
#
# (x + 3x^2) / (1 - x - x^2)
# (x + 3x^2) / (1 - x - x^2) = n
# x + 3x^2 = n(1 - x - x^2)
# delta = b^2 - 4ac = (n+1)^2 + 4(n+3)n
# delta = m^2 should be a perfect square
# (n+1)^2 +4(n+3)n = m^2
# Solved using the recurrence equation below, from the starting points.
ns = []

for (mn, nn) in ((0, -1), (0, 1), (-3, -2), (-3, 2), (-4, -5), (-4, 5), (2, -7), (2, 7)):
    for i in range(20):
        mnew = -9*mn - 4*nn - 14
        nnew = -20*mn - 9*nn - 28
        
        if mnew > 0:
            ns.append(mnew)

        mn = mnew
        nn = nnew

print sorted(set(ns))
print sum(sorted(set(ns))[:30])
