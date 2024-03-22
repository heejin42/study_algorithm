def dfs(x, y):
    global n
    global field
    global dp
    if dp[y][x] != 0:
        return dp[y][x]
    dp[y][x] = 1
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    for i in range(4):
        if 0 <= x+dx[i] < n and 0 <= y+dy[i] < n:
            if field[y+dy[i]][x+dx[i]] > field[y][x]:
                dp[y+dy[i]][x+dx[i]] = dp[y][x]+1
                dp[y][x] = max(dfs(x+dx[i], y+dy[i])+1, dp[y][x])
    return dp[y][x]
            
        
n = int(input())
field = []
for _ in range(n):
    field.append(list(map(int, input().split(' '))))    

dp = [[0 for _ in range(n)] for _ in range(n)]
result = 0
for y in range(n):
    for x in range(n):
        result = max(result, dfs(x, y))
print(result)