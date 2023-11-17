# 게임이 끝날 때까지 몇번 움직이는지 구하는 문제
# 밟았던 발판은 사라지며, 상하좌우로 인접한 칸 중 발판이 있는 칸으로 갈 수 있다.
# 이동할 발판이 없거나, 두 캐릭터가 같은 발판 뒤에 있다가 상대방이 이동하면 패배
# A부터 시작하며 매번 최적의 플레이를 한다. 
#  이기는 사람은 최단경로로 이기려 하고, 지는 사람은 최대경로로 지려고 한다.
# 재귀를 돌때 만약 이길 수 있다면, 최단경로를 리턴해주고 만약 진다면 최대경로를 리턴해준다.
dir = ((-1,0),(0,1),(1,0),(0,-1))

def A_turn(ar,ac,br,bc,cnt,board):
    if board[ar][ac] == 0:
        return (1,cnt)
    winner = []
    loser = []
    flag = False
    for dr,dc in dir:
        nr,nc = ar+dr,ac+dc
        if 0<=nr<len(board) and 0<=nc<len(board[0]) and board[nr][nc] == 1:
            flag = True
            temp = [row[:] for row in board]
            temp[ar][ac] = 0
            iswin,turn = B_turn(br,bc,nr,nc,cnt+1,temp)
            if iswin:
                winner.append(turn)
            else:
                loser.append(turn)
    if flag:
        if winner:
            return (0,min(winner))
        else:
            return (1,max(loser))
    else:
        return (1,cnt)


def B_turn(br,bc,ar,ac,cnt,board):
    if board[br][bc] == 0:
        return (1,cnt)
    winner = []
    loser = []
    flag = False
    for dr,dc in dir:
        nr,nc = br+dr,bc+dc
        if 0<=nr<len(board) and 0<=nc<len(board[0]) and board[nr][nc] == 1:
            flag = True
            temp = [row[:] for row in board]
            temp[br][bc] = 0
            iswin,turn = A_turn(ar,ac,nr,nc,cnt+1,temp)
            if iswin:
                winner.append(turn)
            else:
                loser.append(turn)
    if flag:
        if winner:
            return (0,min(winner))
        else:
            return (1,max(loser))
    else:
        return (1,cnt)


def solution(board, aloc, bloc):
    ar,ac,br,bc = aloc[0],aloc[1],bloc[0],bloc[1]
    answer = A_turn(ar,ac,br,bc,0,board)[1]
    return answer

board = [[1, 1, 1, 1, 1]]
aloc = [0, 0]
bloc = [0, 4]
print(solution(board, aloc, bloc))