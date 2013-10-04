from math import log

k = 2
p = 1
np = 1
lim = (1.0/12345)

while float(p)/np > lim:
    x = (1+2*k+1) / 2.0
    if log(x, 2) == int(log(x, 2)):
        p += 1
    np += 1
    k += 1
    
print ((2*k+1)**2 - 1) / 4
