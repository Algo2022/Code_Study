from sys import stdin

a, b = map(int, stdin.readline().split())

p, q = a, b
while p != q:
    if p > q:
        p -= q
    else:
        q -= p
print(p)
p, q = a, b
while p != q:
    if p > q:
        q += b
    else:
        p += a
print(p)

