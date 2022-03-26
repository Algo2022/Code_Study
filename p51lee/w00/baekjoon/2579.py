import sys
from collections import deque

point_list = []
length = int(sys.stdin.readline())
for _ in range(length):
    point_list.append(int(sys.stdin.readline()))

if length <= 2:
    print(sum(point_list))
else:
    dp = deque([
        point_list[0],
        point_list[1],
        sum(point_list[:2])
        ])

    for point in point_list[2:]:
        dp.appendleft(max(dp[1], dp[2]))
        dp[1] += point
        dp[2] += point
        dp.pop

    print(max(dp[1], dp[2]))
