cache = [-1 for x in range(51)]

def fill(length):
    if length < 0:
        return 0
    if cache[length] != -1:
        return cache[length]
    c = 1
    for i in range(0, length+1):
        for j in range(2, 5):
            c += fill(length - j - i)
    cache[length] = c
    return c

print fill(50)
    
