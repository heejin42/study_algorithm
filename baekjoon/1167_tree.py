import sys
input = sys.stdin.readline

def dfs(pos, distance):
    global visited, graph
    visited[pos] = distance
    for child in graph[pos]:
        if visited[child[0]] == -1:
            visited[child[0]] = distance + child[1]
            dfs(child[0], distance + child[1])         
    

n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n):
    line = list(map(int, input().split(' ')))
    for i in range(1, len(line)-1, 2): 
        graph[line[0]].append([line[i], line[i+1]])
visited = [-1 for _ in range(n+1)]        
dfs(1, 0)
start = visited.index(max(visited))
visited = [-1 for _ in range(n+1)] 
dfs(start, 0)
print(max(visited))