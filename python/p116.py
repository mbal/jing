CACHE = {}
def fill(length, block):
    if (length, block) in CACHE:
        return CACHE[(length, block)]
    if block > length:
        return 0 
    bl = 0
    for i in range(length-block+1):
        bl += 1+fill(length - block - i, block)
    CACHE[(length, block)] = bl
    return bl

print fill(50, 2) + fill(50, 3) + fill(50, 4)
