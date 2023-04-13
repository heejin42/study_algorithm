from collections import deque
def dfs(maps, start_x, start_y):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1] 
    queue = deque([(start_x, start_y)])
    days = int(maps[start_y][start_x])
    maps[start_y][start_x] = 'X'
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]
            if not 0<=next_x<len(maps[0]) or not 0<=next_y<len(maps):
                continue
            else:
                if maps[next_y][next_x] != 'X':
                    days += int(maps[next_y][next_x])
                    print(days)
                    maps[next_y][next_x] = 'X'
                    queue.append((next_x, next_y))
    return days
        
def solution(maps):
    new_maps = []
    for line in maps:
        new_maps.append(list(line))
    answer = []
    for y in range(len(new_maps)):
        for x in range(len(new_maps[0])):
            if new_maps[y][x] == 'X':
                continue
            else:
                days = dfs(new_maps, x, y)
                answer.append(days)
    if len(answer) > 0:
        answer.sort()
    else:
        answer = [-1]
    return answer

maps = ["X591X","X1X5X","X231X", "1XXX1"]
print(solution(maps))