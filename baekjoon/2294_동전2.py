def solution(n,k,coins):
    # n가지 종류의 동전이 coins로 주어질 때, 합이 k가 되게 하는 최소 개수를 출력하라.
    # 불가능한 경우에는 -1
    dp = [10001 for _ in range(k+1)]
    dp[0] = 0
    for i in range(k+1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i-coin]+1) 
    if dp[k] == 10001:
        return -1
    else:
        return dp[k]


n = 3
k = 15
coins = [1,5,12] 
print(solution(n,k,coins))