from sys import stdin
from math import log

def fives(n):
    if n == 0:
        return 0
    k = int(log(n, 5))

    ans = 0
    for i in range(1, k+1):
        ans += n // 5**i
    return ans

def twos(n):
    if n == 0:
        return 0
    k = int(log(n, 2))

    ans = 0
    for i in range(1, k+1):
        ans += n // 2**i
    return ans

n, m = map(int, stdin.readline().split())

print(min(fives(n)-fives(m)-fives(n-m), twos(n)-twos(m)-twos(n-m)))

