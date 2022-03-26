import sys
from collections import defaultdict

n = int(sys.stdin.readline())
dp = defaultdict(lambda:1000000)

dp[1] = 0
for i in range(1, n):
    dp[i*3] = min(dp[i*3], dp[i]+1)
    dp[i*2] = min(dp[i*2], dp[i]+1)
    dp[i+1] = min(dp[i+1], dp[i]+1)
print(dp[n])
