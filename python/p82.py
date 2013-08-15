# suppose we know the shortest path from the next colum to the last one,
# choosing the first step is very simple.

f = open('matrix.txt')
m = []
for line in f:
    m.append([int(x) for x in line.split(',')])

def walk():
    sol = []
    for i in range(len(m)):
        sol.append(m[i][len(m)-1])
    for i in range(len(m)-2, -1, -1):
        sol[0] += m[0][i]
        for j in range(1, len(m)):
            sol[j] = min(sol[j-1] + m[j][i], sol[j]+m[j][i])
        for j in range(len(m)-2, -1, -1):
            sol[j] = min(sol[j], sol[j+1] + m[j][i])
    return sol



print min(walk())
