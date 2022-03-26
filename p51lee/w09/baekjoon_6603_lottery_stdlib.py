import sys
from itertools import combinations


cases = []
while True:
    curr = list(map(int, sys.stdin.readline().split()))
    if curr[0] == 0:
        break
    else:
        cases.append(curr)

for case in cases:
    sol = list(combinations(case[1:], 6))
    solsol = list(map(lambda x: " ".join(map(str, x)), sol))
    for temp in solsol:
        print(temp)
    print()

