from collections import deque
def solution(maps, lands, w, h):
    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    dy = [1, 1, 0, -1, -1, -1, 0, 1]
    count = 0
    while lands:
        start_x, start_y = lands[0] 
        lands.remove((start_x, start_y))
        maps[start_y][start_x] = 0
        q = deque([(start_x, start_y)])
        count += 1
        while q:
            x, y = q.popleft()
            for i in range(8):
                if 0 <= y + dy[i] < h and 0 <= x + dx[i] < w:
                    if maps[y + dy[i]][x + dx[i]] == 1:
                        q.append((x + dx[i], y + dy[i]))
                        maps[y + dy[i]][x + dx[i]] = 0    
                        lands.remove((x + dx[i], y + dy[i]))     
    return count
        

while True:
    w, h = map(int, input().split(' '))
    if w == 0 and h == 0:
        break
    maps = []
    lands = []
    for i in range(h):
        line = list(map(int, input().split(' ')))
        maps.append(line)
        for j in range(w):
            if line[j] == 1:
                lands.append((j, i))
    if len(lands) == 0:
        print(0)
    else:
        print(solution(maps, lands, w, h))