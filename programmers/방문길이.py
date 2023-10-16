#  처음 걸어본 길이를 구하기
def solution(dirs):
    x, y = 0, 0
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    answer = 0
    visited = [[0 for _ in range(6)] for _ in range(6)]
    visited[0][0] = 1
    before = [[[] for _ in range(6)] for _ in range(6)]
    # 간 길의 경우 양쪽 다 등록해야 한다.
    for d in dirs:
        if d == 'U':
            new_x = x + dx[0]
            new_y = y + dy[0]
        elif d == 'D':
            new_x = x + dx[1]
            new_y = y + dy[1]
        elif d == 'R':
            new_x = x + dx[2]
            new_y = y + dy[2]
        else:
            new_x = x + dx[3]
            new_y = y + dy[3]
        
        if new_x > 5 or new_x < -5 or new_y > 5 or new_y < -5:
            continue
        
        if visited[new_y][new_x] == 0:
            visited[new_y][new_x] = 1
            before[new_y][new_x].append((x, y))
            before[y][x].append((new_x, new_y))
            answer += 1
        else:
            if (new_x, new_y) not in before[y][x] and (x, y) not in before[new_y][new_x]:
                before[new_y][new_x].append((x, y))
                before[y][x].append((new_x, new_y))
                answer += 1
                
        x = new_x
        y = new_y
                
    return answer
            
            
dirs = "ULURRDLLU"
print(solution(dirs))