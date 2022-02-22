from sys import stdin
from itertools import combinations

def gcd(a, b):
    p, q = a, b
    if p % q == 0:
        return q
    elif q % p == 0:
        return p
    while p != q:
        if p > q:
            p %= q
            if not p:
                p += q
        else:
            q %= p
            if not q:
                q += p
    return p

cases = []
for _ in range(int(stdin.readline())):
    cases.append(map(int, stdin.readline().split()[1:]))

for c in cases:
    pairs = list(combinations(c, 2))
    ans = 0
    for a, b in pairs:
        ans += gcd(a, b)
    print(ans)


