import sys
from collections import defaultdict

num_coins, n = map(int, sys.stdin.readline().split())

coins = []
for _ in range(num_coins):
    coins.append(int(sys.stdin.readline()))

cases = defaultdict(int)
coins.sort(reverse=True)

for coin in coins:
    cases[coin] += 1
    for num_curr in range(1, n+1):
        if num_curr > coin:
            cases[num_curr] += cases[num_curr-coin]

print(cases[n])

