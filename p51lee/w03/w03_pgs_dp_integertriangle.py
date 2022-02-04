def solution(triangle):
    choice = [0] * len(triangle)

    for layer in triangle[::-1][:-1]:
        choice_buff = choice[:]
        choice = []

        for m, n, p, q in zip(layer[:-1], layer[1:], choice_buff[:-1], choice_buff[1:]):
            choice.append(max(m + p, n + q))

    return choice[0] + triangle[0][0]