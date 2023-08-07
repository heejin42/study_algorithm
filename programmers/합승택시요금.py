import heapq
def solution(n, s, a, b, fares):
    INF = 1e9
    answer = 0
    graph = [[] for _ in range(n+1)]
    for fare in fares:
        aa, bb, price = fare
        graph[aa].append((bb, price))
        graph[bb].append((aa, price))
    
    distance1 = [INF]*(n+1)
    distance1[s] = 0
    q = [(s, 0)]
        
    while q:
        v, dist = heapq.heappop(q)
        for v2, price in graph[v]:
            cost = dist + price
            if distance1[v2] > cost:
                distance1[v2] = cost
                heapq.heappush(q, (v2, cost))
    answer += distance1[a]
    answer += distance1[b]
    
    # 모든 경우에 대해서 탐색
    for k in range(1, n+1):
        
        if k == s:
            continue
        # 탑승해서 간게 크면 패스
        if distance1[k] > answer:
            continue
        distance2 = [INF]*(n+1)
        distance2[k] = 0
        q = [(k, 0)]
        
        subanswer = distance1[k]
        while q:
            v, dist = heapq.heappop(q)
            for v2, price in graph[v]:
                cost = dist + price
                if distance2[v2] > cost:
                    distance2[v2] = cost
                    heapq.heappush(q, (v2, cost))
        subanswer += distance2[a]
        subanswer += distance2[b]
        answer = min(answer, subanswer)
        
    return answer


n = 6
s = 4
a = 6
b = 2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
print(solution(n, s, a, b, fares))