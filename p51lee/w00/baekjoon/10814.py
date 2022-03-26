from sys import stdin

members = []
for _ in range(int(stdin.readline())):
    age, name = stdin.readline().split()
    members.append((int(age), name))

members.sort(key=lambda x: x[0])

for mem in members:
    print(*mem, sep=" ")

