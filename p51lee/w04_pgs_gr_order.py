def make_adj(n, results):
    mat = [[0]*n for _ in range(n)]
    for w, l in results:
        mat[w-1][l-1] = 1
        mat[l-1][w-1] = -1
    return mat

def solution(n, results):
    adjmat = make_adj(n, results)
    answer = 0
    for root in range(n):
        pw = list(filter(lambda x: x != root, range(n)))
        qw = [root]
        pl = pw[:]
        ql = qw[:]
        winners = []
        losers = []
        while qw:
            node = qw.pop()
            for op in range(n):
                if op in pw:
                    if adjmat[node][op] == 1:
                        winners.append(op)
                        pw.remove(op)
                        qw.append(op)
        while ql:
            node = ql.pop()
            for op in range(n):
                if op in pl:
                    if adjmat[node][op] == -1:
                        losers.append(op)
                        pl.remove(op)
                        ql.append(op)
        if len(winners) + len(losers) == n - 1:
            answer += 1
    return answer
