import sys

n, m = map(int, sys.stdin.readline().split())

mat = []
heights = []
route = []
for _ in range(n):
    mat.append(list(map(int, sys.stdin.readline().split())))
    route.append([0]*m)

for i in range(n):
    for j in range(m):
        heights.append((i, j, mat[i][j]))

heights.sort(key=lambda x: x[2], reverse=True)

route[0][0] = 1
valid = lambda x: 0 <= x[0] < n and 0 <= x[1] < m
for h in heights:
    i = h[0]
    j = h[1]
    neighbors = list(filter(valid, [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]))
    print(neighbors)
    for ne in neighbors:
        if mat[i][j] < mat[ne[0]][ne[1]]:
            route[i][j] += route[ne[0]][ne[1]]
print(route[-1][-1])

