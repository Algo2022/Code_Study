from sys import stdin
from collections import Counter
from math import inf

n = int(stdin.readline())
a_list = list(map(int, stdin.readline().split()))
pl, mi, ti, di = map(int, stdin.readline().split())

def dfs_max(acc, p, m, t, d):
    if p + m + t + d == 0:
        return acc
    else:
        ans_max = -inf
        a = a_list[-p-m-t-d]
        if p:
            ans_max = max(ans_max, dfs_max(acc+a, p-1, m, t, d))
        if m:
            ans_max = max(ans_max, dfs_max(acc-a, p, m-1, t, d))
        if t:
            ans_max = max(ans_max, dfs_max(acc*a, p, m, t-1, d))
        if d:
            ans_max = max(ans_max, dfs_max(int(acc/a), p, m, t, d-1))
        return ans_max

def dfs_min(acc, p, m, t, d):
    if p + m + t + d == 0:
        return acc
    else:
        ans_min = inf
        a = a_list[-p-m-t-d]
        if p:
            ans_min = min(ans_min, dfs_min(acc+a, p-1, m, t, d))
        if m:
            ans_min = min(ans_min, dfs_min(acc-a, p, m-1, t, d))
        if t:
            ans_min = min(ans_min, dfs_min(acc*a, p, m, t-1, d))
        if d:
            ans_min = min(ans_min, dfs_min(int(acc/a), p, m, t, d-1))
        return ans_min

print(dfs_max(a_list[0], pl, mi, ti, di))
print(dfs_min(a_list[0], pl, mi, ti, di))
