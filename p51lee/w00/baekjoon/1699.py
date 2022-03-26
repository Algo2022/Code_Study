import sys

n = int(sys.stdin.readline())

dp = [i+1 for i in range(n)]

for i in range(n):
    t = 1
    curr = dp[i]
    while i+1 > t**2:
        if curr > dp[i-t**2]+1:
            curr = dp[i-t**2]+1
            dp[i] = curr
        t += 1
    if i+1 == t**2:
        dp[i] = 1
print(dp[-1])
