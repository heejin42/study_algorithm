from collections import deque
import sys

def check_ghost(x, y, d):
    for g_x, g_y in ghost:
        if d >= abs(g_x-x) + abs(g_y-y):
            return False
    return True
        

def solution(maze, start):
    q = deque([(start[0], start[1], 0)])
    maze[start[1]][start[0]] = 0
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    while q:
        x, y, d = q.popleft()
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]
            if 0 <= next_x < m and 0 <= next_y < n:
                if maze[next_y][next_x] == 'D':
                    return "Yes"
                if maze[next_y][next_x] == '.' or (type(maze[next_y][next_x]) == int and maze[next_y][next_x] > d+1):
                    if check_ghost(next_x, next_y, d+1):
                        q.append((next_x, next_y, d+1))
                        maze[next_y][next_x] = d+1
                        
                    
    return "No"


n, m = map(sys.stdin.readline().strip(), input().split(' '))
maze = []
global ghost 
ghost = []
for i in range(n):
    line = list(sys.stdin.readline().strip())
    if 'N' in line:
        start = (line.index('N'), i)
    for _ in range(line.count('G')):
        x = line.index('G')
        ghost.append((x, i))
        line[x] = '.'
    maze.append(line)
print(solution(maze, start))
