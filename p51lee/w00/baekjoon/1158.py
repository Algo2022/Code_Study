from sys import stdin
from collections import deque

n, k = map(int, stdin.readline().split())

tree = [0]*300000

def init(node, s, e):
    if s == e:
        tree[node] = 1
        return 1
    else:
        m = (s + e) // 2
        temp = init(2*node, s, m) + init(2*node+1, m+1, e)
        tree[node] = temp
        return temp


def query(node, s, e, o):
    if s == e:
        return s
    else:
        m = (s + e) // 2
        if o <= tree[node*2]:
            return query(node*2, s, m, o)
        else:
            return query(node*2+1, m+1, e, o-tree[node*2])


def update(node, s, e, d):
    tree[node] -= 1
    if s == e:
        return 0
    else:
        m = (s + e) // 2
        if d <= m:
            return update(node*2, s, m, d)
        else:
            return update(node*2+1, m+1, e, d)

m = n
seq = []
i = 1
init(1, 1, n)
print("<", end="")
while m:
    i += k - 1
    i %= m
    if not i:
        i = m
    next = query(1, 1, n, i)
    update(1, 1, n, next)
    print(next, end="")
    if m != 1:
        print(", ", end="")
    m -= 1
print(">")

# print("<{}>".format(", ".join(seq)))

