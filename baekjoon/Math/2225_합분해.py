# 0부터 N까지의 정수 K개를 더해서 합이 N이 되는 경우의 수를 구하라
# 한개의 수를 여러번 쓸 수 있고, 순서가 다르면 다른 경우로 센다.
# 답은 1,000,000,000으로 나눈 나머지를 출력할 것


# def dfs(added, k, answer):
#     # 0부터 N까지의 정수 중 k개를 고르는 방법의 수, 
#     if k == 0 and added == n:
#         answer += 1
#         return answer
#     if k < 0 or added > n:
#         return answer
#     for i in range(n+1):
#         answer = dfs(added+i, k-1, answer)
#     return answer
    
# n, k = map(int, input().split(' '))
# answer = dfs(0, k, 0)
# print(answer%1000000000)

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
dp = [[0] * 201 for _ in range(201)]

for i in range(201) :
	dp[1][i] = 1
	dp[2][i] = i + 1

for i in range(2, 201) :
	dp[i][1] = i
	for j in range(2, 201) :
		dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1000000000

print(dp[k][n])