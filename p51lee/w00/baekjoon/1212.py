from sys import stdin

print(bin(int("0o" + stdin.readline().strip(), 8))[2:])

