n = int(input())
trees = []
visited = [[False for _ in range(n)] for _ in range(n)]
result = 0

for _ in range(n):
    trees.append(list(map(int, input().split())))

def dfs(x, y, depth, total_sum):
    global result, visited
    visited[x][y] = True

    for mx, my in [[-1,0], [1,0], [0,-1], [0,1]]:
        dx, dy = mx+x, my+y

        if 0<=dx<n and 0<=dy<n and not visited[dx][dy]:
            visited[dx][dy] = True
            total_sum_temp = total_sum + trees[x][y] + trees[dx][dy]

            if depth==3 or (n<3 and depth==1) :
                result = max(total_sum_temp, result)
                visited[dx][dy] = False
                return

            for i in range(n):
                for j in range(n):
                    if not visited[i][j] :
                        dfs(i, j, depth+1, total_sum_temp)
                        visited[i][j] = False
            visited[dx][dy] = False

for i in range(n):
    for j in range(n):
        dfs(i, j, 0, 0)
        visited[i][j] = False

print(result)