from sys import stdin

stdin.readline()
s = set(map(int, stdin.readline().split()))
stdin.readline()
l = list(map(int, stdin.readline().split()))

for x in l:
    if x in s:
        print(1)
    else:
        print(0)
