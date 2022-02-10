import sys

decode = lambda m, d: sum([31,28,31,30,31,30,31,31,30,31,30][:m-1])+d

l = int(sys.stdin.readline())

flowers = []
for _ in range(l):
    m1, d1, m2, d2 = map(int, sys.stdin.readline().split())
    flowers.append((decode(m1, d1), decode(m2, d2)))

flowers.sort(key=lambda x: x[0])
curr = decode(3, 1)
next = decode(1, 1)
ans = 1

for flower in flowers:
    if next > decode(11, 30):
        break
    elif flower[0] <= curr:
        next = max(next, flower[1])
    elif flower[0] <= next:
        curr = next
        next = flower[1]
        ans += 1
    else:
        ans = 0
        break
if next > decode(11, 30):
    print(ans)
else:
    print(0)
