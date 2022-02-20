import sys

def trans(move, n, m):
    new_move = []
    for x in move:
        if x == n:
            new_move.append(m)
        elif x == m:
            new_move.append(n)
        else:
            new_move.append(x)
    return new_move

def solution(n):
    if n == 1:
        return [[1, 3]]
    else:
        ans = []
        sub_ans = solution(n-1)
        for move in sub_ans:
            ans.append(trans(move, 2, 3))
        ans.append([1, 3])
        for move in sub_ans:
            ans.append(trans(move, 1, 2))
        return ans

n = int(sys.stdin.readline())
sol = solution(n)
print(len(sol))
for move in sol:
    print(*move, sep=" ")

