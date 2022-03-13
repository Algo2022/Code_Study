from math import inf
from sys import stdin

n = int(stdin.readline())
sol_list = list(map(int, stdin.readline().split()))
sol_list.sort()
neu = inf
l, r = 0, n - 1
ans = l, r

while l < r:
    sol_l, sol_r = sol_list[l], sol_list[r]
    sol = sol_l + sol_r
    if abs(sol) < neu:
        neu = abs(sol)
        ans = l, r
    if sol > 0:
        r -= 1
    else:
        l += 1

print(sol_list[ans[0]], sol_list[ans[1]])
