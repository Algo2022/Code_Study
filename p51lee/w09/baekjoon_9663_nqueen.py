import sys
from collections import defaultdict

n = int(sys.stdin.readline())
ans = 0

def sol(acc):
    n
    global ans
    l = len(acc)
    if l == n:
        ans += 1
    else:
        candidates = [False]*n
        for i, q in enumerate(acc):
            candidates[q] = True
            d = l-i
            if 0 <= q+d < n:
                candidates[q+d] = True
            if 0 <= q-d < n:
                candidates[q-d] = True
        for i in range(n):
            if not candidates[i]:
                sol(acc+[i])

sol([])
print(ans)

