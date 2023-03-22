from collections import deque
import sys
input = sys.stdin.readline

def bfs(r):
    global cnt, visited, result, graph
    visited[r] = True
    result[r] = cnt
    cnt += 1
    queue = deque([r])
    while queue:
        x = queue.popleft()
        graph[x].sort()
        for i in graph[x]:
            if visited[i]:
                continue
            queue.append(i)
            visited[i] = True
            result[i] = cnt
            cnt += 1


n, m, r = map(int, input().split(' '))
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split(' '))
    graph[u].append(v)
    graph[v].append(u)


visited = [False] * (n+1)
result = [0] * (n+1)
cnt = 1
bfs(r)
for i in result[1:]:
    print(i)