# 돈을 최대한 많이 지불해서 카드 n개를 사려고 한다.
# 카드 i개가 들어있는 카드팩의 가격은 pi원
# p1~pi가 주어졌을 때, 최대 금액을 구하라
n = int(input())
price = list(map(int, input().split(' ')))

dp = [0 for _ in range(n+1)]
# dp[i] = i개를 사기 위한 최대 금액
for i in range(1, n+1):
    dp[i] = price[i-1]
    
for i in range(n+1):
    for j in range(i):
        dp[i] = max(dp[i], dp[i-j]+dp[j])

print(dp[n])