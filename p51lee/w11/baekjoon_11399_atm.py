from sys import stdin

n = int(stdin.readline())
times = list(map(int, stdin.readline().split()))
times.sort(reverse=True)

ans = 0
for i, t in enumerate(times):
    ans += (i+1)*t

print(ans)
