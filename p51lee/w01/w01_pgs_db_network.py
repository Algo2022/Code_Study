def solution(n, computers):
    p = list(range(n))
    q = []
    answer = 0
    while p:
        q.append(p.pop())
        while q:
            node = q.pop()
            for i in range(n):
                if i in p and computers[node][i]:
                    p.remove(i)
                    q.append(i)
        answer += 1
    return answer
