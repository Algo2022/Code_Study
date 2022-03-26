def diff(word1, word2):
    d = 0
    for c1, c2 in zip(word1, word2):
        if c1 != c2:
            d += 1
    return d


def dfs(target, words, p, adj, node, depth):
    p = p[:]
    if target == words[node]:
        return depth
    elif not p:
        return 0
    ans = []
    for i in range(len(words)):
        if i in p and adj[node][i]:
            p.remove(i)
            a = dfs(target, words, p, adj, i, depth + 1)
            if a > 0:
                ans.append(a)
    if ans:
        return min(ans)
    else:
        return 0


def solution(begin, target, words):
    if target not in words:
        return 0
    words.append(begin)
    adj = [[] for _ in range(len(words))]
    for i, word1 in enumerate(words):
        for word2 in words:
            if diff(word1, word2) == 1:
                adj[i].append(1)
            else:
                adj[i].append(0)
    p = list(range(len(words)))
    node = p.pop()
    return dfs(target, words, p, adj, node, 0)
