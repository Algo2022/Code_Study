from sys import stdin
from math import inf
import heapq
from collections import defaultdict

v, e = map(int, stdin.readline().split())
k = int(stdin.readline()) - 1

adj = [defaultdict(lambda: inf) for _ in range(v)]
for _ in range(e):
    u1, u2, w = map(int, stdin.readline().split())
    adj[u1-1][u2-1] = min(adj[u1-1][u2-1], w)

shortest = [inf] * v
shortest[k] = 0

queue = [(0, k)]
heapq.heapify(queue)

while queue:
    d, c = heapq.heappop(queue)
    for n, w in adj[c].items():
        new_d = shortest[c] + w
        if new_d < shortest[n]:
            shortest[n] = new_d
            heapq.heappush(queue, (new_d, n))

for s in shortest:
    if s == inf: print("INF")
    else: print(s)
