import sys

confs_num = int(sys.stdin.readline())
confs = []
for _ in range(confs_num):
    t1, t2 = map(int, sys.stdin.readline().split())
    confs.append((t1, t2))

confs.sort(key=lambda x: (x[1], x[0]))

ans = 0
curr = 0
for conf in confs:
    if curr <= conf[0]:
        ans += 1
        curr = conf[1]
print(ans)
