from sys import stdin
from collections import Counter

word = stdin.readline().strip()
count_list = [word.find(chr(i)) for i in range(ord("a"), ord("z")+1)]
print(*count_list)

