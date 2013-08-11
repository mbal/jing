i = 300

cubes = {}

while True:
    n = list(str(i**3))
    s = ''.join(sorted(n))
    l = cubes.get(s, [])
    l.append(i)
    cubes[s] = l
    if len(cubes[s]) == 5:
        print cubes[s]
        print int(cubes[s][0]) **3
        break
    i += 1

