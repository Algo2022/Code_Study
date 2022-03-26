from sys import stdin

word = stdin.readline().strip()

suffices = [word[i:] for i in range(len(word))]
suffices.sort()
print(*suffices, sep="\n")
