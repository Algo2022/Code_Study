def solution(people, limit):
    people.sort()
    answer = 0
    iter1 = 0
    iter2 = len(people) - 1
    while True:
        if iter1 > iter2: break
        elif iter2 - iter1 == 0:
            answer += 1
            break
        elif people[iter2] <= limit / 2:
            answer += (iter2 - iter1 + 2) // 2
            break
        elif people[iter1] + people[iter2] <= limit:
            iter2 -= 1
            iter1 += 1
            answer += 1
        else:
            iter2 -= 1
            answer += 1
    return answer