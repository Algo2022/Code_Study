def move(curr, arrow):
    if arrow == 0:
        return curr[0], curr[1] + 1
    elif arrow == 1:
        return curr[0] + 1, curr[1] + 1
    elif arrow == 2:
        return curr[0] + 1, curr[1]
    elif arrow == 3:
        return curr[0] + 1, curr[1] - 1
    elif arrow == 4:
        return curr[0], curr[1] - 1
    elif arrow == 5:
        return curr[0] - 1, curr[1] - 1
    elif arrow == 6:
        return curr[0] - 1, curr[1]
    elif arrow == 7:
        return curr[0] - 1, curr[1] + 1
    
    
def solution(arrows):
    curr = (0, 0)
    edges = set()
    vertices = set()
    centers = set()
    vertices.add(curr)
    for arrow in arrows:
        if arrow == 1 and ((move(curr, 0), move(curr, 2))) in edges:
            centers.add((curr[0] + 0.5, curr[1] + 0.5))
        elif arrow == 3 and ((move(curr, 2), move(curr, 4))) in edges:
            centers.add((curr[0] + 0.5, curr[1] - 0.5))
        elif arrow == 5 and ((move(curr, 4), move(curr, 6))) in edges:
            centers.add((curr[0] - 0.5, curr[1] - 0.5))
        elif arrow == 7 and ((move(curr, 6), move(curr, 0))) in edges:
            centers.add((curr[0] - 0.5, curr[1] + 0.5))
        prev = curr
        curr = move(curr, arrow)
        edges.add((prev, curr))
        edges.add((curr, prev))
        vertices.add(curr)
    return len(edges) / 2 - len(vertices) + 1 + len(centers)
