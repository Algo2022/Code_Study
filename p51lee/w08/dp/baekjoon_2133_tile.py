import sys
from collections import defaultdict

n = int(sys.stdin.readline())
cases = defaultdict(int)

cases[2] = 3
for i in range(4, n+2, 2):
    cases[i] += 3 * cases[i-2]
    for j in range(2, i-2, 2):
       cases[i] += 2 * cases[j]
    cases[i] += 2
print(cases[n])
