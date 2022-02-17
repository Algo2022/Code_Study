import sys
import copy
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())

lab_map = []
for _ in range(n):
    lab_map.append(list(map(int, sys.stdin.readline().split())))

zeros = []
twos = []
safes = []
for i in range(n):
    for j in range(m):
        curr = lab_map[i][j]
        if curr == 0:
            zeros.append((i, j))
        elif curr == 2:
            twos.append((i, j))

wall_cases = combinations(zeros, 3)
for wall_case in wall_cases:
    new_lab_map = copy.deepcopy(lab_map)
    safe = 0

    for new_wall in wall_case:
        i, j = new_wall
        new_lab_map[i][j] = 1

    for two in twos:
        q = [two]
        while q:
            i, j =q.pop()
            new_lab_map[i][j] = 2
            neighbors = [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]
            while neighbors:
                i_n, j_n = neighbors.pop()
                if 0 <= i_n < n and 0 <= j_n < m and new_lab_map[i_n][j_n] == 0:
                    q.append((i_n,j_n))

    for i in range(n):
        for j in range(m):
            if new_lab_map[i][j] == 0:
                safe += 1

    safes.append(safe)

print(max(safes))
