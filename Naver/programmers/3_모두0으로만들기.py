from collections import deque
def solution(a, edges):
    if sum(a) != 0:
        return -1
    
    graph = [[] for i in range(len(a))]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
        
    q = deque([])
    for i in range(len(a)):
        if len(graph[i]) == 1:
            q.append(i)
            
    
    answer = 0
    while q:
        x = q.popleft()
        if a[x] == 0 or len(graph[x]) == 0:
            continue
        if len(graph[x]) > 1:
            q.append(x)
            continue
        elif len(graph[x]) == 1:
            nx = graph[x][0]
            graph[nx].remove(x)
            a[nx] += a[x]
            answer += a[x]
            a[x] = 0
            if nx not in q:
                q.append(nx)      
    if max(a) == 0 and min(a) == 0:
        return answer
    return -1

a = [0,1,0]
edges = [[0,1],[1,2]]
print(solution(a, edges))