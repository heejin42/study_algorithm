n = int(input())
dp = [[] for _ in range(n)]
dp[0] = [0, 1]
# dp[i] = [i번째가 0으로 끝나는 경우, 1로 끝나는 경우]

for i in range(1, n):
    dp[i] = [dp[i-1][0] + dp[i-1][1], dp[i-1][0]]

print(dp[-1][0] + dp[-1][1])