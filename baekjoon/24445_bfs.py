from collections import deque
import sys
input = sys.stdin.readline

n, m, r = map(int, input().split(' '))
queue = deque([r])
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split(' '))
    graph[u].append(v)
    graph[v].append(u)
visited = [False] * (n+1)
result = [0] * (n+1)
cnt = 1
def bfs(r):
    global result, cnt, visited, graph, queue
    result[r] = cnt
    visited[r] = True
    cnt += 1
    while queue:
        x = queue.popleft()
        graph[x].sort(reverse=True)
        for i in graph[x]:
            if visited[i]:
                continue
            queue.append(i)
            result[i] = cnt
            visited[i] = True
            cnt += 1
bfs(r)
for i in result[1:]:
    print(i)