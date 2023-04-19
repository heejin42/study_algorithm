import heapq
def solution(operations):
    heap = []
    for op in operations:
        if op[0] == 'I':
            num = int(op[2:])
            heapq.heappush(heap, num)
        else:
            if len(heap) == 0:
                continue
            if op[2:] == '1':
                heap.remove(max(heap))
            elif op[2:] == '-1':
                heap.remove(min(heap))
    if len(heap) == 0:
        answer = [0, 0]
    else:
        answer = [max(heap), min(heap)]
    return answer


operations = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]
print(solution(operations))