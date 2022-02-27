import sys
from collections import defaultdict

t = int(sys.stdin.readline())
a_len = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
b_len = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))

a_sums = defaultdict(int)

for i in range(a_len):
    s = 0
    for j in range(i, a_len):
        s += a[j]
        a_sums[s] += 1

ans = 0

for i in range(b_len):
    s = 0
    for j in range(i, b_len):
        s += b[j]
        ans += a_sums[t-s]

print(ans)
