from sys import stdin

word = stdin.readline()

for c in word:
    if ord('A') <= ord(c) <= ord('Z'):
        print(chr(ord('A') + (ord(c) - ord('A') + 13)%26), end="")
    elif ord('a') <= ord(c) <= ord('z'):
        print(chr(ord('a') + (ord(c) - ord('a') + 13)%26), end="")
    else:
        print(c, end="")
