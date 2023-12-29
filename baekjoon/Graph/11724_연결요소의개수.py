# 정점의 개수 n, 간선의 개수 m이 주어지고, M개의 줄 양 끝 u,v가 주어진다.
# 연결 요소의 개수를 구하라.
# 즉, 그래프 탐색을 통해 몇개의 그래프가 존재하는지 세는 것이다.
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(node, graph, visited):
    visited[node]=1
    for i in graph[node]:
        if visited[i] == 0:
            dfs(i, graph ,visited)          
            
n, m = map(int, input().split(' '))
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split(' '))
    graph[u].append(v)
    graph[v].append(u)
    
answer = 0
visited = [0 for _ in range(n+1)]
for i in range(1, n+1):
    if visited[i] == 0:
        dfs(i, graph, visited)
        answer += 1
print(answer)
    
