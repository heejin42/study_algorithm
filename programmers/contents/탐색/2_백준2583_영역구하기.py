import sys
sys.setrecursionlimit(10000)

def dfs(graph, x, y):
    global n
    global m
    global cnt
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    for i in range(4):
        next_x = x + dx[i]
        next_y = y + dy[i]
        if 0<=next_x<n and 0<=next_y<m and graph[next_y][next_x] == 0:
            cnt += 1
            graph[next_y][next_x] = 1
            dfs(graph, next_x, next_y)
            
            
m, n, k = map(int, input().split(' '))
graph = [[0 for _ in range(n)] for _ in range(m)]
answer = []
for _ in range(k):
    start_x, start_y, end_x, end_y = map(int, input().split(' '))
    for i in range(start_x, end_x):
        for j in range(start_y, end_y):
            graph[j][i] = 1
            
for y in range(m):
    for x in range(n):
        if graph[y][x] == 0:
            graph[y][x] = 1
            cnt = 1
            dfs(graph, x, y)
            answer.append(cnt)
        else:
            continue

answer.sort()
print(len(answer))
print(*answer) 