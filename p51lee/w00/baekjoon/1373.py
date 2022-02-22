from sys import stdin

print(oct(int("0b" + stdin.readline().strip(), 2))[2:])
