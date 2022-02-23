from sys import stdin

n, m = map(int, stdin.readline().split())

adj = [[] for _ in range(n)]
for _ in range(m):
  f, t, w = map(int, stdin.readline().split())
  adj[f-1].append((t-1, w))
  adj[t-1].append((f-1, w))

fr, to = map(int, stdin.readline().split())
fr -= 1
to -= 1

def validate(limit):
    visit = set()
    stack = [fr]
    while stack:
        curr = stack.pop()
        if curr == to:
            return True
        visit.add(curr)
        for nei, wei in adj[curr]:
            if wei >= limit and nei not in visit:
                stack.append(nei)
    return False

left = 1
right = 1000000001

while left + 1 < right:
    mid = (left + right) // 2
    if validate(mid):
        left = mid
    else:
        right = mid

print(left)
