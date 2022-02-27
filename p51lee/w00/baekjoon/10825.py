from sys import stdin

students = []
for _ in range(int(stdin.readline())):
    name, k, e, m = stdin.readline().strip().split()
    students.append((
            -int(k),
            int(e),
            -int(m),
            name))
students.sort()
for s in students:
    print(s[3])
