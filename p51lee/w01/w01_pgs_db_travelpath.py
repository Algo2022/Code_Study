from copy import deepcopy

def airport_encode(tickets):
    airports = set()
    for [airport1, airport2] in tickets:
        airports.add(airport1)
        airports.add(airport2)
    airport_list = list(airports)
    airport_list.sort()
    airport_to_index = {airport: index for index, airport in enumerate(airport_list)}
    index_to_airport = {index: airport for index, airport in enumerate(airport_list)}
    return airport_to_index, index_to_airport


def find_path(start, footprint, adj, l):
    footprint.append(start)
    if len(footprint) == l:
        return footprint
    ans = []
    for dst, exist in enumerate(adj[start]):
        if exist:
            new_adj = deepcopy(adj)
            new_adj[start][dst] -= 1
            path = find_path(dst, deepcopy(footprint), new_adj, l)
            if path:
                ans.append(path)
    if ans:
        return ans[0]
    else:
        return []

def solution(tickets):
    atoi, itoa = airport_encode(tickets)
    l = len(tickets) + 1
    n = len(atoi)
    adjacent_matrix = [[0]*n for _ in range(n)]
    for [air1, air2] in tickets:
        adjacent_matrix[atoi[air1]][atoi[air2]] += 1
    return [itoa[i] for i in find_path(atoi['ICN'], [], adjacent_matrix, l)]
