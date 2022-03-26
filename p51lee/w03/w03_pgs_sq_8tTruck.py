from collections import deque


def solution(bridge_length, weight, truck_weights):
    bridge_head = deque([0] * (bridge_length - 1))
    answer = bridge_length
    head_sum = 0
    for truck_weight in truck_weights:
        while head_sum + truck_weight > weight:
            bridge_head.appendleft(0)
            head_sum -= bridge_head.pop()
            answer += 1
        head_sum += truck_weight
        bridge_head.appendleft(truck_weight)
        head_sum -= bridge_head.pop()
        answer += 1
    return answer
