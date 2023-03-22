import sys
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

def dfs(cx, cy):
    if dp[cx][cy] != -1:
        return dp[cx][cy]

    cnt = 0
    for i in range(4):
        nx = cx + dx[i]
        ny = cy + dy[i]
        
        if not 0 <= nx < n or not 0 <= ny < m:
            continue
        if map[nx][ny] >= map[cx][cy]:
            continue
        cnt += dfs(nx, ny)

    dp[cx][cy] = cnt
    return dp[cx][cy]



n, m = map(int, input().split(' '))
dp = [[-1 for _ in range(m)] for _ in range(n)]
map = [list(map(int, input().split())) for _ in range(n)]
dp[-1][-1] = 1
print(dfs(0,0))