from bisect import insort
from sys import stdin

data = []
for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    array = []
    for _ in range(n // 10 + 1):
        array += list(map(int, stdin.readline().split()))
    data.append(array)

for array in data:
    medians = []
    sorted_array = []
    for i, num in enumerate(array):
        insort(sorted_array, num)
        if i % 2 == 0:
            medians.append(sorted_array[i // 2])
    print(len(medians))
    for i in range(len(medians) // 10 + 1):
        print(*medians[i * 10 : (i + 1) * 10])
