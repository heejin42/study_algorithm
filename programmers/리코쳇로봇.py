from collections import deque
def solution(board):
    # D 장애물, R 처음 위치, G 목표 지점
    # 한번 이동하면 부딪힐 때까지 가야한다.
    # 최소 이동횟수를 구하자, 만약 갈 수 없다면 -1 리턴
    # 최소 이동.. bfs 문제!
    height = len(board)
    width = len(board[0])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque()
    dist = [[200 for _ in range(width)] for _ in range(height)]
    for i in range(height):
        for j in range(width):
            if board[i][j] == 'R':
                q.append([i, j, 0])
                dist[i][j] = 0
                break
        if q:
            break
            
    while q:
        x,y,d = q.popleft()
        if board[x][y] == 'G':
            return d
        for i in range(4):
            n_x = x
            n_y = y
            while 0<=n_x+dx[i]<height and 0<=n_y+dy[i]<width and board[n_x+dx[i]][n_y+dy[i]]!='D':
                n_x += dx[i]
                n_y += dy[i]
            dist[n_x][n_y] = min(dist[n_x][n_y], d+1)
            q.append([n_x, n_y, d+1])
            
    result = -1
    return result

board = ["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]
print(solution(board))

