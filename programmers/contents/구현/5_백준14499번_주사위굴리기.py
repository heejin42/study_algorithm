n, m, x, y, k = map(int, input().split(' '))
board = []
#   1
# 5 2 6
#   3
#   4  
cube = [0 for _ in range(7)]

top_index = 2
bottom_index = 4
# 동 남 서 북
direct_index = [6, 3, 5, 1]

for _ in range(n):
    board.append(list(map(int, input().split(' '))))

move = list(map(int, input().split(' ')))
dx = [0, 1, -1, 0, 0] 
dy = [0, 0, 0, -1, 1]
for i in move:
    next_x =  x + dx[i]
    next_y = y + dy[i]
    if 0<=next_x<m and 0<=next_y<n:
        if i == 1:
            next_bottom = direct_index[0]
            next_top = direct_index[2] 
            direct_index = [top_index, direct_index[1], bottom_index, direct_index[3]]
            top_index = next_top
            bottom_index = next_bottom 
        elif i == 2:
            next_bottom = direct_index[2]
            next_top = direct_index[0] 
            direct_index = [bottom_index, direct_index[1], top_index, direct_index[3]]
            top_index = next_top
            bottom_index = next_bottom 
        elif i == 3:
            next_top = direct_index[3]
            next_bottom = direct_index[1]
            direct_index = [direct_index[0], top_index, direct_index[2], bottom_index]
            top_index = next_top
            bottom_index = next_bottom 
        else:
            next_top = direct_index[1]
            next_bottom = direct_index[3]
            direct_index = [direct_index[0], bottom_index, direct_index[2], top_index]
            top_index = next_top
            bottom_index = next_bottom 
            
        if board[next_y][next_x] != 0:
            cube[bottom_index] = board[next_y][next_x]
            board[next_y][next_x] = 0
        else:
            board[next_y][next_x] = cube[bottom_index]
            
        x = next_x
        y = next_y
        print(cube[top_index])