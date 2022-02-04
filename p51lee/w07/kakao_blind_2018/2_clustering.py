import re
from collections import defaultdict


def dictify(l):
    d = defaultdict(int)
    for e in l:
        d[e] += 1
    return d


def union(d1, d2):
    d = defaultdict(int)
    for e1 in d1.keys():
        d[e1] = max(d1[e1], d2[e1])
    for e2 in d2.keys():
        d[e2] = max(d1[e2], d2[e2])
    return d


def intersection(d1, d2):
    d = defaultdict(int)
    for e in d1.keys():
        d[e] = min(d1[e], d2[e])
    return d


def solution(str1, str2):
    p = re.compile(r"(?=([a-z]{2}))")
    d1 = dictify(p.findall(str1.lower()))
    d2 = dictify(p.findall(str2.lower()))
    u = sum(union(d1, d2).values())
    i = sum(intersection(d1, d2).values())
    if u == 0:
        return 65536
    else:
        return (i * 65536) // u

