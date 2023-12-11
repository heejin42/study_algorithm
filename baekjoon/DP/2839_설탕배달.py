# N 킬로그램의 설탕을 배달하는 방법 중, 더 적은 수의 봉지를 구하라.
# 3킬로그램 혹은 5킬로그램으로 가능하다.
# dp[n] = dp[n-3] + 1 or dp[n-5] + 1

def solution(n):
    if n <= 5:
        if n == 3 or n == 5:
            return 1
        else:
            return -1
        
    dp = [0 for _ in range(n+1)]
    dp[3] = 1
    dp[5] = 1
    for i in range(6, n+1):
        if dp[i-3] == 0 and dp[i-5] == 0:
            continue
        elif dp[i-3] != 0 and dp[i-5] == 0:
            dp[i] = dp[i-3] + 1
        elif dp[i-3] == 0 and dp[i-5] != 0:
            dp[i] = dp[i-5] + 1
        else:       
            dp[i] = min(dp[i-3], dp[i-5]) + 1
    if dp[n] == 0:    
        return -1
    else:
        return dp[n]
    
n = int(input())
print(solution(n))