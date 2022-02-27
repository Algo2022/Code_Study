from sys import stdin
from collections import defaultdict

a, b = map(int, stdin.readline().split())

prime_dict = defaultdict(lambda:True)
prime_dict[1] = False

n = 1
while n <= b**0.5:
    if prime_dict[n]:
        for m in range(2*n, b+1, n):
            prime_dict[m] = False
    n += 1

for i in range(a, b+1):
    if prime_dict[i]: print(i)

