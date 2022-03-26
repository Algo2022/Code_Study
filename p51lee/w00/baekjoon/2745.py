from sys import stdin

n, b = stdin.readline().strip().split()
b = int(b)

number_dict = dict()
number_dict.update({ str(i): i for i in range(0, 10)})
number_dict.update({chr(ord('A')+i): i+10 for i in range(26)})

ans = 0

for c in n:
    ans *= b
    ans += number_dict[c]
print(ans)

