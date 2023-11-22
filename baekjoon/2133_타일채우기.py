# 3xN 크기의 벽을 2x1, 1x2 크기의 타일로 채우는 경우의 수를 구하자
def solution(n):
    dp = [0]*(n+1)
    dp[0] = 1

    if n  >= 2:
        dp[2] = 3

    for i in range(4,n+1,2):
        dp[i] = dp[i-2] *dp[2]
        for j in range(0,i-2, 2):
            dp[i] += dp[j]*2
    return dp[n]

n = 2
print(solution(n))