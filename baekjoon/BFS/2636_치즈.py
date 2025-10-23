import sys 
from collections import deque
import heapq

def solution(board):
    h = len(board)
    w = len(board[0])
    visited = [[0 for _ in range(w)] for _ in range(h)]
    heap = []
    for i in range(w):
        heap.append((0, 0, i))
        heap.append((0, h-1, i))
        visited[0][i] = 1
        visited[h-1][i] = 1
    for i in range(h):
        heap.append((0, i, 0))
        heap.append((0, i, w-1))
        visited[i][0] = 1
        visited[i][w-1] = 1    
    heapq.heapify(heap)
    max_t = 0
    count = 0
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    while heap:
        t, y, x = heapq.heappop(heap)
        for i in range(4):
            next_y = y + dy[i]
            next_x = x + dx[i]
            if 0 <= next_y < h and 0 <= next_x < w and visited[next_y][next_x] == 0:
                if board[next_y][next_x] == 0:
                    heapq.heappush(heap, (t, next_y, next_x))
                else:
                    heapq.heappush(heap, (t+1, next_y, next_x))
                    if t+1 > max_t:
                        max_t = t+1
                        count = 1
                    elif t+1 == max_t:
                        count += 1
                visited[next_y][next_x] = 1
    if max_t == 0:
        count = 0
    return max_t, count
        

h, w = map(int, sys.stdin.readline().split(' '))
board = []
for _ in range(h):
    board.append(list(map(int, sys.stdin.readline().split(' '))))

print(*solution(board), sep= '\n')