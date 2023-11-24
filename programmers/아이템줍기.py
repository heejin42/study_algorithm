from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    # 테두리로만 이동 가능하며 아이템을 줍기 위한 최단 경로를 구하라
    # 그렇다면 먼저 이동 가능한 경로를 체크해야 한다.
    # 그리고 bfs로 최단 경로를 구하기
    # 예외 경우가 있다. ㄷ자 경로의 경우 바로 이동하는 걸 방지하기 위해 좌표를 두배로 만들고 이동거리의 절반을 리턴하자.
    graph = [[0 for _ in range(101)] for _ in range(101)]
    for x1, y1, x2, y2 in rectangle:
        x1 *= 2
        y1 *= 2
        x2 *= 2
        y2 *= 2
        for x in range(x1, x2+1):
            if graph[y1][x] == 0:
                graph[y1][x] = 1
            if graph[y2][x] == 0:
                graph[y2][x] = 1
        for y in range(y1, y2+1):
            if graph[y][x1] == 0:
                graph[y][x1] = 1
            if graph[y][x2] == 0:
                graph[y][x2] = 1
        for x in range(x1+1, x2):
            for y in range(y1+1, y2):
                graph[y][x] = -1
                
    queue = deque([[characterX*2, characterY*2, 0]])
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    while queue:
        now_x, now_y, distance = queue.popleft()
        if now_x == itemX*2 and now_y == itemY*2:
            return distance//2
        for i in range(4):
            next_x = now_x + dx[i]
            next_y = now_y + dy[i] 
            if 0<=next_x<=100 and 0<=next_y<=100 and graph[next_y][next_x] == 1:
                queue.append([next_x, next_y, distance+1])
                graph[next_y][next_x] = 0
    return 0

rectangle = [[1,1,8,4],[2,2,4,9],[3,6,9,8],[6,3,7,7]]
characterX = 9
characterY = 7 
itemX = 6
itemY = 1
result = 11

print(solution(rectangle, characterX, characterY, itemX, itemY))