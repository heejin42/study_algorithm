import heapq

def solution(operations):
    heap = []
    for op in operations:
        command, num = op.split(' ')
        if command == 'I':
            heapq.heappush(heap, int(num))
        else:
            if len(heap) == 0:
                continue
            elif num == '1':
                heap.pop()
            elif num == '-1':
                heap.pop(0)
    if len(heap) == 0:
        answer = [0, 0]
    else:
        answer = [max(heap), min(heap)]
    return answer
