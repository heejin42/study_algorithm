import math

def dfs(route, dp):
    global cost_board
    global n
    print(route, dp)
    if len(route) == n:
        if cost_board[route[-1]][0] > 0:
            if dp[0] == 0:
                dp[0] = dp[route[-1]] + cost_board[route[-1]][0]
            else:
                dp[0] = min(dp[0], dp[route[-1]] + cost_board[route[-1]][0])
        return
    for i in range(1, n):
        if i not in route and cost_board[route[-1]][i] > 0:
            dp[i] = min(dp[i], dp[route[-1]] + cost_board[route[-1]][i])
            route.append(i)
            dfs(route, dp)
            route.pop()

n = int(input()) 
cost_board = []
for _ in range(n):
    cost_board.append(list(map(int, input().split(' '))))

dp = [math.inf for _ in range(n)]
dp[0] = 0
route = [0]
dfs(route, dp)
print(dp[0])

# 최소 비용 거리 구할 때 -> bfs / 그러나 간선의 가중치가 다르므로 모든 경우를 탐색하는 dfs
# 0에서 출발, dfs로 확인

