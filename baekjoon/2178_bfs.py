from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    global n, m, arr
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    visited = [[0 for _ in range(n)] for _ in range(m)]
    visited[0][0] = 1
    visited[-1][-1] = 2e9
    queue = deque([(0,0)])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            cx = x + dx[i]
            cy = y + dy[i]
            if cx == n-1 and cy == m-1:
                visited[cy][cx] = min(visited[y][x]+1, visited[cy][cx])
                break
            if 0 <= cx < n and 0 <= cy < m:
                if visited[cy][cx] == 0 and arr[cy][cx]=='1':
                    queue.append((cx,cy))
                    visited[cy][cx] = visited[y][x] + 1
    return visited[m-1][n-1]
    
m, n = map(int, input().split(' '))
arr = []
for _ in range(m):
    arr.append(list(input()))

print(bfs())