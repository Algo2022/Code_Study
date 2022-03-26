def solution(routes):
    ans = 1

    routes.sort(key=lambda route: route[0])

    end = routes[0][1]
    for route in routes:
        if route[0] > end:
            ans += 1
            end = route[1]
        elif end > route[1]:
            end = route[1]

    return ans
