from sys import stdin

n, s = map(int, stdin.readline().split())
l = list(map(int, stdin.readline().split()))

ans = 0
for i in range(1, 2**n):
    status = list(bin(i)[2:].zfill(n))
    if sum([i*int(c) for i, c in zip(l, status)]) == s: ans += 1
print(ans)

