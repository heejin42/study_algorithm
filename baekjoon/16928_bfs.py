from collections import deque
import sys
input = sys.stdin.readline

def solve():
    global board, visited
    visited[1] = True
    queue = deque([1])
    while queue:
        x = queue.popleft()
        for i in range(1, 7):
            if visited[x + i] == False:
                if board[x + i] == 0:
                    board[x+i] = board[x] + 1
                    visited[x+i] = True
                    if x+i == 100:
                        return board[100] 
                    queue.append(x+i)
                else:
                    next = board[x+i]
                    if visited[next] == False:
                        board[next] = board[x] + 1
                        visited[next] = True
                        queue.append(next)

n, m = map(int, input().split(' '))
board = [0] * 101
visited = [False] * 101
for _ in range(n):
    x, y = map(int, input().split(' '))
    board[x] = y
for _ in range(m):
    x, y = map(int, input().split(' '))
    board[x] = y

print(solve())
