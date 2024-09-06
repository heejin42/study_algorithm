import sys

def dfs(visited, cnt, i, j):
    global forest
    global n
    global answer
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    answer = max(answer, cnt)
    for k in range(4):
        next_x = j + dx[k]
        next_y = i + dy[k]
        if 0 <= next_x < n and 0 <= next_y < n and visited[next_y][next_x] == 0:
            visited[next_y][next_x] = 1
            cnt += 1
            dfs(visited, cnt, i, j)
            visited[next_y][next_x] = 0
            cnt -= 1
        
    

def solution():
    global forest
    for i in range(n):
        for j in range(n):
            visited = [[0 for _ in range(n)] for _ in range(n)]
            visited[i][j] = 1
            dfs(visited, 0, i, j)
    

n = int(input())
answer = 0
forest = []
for _ in range(n):
    line = list(map(int, sys.stdin.readline().strip().split()))
    forest.append(line)
solution()
print(answer)