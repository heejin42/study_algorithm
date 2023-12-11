# 2xn 타일을 1x2, 2x1, 2x2 타일로 채우는 방법의 수를 구하라
# n에 따른 패턴 찾기
# n=1 = 1
# n=2 = 3
# n=3 = 5
# n=4 = 11   4 + 3 + 1
# n=5 = 21  8 + 12 + 1
# n=6 = 43  21 + 24 + 4 + 1
# dp[n] = 2*dp[n-1] + dp[n-2]


def solution(n):
    if n == 1:
        return 1
    if n == 2:
        return 3
    dp = [0 for _ in range(n+1)]
    dp[1] = 1
    dp[2] = 3
    for i in range(3, n+1):
        dp[i] = 2*dp[i-2]+dp[i-1]
    return dp[n]%10007
n = int(input())
print(solution(n))
 
 