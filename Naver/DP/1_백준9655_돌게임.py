# 돌게임은 번갈아가며 1개 또는 3개 가져가는 게임
# 돌을 가져가는 경우의 수는?
# 상근 1 창영 1 , 상근 1 창영 3 , 상근 3 창영 1 , 상근 3 창영 3
# dp[1] = SK
# dp[2] = CY | dp[3] = SK | dp[4] = CY | dp[5] = SK | dp[6] = CY | dp[7] = SK | dp[8] = CY
# dp[2] = CY | dp[3] = SK | dp[4] = CY | dp[5] = SK | dp[6] = SK | dp[7] = SK | dp[8] = CY
# dp[2] = CY | dp[3] = SK | dp[4] = CY | dp[5] = CY | dp[6] = CY | dp[7] = SK | dp[8] = CY
# dp[2] = CY | dp[3] = SK | dp[4] = CY | dp[5] = CY | dp[6] = CY | dp[7] = SK | dp[8] = SK | dp[9] = SK
# dp[2] = CY | dp[3] = SK | dp[4] = SK | dp[5] = SK
# dp[2] = CY | dp[3] = CY | dp[4] = CY | dp[5] = SK
# dp[2] = SK | dp[3] = SK | dp[4] = SK | dp[5] = CY
# dp[2] = SK | dp[3] = SK | dp[4] = SK | dp[5] = CY | dp[6] = CY | dp[7] = CY
# dp[n]
# if dp[n-1][1] == 1:
    # SK, CY 모두 가능
    # [dp[n-1][0], 2]
    # [dp[n-1][0] 아닌 것, 1]
# if dp[n-1][1] == 2:
#     dp[n-1][0], 3
# if dp[n-1][1] == 3:
#     dp[n-1][0] 아닌 것, 1]
n = int(input())

win = [-1]*10001

win[1] = 1 #SK
win[2] = 0 #CY
win[3] = 1 #SK

for i in range(4,n+1):
    if win[i-1] == 1 or win[i-3] == 1:
        win[i] = 0
    else:
        win[i] = 1

if win[n]==1:
    print('SK')
else:
    print('CY')