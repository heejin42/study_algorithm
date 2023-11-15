# 가로길이 n, 세로길이 3 판 타일링하는 방법
# 타일 종류는 두 종류
# 1 1  1 1 1  1
# 1 1  1 1 1  1
# 1 1         1

def solution(n):
    dp = [0 for i in range(100000)]
    dp[1] = 1
    dp[2] = 3
    dp[3] = 10
    if n <= 3:
        return dp[n]%1000000007
    for i in range(4, n+1):
        dp[i] = dp[i-3]*dp[3] + dp[i-2]*dp[2] + dp[i-1]
    return dp[n]%1000000007

n = 3
print(solution(n))