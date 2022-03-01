from sys import stdin
from collections import Counter

_ = int(stdin.readline())
numbers = list(map(int, stdin.readline().split()))
x = int(stdin.readline())

number_dict = Counter(numbers)
numbers = list(number_dict.keys())
numbers.sort()

left = 0
right = len(numbers) - 1

ans = 0
while left < right:
    l = numbers[left]
    r = numbers[right]
    s = l + r
    if s == x:
        ans += number_dict[l] * number_dict[r]
        left += 1
        right -= 1
    elif s < x:
        left += 1
    elif s > x:
        right -= 1

if numbers[left] * 2 == x:
    l = numbers[left]
    ans += number_dict[l] * (number_dict[l] - 1)

print(ans)

