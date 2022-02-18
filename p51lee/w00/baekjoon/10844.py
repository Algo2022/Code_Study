import sys

n = int(sys.stdin.readline())

dp = [[0]*10 for _ in range(n)]

dp[0] = [0,1,1,1,1,1,1,1,1,1]

for i in range(1, n):
    prev = dp[i-1]
    dp[i][0] = prev[1]
    dp[i][9] = prev[8]
    for j in range(1,9):
        dp[i][j] = prev[j-1]+prev[j+1]

print(sum(dp[n-1])%1000000000)
