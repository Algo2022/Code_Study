from collections import defaultdict

def solution(k, room_number):
    used = defaultdict(int)
    answer = []
    for n in room_number:
        route = []
        while used[n]:
            route.append(n)
            n += used[n]
        used[n] += 1
        for m in route:
            used[m] = n - m
        answer.append(n)
    return answer
