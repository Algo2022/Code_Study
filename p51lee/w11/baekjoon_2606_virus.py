from sys import stdin

n = int(stdin.readline())
mat = [[0]*n for _ in range(n)]
for _ in range(int(stdin.readline())):
    a, b = map(int, stdin.readline().split())
    mat[a-1][b-1] = 1
    mat[b-1][a-1] = 1

visit = set()
stack = [0]
ans = 0
while stack:
    curr = stack.pop()
    if curr not in visit:
        ans += 1
    visit.add(curr)
    for nei, con in enumerate(mat[curr]):
        if con and nei not in visit:
            stack.append(nei)

print(ans-1)
