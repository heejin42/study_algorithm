def solution(sequence):
    # 연속 펄스? 1 -1 1 -1 / -1 1 -1 1
    # dp 문제일 것 같은데..? 
    # 각 위치마다 -1일때의 최대, 1일때의 최대를 기록하자
    # dp[2] = max(dp[2], -dp[2], -dp[1]+dp[2], dp[1]-dp[2])
    dp = [[] for _ in range(len(sequence))]
    dp[0] = [-(sequence[0]), sequence[0]]
    answer = max(sequence[0], -(sequence[0]))
    for i in range(1, len(sequence)):
        num1 = max(-(sequence[i]), dp[i-1][1]-sequence[i])
        num2 = max(sequence[i], dp[i-1][0]+sequence[i])
        dp[i] = [num1, num2]
        answer = max(answer, num1, num2)
    return answer

sequence = [2, 3, -6, 1, 3, -1, 2, 4]
print(solution(sequence))