import sys

def solution(n, graph):
    yet_dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
    done_dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
    yet_dp[1][1] = graph[0][0]
    done_dp[1][1] = graph[0][0]*2
    # dp[i][j] = dp[i-1][j] or dp[i][j-1] + 현재
    # 순서는 1행, 1열, 2행, 2열 ...
    for r in range(1, n+1):
        for c in range(1, n+1):# 행
            yet_dp[r][c] = max(yet_dp[r-1][c], yet_dp[r][c-1]) + graph[r-1][c-1]
            done_dp[r][c] = max(max(done_dp[r-1][c], done_dp[r][c-1]) + graph[r-1][c-1], max(yet_dp[r-1][c], yet_dp[r][c-1]) + (graph[r-1][c-1]*2))
    return done_dp[n][n]

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().strip().split(' '))))
                 
print(solution(n, graph))