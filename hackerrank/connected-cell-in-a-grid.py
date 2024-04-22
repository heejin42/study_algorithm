from collections import deque
def connectedCell(matrix):
    n = len(matrix[0])
    m = len(matrix)
    q = deque([])
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    
    for y in range(m):
        for x in range(n):
            if matrix[y][x] != 1:
                continue
            q.append([x,y])
            cnt = 0
            while q:
                x, y = q.popleft()
                for i in range(4):
                    if 0 <= y + dy[i] < m and 0 <= x + dx[i] < n and matrix[y + dy[i]][x+dx[i]] == 1:
                       cnt += 1
                       matrix[y+dy[i]][x+dx[i]] = cnt
                       q.append([x+dx[i], y+dy[i]])
    result = 1
    for line in matrix:
        result = max(result, max(line))
    return result
    
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    