def solution(n):
    # n번째 피보나치수를 구해서 1234567로 나눈 나머지를 리턴
    dp = [0 for _ in range(n+1)]
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
            
    answer = dp[n] % 1234567
    return answer

n = 5
print(solution(n))