# 정수 N이 주어졌을 때, n을 1,2,3의 합으로 나타내는 방법의 수를 구하여라.

def solution(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4 
    dp = [0 for _ in range(n+1)]
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4 
    for i in range(4, n+1):
        dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
    return dp[n]

t = int(input())
for _ in range(t):
    n = int(input())
    print(solution(n))