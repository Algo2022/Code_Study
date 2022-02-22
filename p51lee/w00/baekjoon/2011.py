import sys

code = list(map(int, sys.stdin.readline().strip()))
l = len(code)

dp = [1]*(l+1)

prev = -1
for i in range(1, l+1):
    curr = code[l-i]

    if curr == 0:
        dp[i] = 0
    elif curr > 2:
        dp[i] = dp[i-1]
    else:
        if prev == -1:
            dp[i] = 1
        else:
            if curr == 1:
                dp[i] = dp[i-1]+dp[i-2]
            elif 0 <= prev <= 6:
                dp[i] = dp[i-1]+dp[i-2]
            else:
                dp[i] = dp[i-1]
    prev = curr

print(dp[-1]%1000000)
