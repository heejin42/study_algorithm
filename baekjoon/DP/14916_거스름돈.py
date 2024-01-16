# 2원짜리와 5원짜리 거스름돈이 있다. 동전 개수 최소를 구해라
n = int(input())
if n < 6:
    if n == 2 or n == 5:
        print(1)
    if n == 4:
        print(2)
    print(-1)

dp = [n for _ in range(n+1)]
dp[2] = 1
dp[4] = 2
dp[5] = 1
for i in range(6, n+1):
    dp[i] = min(dp[i], dp[i-2] + 1, dp[i-5] + 1)
if dp[n] == n:
    print(-1)
else:
    print(dp[n])