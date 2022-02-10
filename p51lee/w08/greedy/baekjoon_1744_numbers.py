import sys

l = int(sys.stdin.readline())
p_numbers = []
n_numbers = []
ones = 0
zeros = 0

for _ in range(l):
    n = int(sys.stdin.readline())
    if n > 1:
        p_numbers.append(n)
    elif n > 0:
        ones += 1
    elif n > -1:
        zeros += 1
    else:
        n_numbers.append(-n)

p_numbers.sort()
n_numbers.sort()
ans = ones

while len(p_numbers) > 1:
    ans += p_numbers.pop() * p_numbers.pop()

while len(n_numbers) > 1:
    ans += n_numbers.pop() * n_numbers.pop()

if p_numbers:
    ans += p_numbers[0]
if n_numbers:
    if not zeros:
        ans -= n_numbers[0]

print(ans)
