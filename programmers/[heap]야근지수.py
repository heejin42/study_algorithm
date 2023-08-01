import heapq
def solution(works, n):
    # 야근 피로도 = 남은 일들의 작업량 제곱하여 더한 값
    # 1시간에 작업량 1만큼 할 수 있고, n 시간 남아있다고 할 때, 최소 야근 피로도 구하기
    # works < 20,000 / work < 50000, n < 1,000,000
    # 제곱의 합을 줄인다? 전체적으로 큰 값을 줄인다! n만큼 계속 정렬하면? 시간 복잡도..
    # 시간복잡도를 줄이기 위해 list를 정렬하는 것이 아닌 힙을 사용해보자!
    works = [-work for work in works]
    heapq.heapify(works)
    for _ in range(n):
        work = heapq.heappop(works) 
        if work == 0:
            return 0
        else:
            heapq.heappush(works, work+1)
    total = 0
    for work in works:
        total += (work*work)
    return total

works = [4,3,3]
n = 4
print(solution(works, n))