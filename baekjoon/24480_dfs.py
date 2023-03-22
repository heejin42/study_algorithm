import sys
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

def dfs(v):
    global cnt
    visited[v] = True
    answer[v-1] = cnt
    for i in graph[v]:
        if not visited[i]:
            cnt += 1
            dfs(i)

n, m, r = map(int, input().split(' '))

graph = [[] for _ in range(n+1)]
for i in range(m):
    u, v = map(int, input().split(' '))
    graph[u].append(v)
    graph[v].append(u)
for lst in graph:
    lst.sort(reverse = True)

visited = [False] * (n+1)
cnt = 1
answer = [0] * (n)
dfs(r)
for i in answer:
    print(i)