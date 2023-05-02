import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(node, distance):
    global graph, visited
    for child, w in graph[node]:
        if visited[child] == -1:
            visited[child] = distance + w
            dfs(child, distance + w)
            
n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    parent, child, w = map(int, input().split(' '))
    graph[parent].append([child, w])
    graph[child].append([parent, w])

visited = [-1 for _ in range(n+1)]
visited[1] = 0
dfs(1, 0)

start = visited.index(max(visited))
visited = [-1 for _ in range(n+1)]
visited[start] = 0
dfs(start, 0)
print(max(visited))    
    