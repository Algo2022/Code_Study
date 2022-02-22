from sys import stdin
from collections import deque

left = deque(list(stdin.readline()[:-1]))
right = deque()
inst_list = []
for _ in range(int(stdin.readline())):
    inst_list.append(stdin.readline().strip())

for inst in inst_list:
    if inst == "L":
        if left:
            right.appendleft(left.pop())
    elif inst == "D":
        if right:
            left.append(right.popleft())
    elif inst == "B":
        if left:
            left.pop()
    elif inst.startswith("P"):
        left.append(inst[2])
print(*(left+right), sep="")
