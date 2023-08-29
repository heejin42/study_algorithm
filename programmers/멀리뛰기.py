def solution(n):
    # 맨 끝 칸에 도달해야 한다.
    # 1칸 or 2칸 뛸 수 있음.
    # 1~n이 있을 때, n-1 번째에 도착하는 경우 + n-2번째에 도착하는 경우
    # dp[n] = dp[n-1] + d[n-2]
    if n < 3:
        return n
    dp = [0 for _ in range(n+1)]
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    answer = dp[n]%1234567
    return answer

n = 4
print(solution(n))