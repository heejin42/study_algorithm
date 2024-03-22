def solution(n, tops):
    if tops[0] == 0:
        dp = [2,1]
    else:
        dp = [3,1]

    # 0인 경우 -> 2개
    # 1인 경우 -> 3개
    for i in range(1, n-1):
        if tops[i] == 0:
            new_dp = [dp[0]*2+dp[1], dp[0]+dp[1]]
        else:
            new_dp = [dp[0]*3+dp[1]*2, dp[0]+dp[1]]
        dp = new_dp
        
    if tops[n-1] == 0:
        answer = dp[0]*3+dp[1]*2
    else:
        answer = dp[0]*4+dp[1]*3

    answer = answer % 10007
    return answer