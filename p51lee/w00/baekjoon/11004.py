from sys import stdin

n, k = map(int, stdin.readline().split())
seq = list(map(int, stdin.readline().split()))

seq.sort()
print(seq[k-1])
