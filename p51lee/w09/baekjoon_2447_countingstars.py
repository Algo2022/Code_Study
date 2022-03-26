import sys

def solution(n):
    if n == 1:
        return [["*"]]
    else:
        m = n // 3
        ans = [[] for _ in range(n)]
        ans_sub = solution(m)
        for i in range(m):
            ans[i] += ans_sub[i] * 3
            ans[m + i] += ans_sub[i] + [" "] * m + ans_sub[i]
            ans[2 * m + i] += ans_sub[i] * 3
        return ans


n = int(sys.stdin.readline())
for line in solution(n):
    print("".join(line))

