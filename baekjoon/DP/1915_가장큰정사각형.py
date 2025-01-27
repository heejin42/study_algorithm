n, m = map(int, input().split(' '))
board = []
for _ in range(n):
    board.append(list(input()))
    
record = [[0 for _ in range(m)] for __ in range(n)]
max_len = 0
for i in range(m):
    if board[0][i] == '1':
        record[0][i] = 1
        max_len = 1
for j in range(n):
    if board[j][0] == '1':
        record[j][0] = 1
        max_len = 1
        
for i in range(1, n):
    for j in range(1, m):
        if board[i][j] == '0':
            record[i][j] = 0
            continue
        record[i][j] = 1
        if record[i-1][j-1] == record[i-1][j] == record[i][j-1]:
            record[i][j] = record[i-1][j-1] + 1
        else:
            record[i][j] = min(record[i-1][j-1],record[i-1][j],record[i][j-1]) + 1
    max_len = max(max_len, max(record[i]))
print(max_len*max_len)



# 시간초과로 for문을 간단하게 dp로 수정