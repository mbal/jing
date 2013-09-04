xa, ya = (0.0, 10.1)
xo, yo = (1.4, -9.6)

count = 0

while True:
    m = (yo - ya) / (xo - xa)
    mp = -4*xo / yo

    tanA = abs((m - mp) / (1 + m*mp))

    mnew = (mp - tanA) / (1 + tanA * mp)

    qnew = yo - mnew * xo

    a = mnew**2 + 4
    b = 2 * mnew * qnew
    c = qnew * qnew - 100

    delta = b*b - 4*a*c

    x1 = (-b + delta**.5)/(2*a)
    x2 = (-b - delta**.5)/(2*a)

    xa, ya = xo, yo

    xo = x1 if abs(x1 - xo) > abs(x2 - xo) else x2
    yo = mnew * xo + qnew

    print xo, yo

    if -0.01 <= xo <= 0.01 and yo > 0:
        break

    count += 1

print count
