from sys import stdin
from bisect import bisect_left, insort

n, m, k = map(int, stdin.readline().split())
data = dict([tuple(map(int, stdin.readline().split())) for _ in range(n)])
insts = [tuple(map(int, stdin.readline().split())) for _ in range(m)]
keys = list(data.keys())
keys.sort()

def find_key(key):
    i = bisect_left(keys, key)
    if i == 0:
        if keys[0] - key <= k:
            return keys[0]
        else:
            return -1
    elif i == len(keys):
        if key - keys[-1] <= k:
            return keys[-1]
        else:
            return -1
    else:
        diff1 = abs(keys[i-1] - key)
        diff2 = abs(key - keys[i])
        if min(diff1, diff2) > k:
            return -1
        if diff1 > diff2:
            return keys[i]
        elif diff1 < diff2:
            return keys[i-1]
        else:
            return -2

for inst in insts:
    opcode = inst[0]
    if opcode == 1:
        key, value = inst[1:]
        data[key] = value
        insort(keys, key)
    elif opcode == 2:
        key, value = inst[1:]
        newkey = find_key(key)
        if newkey >= 0:
            data[newkey] = value
    elif opcode == 3:
        key = inst[1]
        newkey = find_key(key)
        if newkey == -1:
            print(-1)
        elif newkey == -2:
            print("?")
        else:
            print(data[newkey])

