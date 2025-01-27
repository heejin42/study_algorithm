# T초 동안 두 나무 중 하나에서 떨어진다.
# w 이하로 움직여 얻을 수 있는 최대 자두 개수는?
# 시작은 1번
t, w = map(int, input().split(' '))
trees = []
for _ in range(t):
    trees.append(int(input()))
dp = [[(0,0), (0,0)] for _ in range(t)]
if trees[0] == 1:
    dp[0] = [(1, w), (0, w-1)]
else:
    dp[0] = [(0, w), (1, w-1)]

for i in range(1, t):
    count_1, w_1 = dp[i-1][0]
    count_2, w_2 = dp[i-1][1]
    # dp[i][0] -> dp[i-1][0], dp[i-1][1]에
    # dp[i][1]
    if trees[i] == 1: # 1번 나무에 있는 경우
        dp[i][0] = (count_1+1, w_1), (count_2+1, w_2-1)
        dp[i][1] = (count_2, w_2), (count_1, w_1-1)
        