from sys import stdin

n = int(stdin.readline())

ans = ""

while n:
    r = n % 2
    n //= 2
    n *= -1
    ans = str(r) + ans
if ans:
    print(ans)
else:
    print(0)

