from sys import stdin
from collections import Counter

line_list = stdin.readlines()

for line in line_list:
    counter = Counter(line)
    lower = 0
    upper = 0
    number = 0
    space = 0
    for k, v in counter.items():
        if ord('a') <= ord(k) <= ord('z'):
            lower += v
        elif ord('A') <= ord(k) <= ord('Z'):
            upper += v
        elif ord('0') <= ord(k) <= ord('9'):
            number += v
        elif k == ' ':
            space += v
    print(lower, upper, number, space)
