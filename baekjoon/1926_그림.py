from collections import deque
n, m = map(int, input().split(' '))
paper = []
for _ in range(n):
    paper.append(list(map(int, input().split(' '))))

paintings = []

def bfs(i, j):
    visited[i][j] = 1
    q = deque([(i, j)])
    size = 0
    while q:
        i, j = q.popleft()
        size += 1
        di = [0, -1, 0, 1]
        dj = [1, 0, -1, 0]
        for x in range(4):
            new_i = i + di[x]
            new_j = j + dj[x]
            if 0 <= new_i < n and 0 <= new_j < m and paper[new_i][new_j] == 1 and visited[new_i][new_j] == 0:
                q.append((new_i, new_j))
                visited[new_i][new_j] = 1
    return size
        
paintings = [0]
visited = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        if paper[i][j] == 1 and visited[i][j] == 0:
            paintings.append(bfs(i, j))

print(len(paintings)-1)
print(max(paintings))