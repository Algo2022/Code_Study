from sys import stdin
from collections import Counter

word = stdin.readline().strip()
counter = Counter(word)
count_list = [counter.get(chr(i), 0) for i in range(ord("a"), ord("z")+1)]
print(*count_list)
