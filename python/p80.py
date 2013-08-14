def sqroot(ns):
    root = []
    rem = 0
    while ns:
        c = rem * 100 + int(ns[:2])
        p = int(''.join(map(str, root)) or '0')
        x = 1
        while x*(20*p+x) <= c:
            x+=1
        x = x - 1
        y = x*(20*p+x)
        root.append(x)
        rem = c - y
        ns = ns[2:]
    return root

s = 0
for i in range(1, 101):
    if i**.5 == int(i**.5):
        continue
    s += sum(sqroot(str(i).zfill(2) + "0"*200)[:100])
print s

