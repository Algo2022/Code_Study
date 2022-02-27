from sys import stdin

n, b = map(int, stdin.readline().split())

number_dict = dict()
number_dict.update({ i: str(i) for i in range(0, 10)})
number_dict.update({i+10: chr(ord('A')+i) for i in range(26)})

ans = ""
while n:
    r = n % b
    n //= b
    ans = number_dict[r] + ans
print(ans)

