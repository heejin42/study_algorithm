import sys

def dfs(x, idx):
    global visited
    for i in t_graph[idx]:
        if visited[x][i] == 0:
            visited[x][i] = 1
            visited[i][x] = 1
            dfs(x, i)
        
            
    return s_list

n, m = map(int, sys.stdin.readline().split(' '))
t_graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split(' '))
    t_graph[a].append(b)
    
    
answer = 0
for i in range(n):
    visited[i].count(0)
    if visited[i].count(0) == 1:
        answer += 1
        
print(answer)