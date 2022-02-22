import sys

point_list = []

for _ in range(int(sys.stdin.readline())):
    point_list.append(list(map(int, sys.stdin.readline().split())))

point_list.sort()

for point in point_list:
    print(*point, sep=" ")
