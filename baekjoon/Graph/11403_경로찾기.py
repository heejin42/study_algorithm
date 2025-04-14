import sys
n = int(sys.stdin.readline())
graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split(' '))))

visited = [0 for _ in range(n+1)]

def dfs(x):
    for i in range(n):
        if graph[x][i] == 1 and visited[i] == 0:
            visited[i] = 1
            dfs(i)

for i in range(n):
    dfs(i)
    for j in range(n):
        if visited[j] == 1:
            print(1, end=' ')
        else:
            print(0, end=' ')
    print()
    visited = [0 for _ in range(n+1)]
    