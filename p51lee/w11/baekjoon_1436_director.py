from sys import stdin
import re

n = int(stdin.readline())
devil = re.compile("666")

ans = 665
count = 0

while count < n:
    ans += 1
    if devil.search(str(ans)):
        count += 1
print(ans)

