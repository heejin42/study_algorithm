# 스티커를 뗴면 상하좌우는 뗄 수 없다. 
# 2n개의 스티커가 있고, 각 스티커의 점수가 있을 때, 뗄 수 있는 최대값은?

def solution(n, stickers):
    # 현재 꺼를 떼는 경우의 최대값은?
    # 사선 or 한칸 건너 or 한칸 건너 사선
    dp = [[0 for _ in range(n)] for _ in range(2)]
    dp[0][0] = stickers[0][0]
    dp[1][0] = stickers[1][0]
    if n == 1:
        return max(dp[0][0], dp[1][0])
    dp[0][1] = stickers[1][0] + stickers[0][1]
    dp[1][1] = stickers[1][1] + stickers[0][0]
    if n == 2:
        return max(dp[0][1], dp[1][1])
    
    for i in range(2, n):
        dp[0][i] = max(dp[1][i-1], dp[0][i-2], dp[1][i-2]) + stickers[0][i]
        dp[1][i] = max(dp[0][i-1], dp[0][i-2], dp[1][i-2]) + stickers[1][i]
    return max(max(dp[0][-3:]), max(dp[1][-3:]))    
    

t = 2
n = 5
stickers = [[50, 10, 100, 20, 40], [30, 50, 70, 10, 60]]
print(solution(n, stickers))