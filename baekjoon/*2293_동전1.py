import sys
input = sys.stdin.readline

def solution(coins, k):
    dp = [0 for _ in range(k+1)]
    dp[0] = 1
    # dp[i] = dp[i-coin] + 1 + dp[i-coin] + 1
    for coin in coins:
        for i in range(coin, k+1):
            dp[i] += dp[i-coin]
    return dp[k]
    
    
    

n, k = map(int, input().strip().split(' '))
coins = []
for _ in range(n):
    coins.append(int(input().strip()))
coins.sort()
print(solution(coins, k))