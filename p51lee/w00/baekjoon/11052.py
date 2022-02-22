import sys

n = int(sys.stdin.readline())
price_list = list(map(int, sys.stdin.readline().split()))
price_n = len(price_list)

dp = [0]*n
for i, p in enumerate(price_list):
    dp[i] = p

for i in range(n):
    for j in range(price_n):
        if i+j+1 < n:
            dp[i+j+1] = max(dp[i+j+1], dp[i] + price_list[j])
        else:
            break

print(dp[-1])
