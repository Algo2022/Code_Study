import sys

n, k = map(int, sys.stdin.readline().split())

dp = [ [0] * (n+1) for _ in range(k) ]

for i in range(k):
    dp[i][0] = 1
for i in range(n+1):
    dp[0][i] = 1

for i in range(1, k):
    for j in range(1, n+1):
        dp[i][j] = sum(dp[i-1][:j+1])
# print(*dp, sep="\n")
print(dp[k-1][n]%1000000000)
