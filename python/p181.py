def main(B, W):
    m = [[0 for y in range(W+1)] for x in range(B+1)]

    m[0][0] = 1
    for i in range(B+1):
        for j in range(W+1):
            if i == 0 and j == 0:
                continue
            for a in range(i, B+1):
                for b in range(j, W+1):
                    m[a][b] += m[a-i][b-j]
    return m

print main(40, 60)[40][60]
