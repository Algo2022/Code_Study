import sys
from collections import deque

n = int(sys.stdin.readline())

wine_list = []
for _ in  range(n):
    wine_list.append(int(sys.stdin.readline()))

if n <= 2:
    print(sum(wine_list))
else:
    initial_state = [
            wine_list[0],
            wine_list[1],
            sum(wine_list[:2])
            ]

    wine_state = deque(initial_state)

    for wine in  wine_list[2:]:
        wine_state.appendleft(max(wine_state))
        wine_state[1] += wine
        wine_state[2] += wine
        wine_state.pop()
    print(max(wine_state))
