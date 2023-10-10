# 갈 수 있는 경로가 정해져 있다.
# 아이템은 테두리 위 어딘가에 있다.
# 최소 경로 -> bfs
from queue import PriorityQueue
from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    route = [[0 for _ in range(102)] for _ in range(102)]
    # 갈 수 없는 길 0 -1, 갈 수 있는 길 1
    for r in rectangle:
        x1, y1, x2, y2 = map(lambda x: x*2, r)
        # 먼저 안을 -1로, 테두리를 0일 경우에 1로
        for i in range(x1+1, x2):
            for j in range(y1+1, y2):
                route[j][i] = -1
        for i in range(x1, x2+1):
            if route[y1][i] == 0:
                route[y1][i] = 1
            if route[y2][i] == 0:
                route[y2][i] = 1
        for j in range(y1, y2+1):
            if route[j][x1] == 0:
                route[j][x1] = 1
            if route[j][x2] == 0:
                route[j][x2] = 1
    
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    queue = deque([[characterX*2, characterY*2]])
    visited = [[-1 for _ in range(102)] for _ in range(102)]
    visited[characterY*2][characterX*2] = 0
    while True:
        now_x, now_y = queue.popleft()
        if now_x == itemX*2 and now_y == itemY*2:
            answer = visited[now_y][now_x]
            break
        for d in range(4): 
            if route[now_y+dy[d]][now_x+dx[d]] == 1 and visited[now_y+dy[d]][now_x+dx[d]]==-1:
                queue.append([now_x+dx[d], now_y+dy[d]])
                visited[now_y+dy[d]][now_x+dx[d]] = visited[now_y][now_x] + 1
    return answer//2

rectangle = [[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]]
characterX = 1
characterY = 3 
itemX = 7
itemY = 8
result = 17

print(solution(rectangle, characterX, characterY, itemX, itemY))