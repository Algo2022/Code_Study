def is_valid(n, costs):
    connected_island = {costs[0][0]}

    for _ in range(len(costs)):
        set_temp = connected_island.copy()
        for island in set_temp:
            for cost in costs:
                if cost[0] == island:
                    connected_island.add(cost[1])
                elif cost[1] == island:
                    connected_island.add(cost[0])
    if len(connected_island) < n:
        return False
    else:
        return True


def solution(n, costs):
    costs.sort(key=lambda cost: cost[2])
    answer = sum(cost[2] for cost in costs)
    for _ in costs.copy():
        expensive_cost = costs.pop()
        if not is_valid(n, costs):
            costs.insert(0, expensive_cost)
        else:
            answer -= expensive_cost[2]

    return answer
