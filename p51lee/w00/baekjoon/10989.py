from sys import stdin
from collections import defaultdict

num_dict = defaultdict(int)
for _ in range(int(stdin.readline())):
    num_dict[int(stdin.readline())] += 1

keys = list(num_dict.keys())
keys.sort()

for key in keys:
    for _ in range(num_dict[key]):
        print(key)
