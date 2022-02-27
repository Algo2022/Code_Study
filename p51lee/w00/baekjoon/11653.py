from sys import stdin
from collections import defaultdict

b = int(stdin.readline())

prime_dict = defaultdict(lambda:True)
prime_dict[1] = False

n = 1
while n <= b**0.5:
    if prime_dict[n]:
        for m in range(2*n, int(b**0.5)+1, n):
            prime_dict[m] = False
    n += 1

primes = []
for i in range(1, int(b**0.5)+1):
    if prime_dict[i]: primes.append(i)

for p in primes:
    while b % p == 0:
        print(p)
        b //= p
if b != 1:
    print(b)
