def solution(board):
    answer = 1
    success_o = 0
    success_x = 0
    count_o = 0
    count_x = 0
    new_board = []
    for line in board:
        count_o += line.count('O')
        if line.count('O') == 3:
            success_o += 1
        count_x += line.count('X')
        if line.count('X') == 3:
            success_x += 1
        new_board.append(list(line))
 
    if count_x > count_o:
        answer = 0
    
    cross_1 = new_board[0][0]
    flag_1 = True
    cross_2 = new_board[2][0]
    flag_2 = True

    for i in range(3):
        if new_board[0][i] == 'O':
            if new_board[1][i] == 'O' and new_board[2][i] == 'O':
                success_o += 1
        elif new_board[0][i] == 'X':
            if new_board[1][i] == 'X' and new_board[2][i] == 'X':
                success_x += 1
        if new_board[i][i] != cross_1:
            flag_1 = False
        if new_board[2-i][i] != cross_2:
            flag_2 = False
    if flag_1:
        if cross_1 == 'O':
            success_o += 1
        elif cross_1 == 'X':
            success_x += 1
    if flag_2:
        if cross_2 == 'O':
            success_o += 1
        elif cross_2 == 'X':
            success_x += 1
            
    if success_x > 0 and success_o > 0:
        answer = 0 
    elif success_x > 0 and success_o == 0:
        if count_x != count_o:
            answer = 0
    elif success_x == 0 and success_o > 0:
        if count_o != count_x + 1:
            answer = 0
    return answer

board = ["O.X", ".O.", "..X"]
print(solution(board))