from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())

maze = []
for _ in range(n):
    maze.append(list(map(int, stdin.readline().strip())))

queue = deque([(0, 0)])
visit = set()

while queue:
    i, j = queue.popleft()
    if (i, j) in visit:
        continue
    visit.add((i, j))
    if i > 0 and maze[i-1][j] > 0:
        if (i-1, j) not in visit:
            maze[i-1][j] = maze[i][j]+1
            queue.append((i-1, j))
    if j > 0 and maze[i][j-1] > 0:
        if (i, j-1) not in visit:
            maze[i][j-1] = maze[i][j]+1
            queue.append((i, j-1))
    if i < n-1 and maze[i+1][j] > 0:
        if (i+1, j) not in visit:
            maze[i+1][j] = maze[i][j]+1
            queue.append((i+1, j))
    if j < m-1 and maze[i][j+1] > 0:
        if (i, j+1) not in visit:
            maze[i][j+1] = maze[i][j]+1
            queue.append((i, j+1))

print(maze[-1][-1])
