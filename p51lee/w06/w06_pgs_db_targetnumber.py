def solution(numbers, target):
    answer = 0
    l = len(numbers)
    for x in range(2 ** l):
        x_str = str(bin(x))[2:].zfill(l)
        sum = 0
        for i, sign in enumerate(x_str):
            print(sign)
            if sign == '0':
                sum += numbers[i]
            else:
                sum -= numbers[i]
        if sum == target:
            answer += 1
    return answer
