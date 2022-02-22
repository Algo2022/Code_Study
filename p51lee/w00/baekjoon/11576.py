from sys import stdin

a, b = map(int, stdin.readline().split())
n = int(stdin.readline())
num_a = list(map(int, stdin.readline().split()))

num = 0

for i in num_a:
    num *= a
    num += i

ans = []

while num:
    r = num%b
    num //= b
    ans.append(r)

print(*ans[::-1], sep=" ")
