import sys

case_list = []

for _ in range(int(sys.stdin.readline())):
    case_list.append(int(sys.stdin.readline()))

goal = max(case_list)

seq = [1, 1, 1, 2, 2]

for n in range(6, goal+1):
    seq.append(seq[n-2]+seq[n-6])
for c in case_list:
    print(seq[c-1])
