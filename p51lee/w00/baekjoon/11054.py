import sys

length = int(sys.stdin.readline())
sequence = list(map(int, sys.stdin.readline().split()))

dp_dec = []
dp_inc = []

for n in sequence:
    l = 1
    a = 0
    for m, k in dp_inc:
        if m < n:
            a = max(a, k)
    dp_inc.append((n, l+a))

for n in sequence[::-1]:
    l = 1
    a = 0
    for m, k in dp_dec:
        if m < n:
            a = max(a, k)
    dp_dec.append((n, l+a))

dp_dec.reverse()

ans = 0
for i in range(length):
    ans = max(ans, dp_inc[i][1] + dp_dec[i][1] - 1)
print(ans)

