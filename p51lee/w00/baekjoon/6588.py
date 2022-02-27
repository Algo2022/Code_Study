from sys import stdin
from collections import defaultdict

numbers = list(map(int, stdin.readlines()[:-1]))
b = max(numbers)

prime_dict = defaultdict(lambda:True)
prime_dict[1] = False

n = 1
while n <= b**0.5:
    if prime_dict[n]:
        for m in range(2*n, b+1, n):
            prime_dict[m] = False
    n += 1

primes = []
for i in range(b+1):
    if prime_dict[i]: primes.append(i)

for n in numbers:
    for p in primes:
        if prime_dict[n-p]:
            print("{} = {} + {}".format(n, p, n-p))
            break
