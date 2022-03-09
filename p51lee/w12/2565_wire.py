from sys import stdin

wire_list = []
n = int(stdin.readline())
for _ in range(n):
    f, t = map(int, stdin.readline().split())
    wire_list.append((f, t))

wire_list.sort()
dp = [1] * n

for i, (f1, t1) in enumerate(wire_list):
    for j, (f2, t2) in enumerate(wire_list[i+1:], start=i+1):
        if t1 < t2: dp[j] = max(dp[j], dp[i] + 1)

print(n-max(dp))
