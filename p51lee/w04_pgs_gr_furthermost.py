def adj_list(n, edge):
    l = {i: [] for i in range(n)}
    for e in edge:
        l[e[0]-1].append(e[1]-1)
        l[e[1]-1].append(e[0]-1)
    return l


def solution(n, edge):
    edge_dict = adj_list(n, edge)
    p = [0 for _ in range(n)]
    v = n - 1
    p[0] = 1
    q_curr = [0]
    q_next = []
    while v:
        ans = 0
        while q_curr:
            node = q_curr.pop()
            for i in edge_dict[node]:
                if p[i] == 0:
                    p[i] = 1
                    v -= 1
                    q_next.append(i)
                    ans += 1
        q_curr = q_next[:]
        q_next = []
    return ans
