from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
map = []
for n in range(N):
    map.append(list(input().strip()))
visited = [[False for _ in range(N)] for _ in range(N)]

def bfs(x, y):
    global map, visited, N
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    cnt = 1
    queue = deque([(x, y)])
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            cx = x + dx[i]
            cy = y + dy[i]
            if cx < 0 or cx >= N or cy < 0 or cy >= N:
                continue
            if map[cx][cy] == '1' and visited[cx][cy] == False:
                queue.append((cx, cy))
                visited[cx][cy] = True
                cnt += 1
    return cnt


result = []
for i in range(N):
    for j in range(N):
        if visited[i][j] == False and map[i][j] == '1':
            cnt = bfs(i, j)
            result.append(cnt)
        
result.sort()
print(len(result))
for i in result:
    print(i)