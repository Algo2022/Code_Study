import heapq

def solution(operations):
    min_heap = []
    max_heap = []
    heapq._heapify_max(max_heap)
    for operation in operations:
        opcode, operand = operation.split(" ")
        if opcode == "I":
            heapq.heappush(min_heap, int(operand))
            heapq.heappush(max_heap, -int(operand))
        elif opcode == "D":
            if not (min_heap and max_heap):
                continue
            elif operand == "1":
                min_heap.remove(-heapq.heappop(max_heap))
            elif operand == "-1":
                max_heap.remove(-heapq.heappop(min_heap))
    if min_heap and max_heap:
        return [-heapq.heappop(max_heap), heapq.heappop(min_heap)]
    else:
        return [0, 0]
