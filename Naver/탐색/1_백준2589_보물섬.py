from collections import deque
import sys

input = sys.stdin.readline
l, w = map(int, input().split(' '))
treasure_map = []
for _ in range(l):
    treasure_map.append(list(str(input())))


def get_furthest_distance(y,x,visited):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    q = deque([[x,y,0]])
    visited[y][x] = 1
    while q:
        now_x, now_y, distance = q.popleft()
        for i in range(4):
            next_x = now_x + dx[i]
            next_y = now_y + dy[i]
            if 0 <= next_x < w and 0 <= next_y < l and treasure_map[next_y][next_x] == 'L' and visited[next_y][next_x] == 0:
                q.append([next_x, next_y, distance+1])
                visited[next_y][next_x] = distance+1
    
    max_distance = 0
    for line in visited:
        max_distance = max(max_distance, max(line))    
    return max_distance

# 보물은 가장 먼 육지 사이에 묻혀있다. 
# 모든 육지 사이를 거리를 구하는 문제

distance = []
for i in range(l):
    for j in range(w):
        if treasure_map[i][j] == 'W':
            continue
        visited = [[0 for _ in range(w)] for _ in range(l)]
        distance.append(get_furthest_distance(i,j,visited))
print(max(distance))