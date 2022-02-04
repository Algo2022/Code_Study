def solution(msg):
    di = {chr(ord('A')+i): i+1 for i in range(26)}
    tail = 27
    prev = ""
    answer = []
    for c in msg:
        curr = prev + c
        if curr in di.keys():
            prev = curr
        else:
            answer.append(di[prev])
            di[curr] = tail
            tail += 1
            prev = c
    answer.append(di[prev])
    return answer

