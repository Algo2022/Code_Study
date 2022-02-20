import sys

n = int(sys.stdin.readline())

dp = [0]*max(n,2)
dp[0] = 1
dp[1] = 3
for i in range(2, n):
    dp[i] = dp[i-1] + 2*dp[i-2]
print(dp[n-1] % 10007)

