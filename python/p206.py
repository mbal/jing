i = 10**9 + 30
c = 0
v = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
while i < (2**.5) * 10**9:
    s = str(i * i)
    if len(s) != 19:
        continue
    for k in range(0, len(s), 2):
        if s[k] != v[k/2]:
            break
    else:
        print i
        break
    i += 40 if c % 2 == 0 else 60
    c += 1
    c %= 2
