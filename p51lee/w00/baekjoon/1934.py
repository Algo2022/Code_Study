from sys import stdin

pairs = []
for _ in range(int(stdin.readline())):
    pairs.append(map(int, stdin.readline().split()))

for a, b in pairs:
    p, q = a, b
    if p % q == 0:
        print(p)
        continue
    elif q % p == 0:
        print(q)
        continue
    while p != q:
        if p > q:
            p %= q
            if not p:
                p += q
        else:
            q %= p
            if not q:
                q += p
    print(a*b//p)

