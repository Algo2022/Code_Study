from collections import deque
from sys import stdin

ans_list = []
while True:
    n, m = map(int, stdin.readline().split())
    if n or m:
        adj = [[0] * n for _ in range(n)]
        for _ in range(m):
            i, j = map(int, stdin.readline().split())
            adj[i - 1][j - 1] = 1
            adj[j - 1][i - 1] = 1
        visited = [-1] * n
        ans = 0
        for root in range(n):
            if visited[root] != -1:
                continue
            else:
                is_tree = True
                queue = deque([root])
                visited[root] = root
                while queue:
                    curr = queue.pop()
                    for next in range(n):
                        if adj[curr][next]:
                            if visited[next] != -1 and visited[curr] != next:
                                is_tree = False
                                # print(visited)
                                # print(curr, next)
                            elif visited[next] == -1:
                                visited[next] = curr
                                queue.appendleft(next)
                if is_tree:
                    ans += 1
        ans_list.append(ans)
    else:
        break

for c, ans in enumerate(ans_list, start=1):
    if ans == 0:
        print("Case {}: No trees.".format(c))
    elif ans == 1:
        print("Case {}: There is one tree.".format(c))
    else:
        print("Case {}: A forest of {} trees.".format(c, ans))
