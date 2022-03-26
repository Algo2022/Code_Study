from sys import stdin
from collections import deque

n, m, v = map(int, stdin.readline().split())
v -= 1

adj = [[0]*n for _ in range(n)]
for _ in range(m):
    i, j = map(int, stdin.readline().split())
    adj[i-1][j-1] = 1
    adj[j-1][i-1] = 1

log_dfs = []
log_bfs = []

stack = [v]
visit = set()
while stack:
    curr = stack.pop()
    if curr in visit:
        continue
    visit.add(curr)
    log_dfs.append(curr+1)
    for i, e in reversed(list(enumerate(adj[curr]))):
        if e and i not in visit:
            stack.append(i)

queue = deque([v])
visit = set()
while queue:
    curr = queue.popleft()
    if curr in visit:
        continue
    visit.add(curr)
    log_bfs.append(curr+1)
    for i, e in enumerate(adj[curr]):
        if e and i not in visit:
            queue.append(i)

print(*log_dfs, sep=" ")
print(*log_bfs, sep=" ")

