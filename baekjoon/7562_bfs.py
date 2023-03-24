from collections import deque
import sys
input = sys.stdin.readline

def bfs(start_x, start_y, target_x, target_y, n):
    dx = [1, 2, -1, -2, 1, 2, -1, -2]
    dy = [2, 1, 2, 1, -2, -1, -2, -1]
    queue = deque([(start_x, start_y)])
    visited = [[0 for _ in range(n)] for _ in range(n)]
    while queue:
        x, y = queue.popleft()
        if x == target_x and y == target_y:
            return visited[y][x]
        for i in range(8):
            cx = x + dx[i]
            cy = y + dy[i]
            if 0 <= cx < n and 0 <= cy < n and visited[cy][cx] == 0:
                visited[cy][cx] = visited[y][x] + 1
                queue.append((cx, cy))


T = int(input())
for t in range(T):
    n = int(input())
    start_x, start_y = map(int, input().split(' '))
    target_x, target_y = map(int, input().split(' '))
    print(bfs(start_x, start_y, target_x, target_y, n))