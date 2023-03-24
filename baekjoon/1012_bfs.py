from collections import deque
import sys
input = sys.stdin.readline

T = int(input()) 

def bfs(x, y, visited, arr):
    global m, n
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    queue = deque([(x,y)])
    visited[y][x] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            cx = x + dx[i]
            cy = y + dy[i]
            if 0 <= cx < m and 0 <= cy < n:
                if arr[cy][cx] == 1 and visited[cy][cx] == False:
                    queue.append((cx, cy))
                    visited[cy][cx] = True


def solve():
    global m, n, k
    arr = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split(' '))
        arr[y][x] = 1

    count = 0
    visited = [[False for _ in range(m)] for _ in range(n)]
    
    for x in range(m):
        for y in range(n):
            if visited[y][x] == False and arr[y][x] == 1:
                bfs(x, y, visited, arr)
                count += 1
    return count

for t in range(T):
    m, n, k = map(int, input().split(' '))
    print(solve())