from collections import deque
import sys
n,m,r = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]

for i in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

visited_dfs = [0]*(n+1)
visited_bfs = [0]*(n+1)
count_dfs = 1
count_bfs = 1

def dfs(v):
    global visited_dfs, count_dfs
    print(v, end = ' ')
    visited_dfs[v] = 1
    if count_dfs == n:
        return
    arr = sorted(graph[v])
    for x in arr:
        if visited_dfs[x] == 0:
            count_dfs += 1
            dfs(x)
        else:
            continue
queue = deque()
def bfs(v):
    global visited_bfs, count_bfs
    arr = sorted(graph[v])
    for x in arr:
        if visited_bfs[x] == 0:
            print(x, end=' ')
            visited_bfs[x] = 1
            queue.append(x)
            count_bfs += 1
    if count_bfs == n:
        return
    while queue:
        bfs(queue.popleft())


dfs(r)
print()
print(r, end = ' ')
visited_bfs[r] = 1
bfs(r)