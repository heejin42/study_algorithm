def solution(n, money):
    # money 단위의 화폐가 있을 때, n을 만들 수 있는 경우의 수
    # n = 100,000 이하의 자연수, money = 100 종류 이하
    # 1,000,000,007로 나눈 나머지 리턴
    
    # 중복 조합은 경우의 수가 너무 많을 것 같고, 중첩 for문으로 모든 경우를 체크하는 것도 시간복잡도가 어마어마해진다.
    # 그렇다면? dp를 이용해볼까...? 순서 관계가 없다는 것이 중요!
    # 1, 2, 5 동전으로 10을 만드는 경우의 수는?
    #       1   2   3   4   5   6   7   8   9   10
    #   1   1   1   1   1   1   1   1   1   1    1
    #   2   0   1   1   2   2   3   3   4   4    5
    #   5   0   0   0   0   1   1   2   2   3    4
    # total 1   2   2   3   4   5   6   7   8    10
    # price in range(n), coin in money 일 때, dp[price] == dp[price-coin]이다. 
    
    answer = 0
    dp = [0 for _ in range(n+1)]
    dp[0] = 1
    for coin in money:
        for price in range(coin, n+1):
            dp[price] += dp[price-coin]
    return dp[n]%1000000007

n = 5
money = [1,2,5]
print(solution(n, money))