# 2xn 크기의 직사각형을 1x2, 2x1 타일로 채우는 방법의 수를 구하여라.
# dp[i] = dp[i-2] + dp[i-1]
def solution(n):
    dp = [0 for i in range(n)]
    dp[0], dp[1] = 1, 2
    for i in range(2, n):
        dp[i] = (dp[i-1] + dp[i-2]) % 1000000007

    return dp[n-1]