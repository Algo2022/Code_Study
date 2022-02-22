import sys

point_list = []

for _ in range(int(sys.stdin.readline())):
    point_list.append(list(map(int, sys.stdin.readline().split())))

point_list.sort(key=lambda x: x[::-1])

for point in point_list:
    print(*point, sep=" ")

