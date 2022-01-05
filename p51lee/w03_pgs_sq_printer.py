from collections import deque


def solution(priorities, location):
    answer = 0
    priorities_deque = deque(enumerate(priorities))
    priorities_sorted = sorted(priorities, reverse=True)
    while priorities_deque:
        if priorities_sorted[0] == priorities_deque[0][1]:
            priorities_sorted.pop()
            printed = priorities_deque.popleft()
            answer += 1
            if printed[0] == location:
                break
        else:
            priorities_deque.rotate(-1)
    return answer

print(solution([1,1,9,1,1,1], 0)
