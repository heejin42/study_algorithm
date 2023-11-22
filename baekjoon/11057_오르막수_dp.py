def solution(n): 
    # 같은 수를 포함하는 오름차순 파트를 오르막이라고 한다.
    # 길이가 n인 오르막수 오르막 개수를 구하라 (10,007로 나눈 나머지 출력할 것)
    # dp[i][j] = sum(dp[i-1][:j+1])
    dp = [[0 for _ in range(11)] for _ in range(n)]
    dp[0] = [0,1,1,1,1,1,1,1,1,1,1]
    for i in range(1, n):
        for j in range(11):
            dp[i][j] = sum(dp[i-1][:j+1])
    return sum(dp[-1])%10007

n = 3
print(solution(n))