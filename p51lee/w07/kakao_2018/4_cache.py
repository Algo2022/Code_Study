from collections import deque

def solution(cacheSize, cities):
    cities_dq = deque(map(lambda s: s.lower(), cities))
    cities_num = len(cities)
    cache = deque()
    cacheAlloc = 0
    answer = 0
    while cities_dq:
        curr = cities_dq.popleft()
        if curr in cache:
            cache.remove(curr)
            cache.append(curr)
            answer += 1
        else:
            answer += 5
            cache.append(curr)
            if cacheAlloc == cacheSize:
                cache.popleft()
            else:
                cacheAlloc += 1
    return answer
