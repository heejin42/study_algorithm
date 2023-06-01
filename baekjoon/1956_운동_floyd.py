import sys
input = sys.stdin.readline
INF = int(1e9)

v, e = map(int, input().split(' '))
graph = [[INF for _ in range(v+1)] for _ in range(v+1)]
for _ in range(e):
    x, y, d = map(int, input().split(' '))
    graph[x][y] = d

for i in range(1, v+1):
    for j in range(1, v+1):
        for k in range(1, v+1):
            graph[i][j]  = min(graph[i][j], graph[i][k] + graph[k][j])
            
answer = INF
for i in range(1, v+1):
    answer = min(answer, graph[i][i])
if answer == INF:
    print(-1)  
else:        
    print(answer)
    

    