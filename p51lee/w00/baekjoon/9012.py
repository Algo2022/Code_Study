from sys import stdin

ps_list = []
for _ in range(int(stdin.readline())):
    ps_list.append(stdin.readline().strip())

for ps in ps_list:
    stack = 0
    valid = True
    for p in ps:
        if p == "(":
            stack += 1
        else:
            if stack:
                stack -= 1
            else:
                valid = False
                break
    if valid and stack == 0:
        print("YES")
    else:
        print("NO")
