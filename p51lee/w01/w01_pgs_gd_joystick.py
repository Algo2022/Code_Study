def letter_diff(chr):
    diff = abs(ord(chr) - ord('A'))
    return min(diff, 26 - diff)


def solution(name):
    l = len(name)
    name_decode = list(map(letter_diff, name))
    i = 0
    answer = 0
    while sum(name_decode) > 0:
        answer += name_decode[i]
        name_decode[i] = 0
        for j in range(1, l):
            if name_decode[(i+j)%l] != 0:
                i = (i+j)%l
                answer += j
                break
            elif name_decode[(i-j)%l] != 0:
                i = (i-j)%l
                answer += j
                break
    return answer
