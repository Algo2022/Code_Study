import sys

def solution(case, k):
    if len(case) == k:
        return [case]
    elif k == 0:
        return [[]]
    else:
        ans = []
        ans_sub1 = solution(case[1:], k)
        ans_sub2 = solution(case[1:], k-1)
        ans += ans_sub1
        for sub2 in ans_sub2:
            ans.append(case[0:1]+sub2)
        return ans
cases = []

while True:
    curr = list(map(int, sys.stdin.readline().split()))
    if curr[0] == 0:
        break
    else:
        cases.append(curr)

for case in cases:
    sol = solution(case[1:], 6)
    sol.sort()
    solsol = list(map(lambda x: " ".join(map(str, x)), sol))
    for temp in solsol:
        print(temp)
    print()
