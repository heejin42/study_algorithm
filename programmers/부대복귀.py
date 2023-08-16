from collections import deque

def bfs(s, graph):
    visited = [-1 for _ in range(len(graph))]
    visited[s] = 0
    routes = deque([s])
    while routes:
        now = routes.popleft()
        for x in graph[now]:
            if visited[x] == -1:
                routes.append(x)
                visited[x] = visited[now]+1
    return visited

def solution(n, roads, sources, destination):
    answer = []
    graph = [[] for _ in range(n+1)]
    for a,b in roads:
        graph[a].append(b)
        graph[b].append(a) 
    visited = bfs(destination, graph)
    for s in sources:
        answer.append(visited[s])
    return answer

n = 5
roads = [[1, 2], [1, 4], [2, 4], [2, 5], [4, 5]]
sources = [1, 3, 5]	
destination = 5
print(solution(n, roads, sources, destination))