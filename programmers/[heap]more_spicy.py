import heapq
def solution(scoville, k):
    answer = 0
    heap = []
    for s in scoville:
        heapq.heappush(heap, s)
    while heap[0] < k:
        try:
            first = heapq.heappop(heap)
            second = heapq.heappop(heap)
            new = first + (second * 2)
            answer += 1
            heapq.heappush(heap, new)
        except IndexError:
            return -1
    return answer

scoville = [1, 2, 3, 9, 10, 12]
k = 7
print(solution(scoville, k))