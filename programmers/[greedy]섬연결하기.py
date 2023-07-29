def solution(n, costs):
    answer = 0
    costs.sort(key = lambda x:x[2])
    link = set([costs[0][0]])
    while len(link) < n:
        for cost in costs:
            if cost[0] in link and cost[1] in link:
                continue
            if cost[0] in link or cost[1] in link:
                link.update([cost[0], cost[1]])
                answer += cost[2]
                break
    return answer

n = 4
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
print(solution(n, costs))