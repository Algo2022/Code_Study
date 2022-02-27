import sys

ans = []
for _ in range(int(sys.stdin.readline())):
    ans.append(int(sys.stdin.readline()))

ans.sort()
print(*ans, sep="\n")
