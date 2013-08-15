f = open('matrix.txt')

m = []
for line in f:
    m.append([int(x) for x in line.split(',')])

cache = {}

def recur(i, j):
    if (i,j) in cache:
        return cache[(i,j)]
    if i == len(m)-1 and j == len(m[0])-1:
        return m[i][j]
    elif j == len(m[0])-1:
        down = recur(i+1, j)
        cache[(i+1, j)] = down
        return m[i][j] + down
    elif i == len(m)-1:
        right = recur(i, j+1)
        cache[(i, j+1)] = right
        return m[i][j] + right
    else:
        down = recur(i+1, j)
        right = recur(i, j+1)
        cache[(i+1, j)] = down
        cache[(i, j+1)] = right
        return m[i][j] + min(down, right)

print recur(0,0)

