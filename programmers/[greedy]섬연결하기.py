# def solution(n, costs):
#     answer = 0
#     costs.sort(key = lambda x:x[2])
#     link = set([costs[0][0]])
#     while len(link) < n:
#         for cost in costs:
#             if cost[0] in link and cost[1] in link:
#                 continue
#             if cost[0] in link or cost[1] in link:
#                 link.update([cost[0], cost[1]])
#                 answer += cost[2]
#                 break
#     return answer

# n = 4
# costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
# print(solution(n, costs))


# n개의 섬 사이 다리 건설 비용이 주어질 떄, 모두 연결하는 경우의 최소 비용을 구하라
from collections import deque
def solution(n, costs):
    costs.sort(key = lambda x:x[2])
    queue = deque(costs)
    linked = set([costs[0][0]])
    cost = 0
    while len(linked) < n:
        for a,b,c in queue:
            if a not in linked and b in linked:
                cost += c
                linked.add(a)
                break
            if a in linked and b not in linked:
                cost += c
                linked.add(b)
                break
    return cost

    
n = 4    
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
print(solution(n, costs))