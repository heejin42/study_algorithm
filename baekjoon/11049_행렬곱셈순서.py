# 행렬의 곱셈
# N x M 인 행렬A, M x K 인 행렬B의 곱셈 연산 수는 N*M*K, 결과는 N x K 크기
# 행렬을 곱하는 순서에 따라 달라진다.
# 행렬 곱의 순서에 따라 연산의 수가 달라진다. 
# 행렬의 개수 N가 주어지고, 행렬의 각각의 크기가 주어졌을 때, 연산의 최솟값을 출력할 것
import sys
def solution(n, metrix):
    dp = [[0]*n for i in range(n)]
    for cnt in range(n-1):
        for i in range(n-1-cnt):
            j = i+cnt+1
            dp[i][j] = 2**31
            for k in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + mat[i][0]*mat[k][1]*mat[j][1])
    return dp[0][-1]
    
    # 해당 행렬까지 처리하는 연산 수는? dp[i][j] = i번째부터 j번째까지 처리하는 횟수
    # dp[i][j] = min(dp[i][j], dp[i][x] + dp[x][j] + graph[i][x][0]*graph[i][x][1]*graph[x][j][1])
    # graph[i][j] = [graph[i][x][0], graph[x][j][1]]
    
n = 3
metrix = [[5,3],[3,2],[2,6]]
print(solution(n, metrix))
