import sys

n = int(sys.stdin.readline())
cases = []
for _ in range(n):
    cases.append(int(sys.stdin.readline()))

t = max(cases)
dp = [0]*t
dp[0] = 1
dp[1] = 2
dp[2] = 4
for i in range(3, t):
    dp[i] = dp[i-3]+dp[i-2]+dp[i-1]

for i in cases:
    print(dp[i-1])
