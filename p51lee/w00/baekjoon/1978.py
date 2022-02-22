from sys import stdin
from collections import defaultdict

length = int(stdin.readline())
numbers = list(map(int, stdin.readline().split()))
max_n = max(numbers)

prime_dict = defaultdict(lambda:True)
prime_dict[1] = False

n = 1
while n <= max_n**0.5:
    if prime_dict[n]:
        for m in range(2*n, max_n+1, n):
            prime_dict[m] = False
    n += 1
print(sum(map(lambda x: prime_dict[x], numbers)))
