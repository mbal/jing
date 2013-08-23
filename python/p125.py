pssum = []
for i in range(10**4):
    pssum.append(i**2)

for i in range(1, 10**4):
    pssum[i] = pssum[i-1] + pssum[i]

def palin(n):
    s = str(n)
    return s == s[::-1]

seen = set()

s = 0
for i in range(len(pssum)-2):
    for j in range(i+2, len(pssum)):
        ss = pssum[j] - pssum[i]
        if ss > 10**8:
            break
        if ss in seen:
            continue
        if palin(ss):
            seen.add(ss)
            s += ss

print s
