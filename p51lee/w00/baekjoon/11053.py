import sys

length = int(sys.stdin.readline())
sequence = list(map(int, sys.stdin.readline().split()))

dp = []
ans = 0
for n in sequence:
    l = 1
    a = 0
    for m, k in dp:
        if m < n:
            a = max(a, k)
    dp.append((n, l+a))
    ans = max(ans, l+a)
print(ans)
