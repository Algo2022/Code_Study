import sys

length = int(sys.stdin.readline())
seq = list(map(int, sys.stdin.readline().split()))

dp = [-1000]

for n in seq:
    dp.append(n + max(0, dp[-1]))

print(max(dp))
