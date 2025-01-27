import math
import copy
n, m = map(int, input().split(' '))
memories = list(map(int, input().split(' ')))
costs = list(map(int, input().split(' ')))
answer = math.inf
# 총 memories 일부의 합 m이 필요, costs를 제일 작게!
# 1 <= n <= 100
# 조합은 너무 오래 걸림, 경우에 따라 memories 합과 costs 합 필요
# 1개 -> 선택의 경우 n, memories 
# 2개 -> 선택의 경우 n * n
# 3개 -> 2개 고른 경우 * n
# 4개 -> 3개 고른 경우 * n
# 모든 경우의 수 중에, m 이상의 경우 최저 cost 구하기 ->
# m 이상의 경우 cost 기록, 이미 m 이상인 경우 계산 x

get_dp = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    get_dp[i][i] = 1
m_dp = [i for i in memories]
c_dp = [i for i in costs]

while m_dp:
    new_m_dp = []
    new_c_dp = []
    new_get_dp = []
    for i in range(len(m_dp)):
        if m_dp[i] >= m:
            answer = min(answer, c_dp[i])
            continue
        for j in range(n): 
            if get_dp[i][j] == 1:
                continue
            new_m_dp.append(m_dp[i]+memories[j])
            new_c_dp.append(c_dp[i]+costs[j])
            new_get_dp.append(list(get_dp[i]))
            new_get_dp[-1][j] = 1
    m_dp = copy.copy(new_m_dp)
    c_dp = copy.copy(new_c_dp)
    get_dp = copy.deepcopy(new_get_dp)
            
print(answer)