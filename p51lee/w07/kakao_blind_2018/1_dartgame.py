import re

def solution(dartResult):
    num = re.compile("[0-9]+")
    nonu = re.compile("[^0-9]+")
    base = list(map(int, num.findall(dartResult)))
    attr = nonu.findall(dartResult)
    for i in range(len(base)):
        a = attr[i]
        if a[0] == "D":
            base[i] = base[i] ** 2
        elif a[0] == "T":
            base[i] = base[i] ** 3
        if a[-1] == "*":
            base[i] *= 2
            if i != 0:
                base[i-1] *= 2
        elif a[-1] == "#":
            base[i] *= -1
    return sum(base)
