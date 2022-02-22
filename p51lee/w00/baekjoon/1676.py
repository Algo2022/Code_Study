from sys import stdin
from math import log

n = int(stdin.readline())
if n == 0:
    print(0)
    quit()
k = int(log(n, 5))

ans = 0
for i in range(1, k+1):
    ans += n // 5**i
print(ans)
