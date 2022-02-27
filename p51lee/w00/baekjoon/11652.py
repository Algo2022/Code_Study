from sys import stdin
from collections import Counter

num_list = []
for _ in range(int(stdin.readline())):
    num_list.append(int(stdin.readline()))

print(max(list(Counter(num_list).items()), key=lambda x:(x[1], -x[0]))[0])

