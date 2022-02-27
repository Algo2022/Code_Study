from sys import stdin

ps = stdin.readline().strip()

ans = 0
stack = 0
laser = False
for i in range(0, len(ps)-1):
    curr = ps[i]
    next = ps[i+1]
    if laser:
        laser = False
        continue
    elif curr == "(" and next == ")":
        ans += stack
        laser = True
    elif curr == "(":
        ans += 1
        stack += 1
    elif curr == ")":
        stack -= 1
print(ans)
