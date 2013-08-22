G = [[131,673,234,103,18],
[201,96,342,965,150],
[630,803,746,422,111],
[537,699,497,121,956],
[805,732,524,37,331]]

f = open('matrix.txt')
G = []
for line in f:
    G.append(map(int, line.strip().split(',')))

def neighbors(i, j):
    maxj, maxi = 1, 1
    mini, minj = 0, 0
    if i >= 1:
        mini = -1
    if j >= 1:
        minj = -1
    if i < len(G)-1:
        maxi = 2
    if j < len(G[0])-1:
        maxj = 2
    n = []
    for k in range(mini, maxi):
        for z in range(minj, maxj):
            if abs(k) != abs(z):
                n.append((i+k, j+z))
    return n

def smaller(lst, distances):
    dist = 10**10
    pos = 0, 0
    for x in lst:
        if distances[x] < dist:
            dist = distances[x]
            pos = x
    return pos

	
def dijkstra():
    m = G
    current = (0, 0)
    todo = [current]

    dist = {}
    for i in range(len(m)):
        for j in range(len(m[i])):
            dist[(i,j)] = 10**10
            todo.append((i, j))

    dist[(0,0)] = m[0][0]

    while todo:
        current = smaller(todo, dist)
        todo.remove(current)

        alt = dist[current]
        if alt == 10**10:
            break

        for neigh in neighbors(*current):
            alt = dist[current] + m[neigh[0]][neigh[1]]
            if alt < dist[neigh]:
                dist[neigh] = alt

    return dist

print dijkstra()[79,79]
