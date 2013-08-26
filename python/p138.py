xn = 1
yn = 0

s = 0

for i in range(13):
    xnew = -9*xn - 10*yn + 8
    ynew = -8*xn - 9*yn + 8

    s += abs(xnew)

    xn = xnew
    yn = ynew

print s-1
