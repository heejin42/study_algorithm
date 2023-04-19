from collections import deque
def solution(maps):
    x = len(maps[0])
    y = len(maps)
    queue = deque([(0,0)])
    graph = [[0 for _ in range(x)] for _ in range(y)]
    graph[0][0] = 1
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    while queue:
        now_x, now_y = queue.popleft()
        if now_x == x-1 and now_y == y-1:
            return graph[now_y][now_x]
        for i in range(4):
            new_x = now_x + dx[i]
            new_y = now_y + dy[i]
            if 0<=new_x<x and 0<=new_y<y and maps[new_y][new_x] == 1:
                if graph[new_y][new_x] == 0:
                    graph[new_y][new_x] = graph[now_y][now_x] + 1
                    queue.append((new_x, new_y))
    return -1
