# from collections import deque
# def solution(n, vertex):
#     graph = [[] for _ in range(n+1)]
#     for v in vertex:
#         graph[v[0]].append(v[1])
#         graph[v[1]].append(v[0])
#     visited = [0 for _ in range(n+1)]
#     queue = deque(graph[1])
#     for node in graph[1]:
#         visited[node] = 1
#     while queue:
#         x = queue.popleft()
#         for node in graph[x]:
#             if node == 1:
#                 continue
#             if visited[node] == 0:
#                 visited[node] = visited[x]+1
#                 queue.append(node)
#     answer = visited.count(max(visited))
#     return answer


# 1번 노드부터 가장 멀리 떨어진 노드가 몇개인지 구하라
# bfs
from collections import deque
def solution(n, vertex):
    graph = [[] for _ in range(n+1)]
    for a,b in vertex:
        graph[a].append(b)
        graph[b].append(a)
    visited = [0 for _ in range(n+1)]
    visited[1] = 1
    que = deque([1])
    while que:
        n = que.popleft()
        for i in graph[n]:
            if visited[i] == 0:
                que.append(i)
                visited[i] = visited[n]+1    
    return visited.count(max(visited))

n = 6
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n, vertex))