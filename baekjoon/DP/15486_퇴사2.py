# 남은 n일 동안 최대한 많은 상담을 할 때 최대 수익을 구하라
# 각 일수마다 잡혀있는 상담이 있고, 걸리는 시간과 금액이 배열로 주어진다.
import sys
n = int(input())
price_dp = [0 for _ in range(n+1)]
for i in range(1, n+1):
    t, p = map(int, sys.stdin.readline().split())
    price_dp[i] = max(price_dp[i-1], price_dp[i])
    if i+t-1 <= n:
        price_dp[i+t-1] = max(price_dp[i+t-1], price_dp[i-1] + p)
print(price_dp[-1])

# 1일차 = 1일 상담을 한다. end_date[0] = t, dp[0] = p
# 2일차 = ~1일까지 끝난 경우 최대 이익 + 오늘의 상담
# 3일차 = ~2일까지 끝난 경우 최대의 이익 + 오늘의 상담
# price_dp = [0 for _ in range(n+2)]
# for i in range(1, n+1):
#     if i + times[i-1] <= n+1:
#         x = max(price_dp[:i+1]) + prices[i-1]
#         price_dp[i + times[i-1]] = max(price_dp[i + times[i-1]], x)
# print(max(price_dp))