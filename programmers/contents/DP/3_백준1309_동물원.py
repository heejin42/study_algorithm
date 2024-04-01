# 2 X N 크기의 우리가 있다. 사자를 배치하는 경우의 수를 9901로 나눈 나머지를 출력하라.
n = int(input())
dp = [0 for _ in range(n)]
dp[0] = 3
dp[1] = 7
for i in range(2, n):
    dp[i] = (2*dp[i-1] + dp[i-2])%9901
print(dp[n-1])