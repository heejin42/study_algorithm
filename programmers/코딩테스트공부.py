# 코딩 테스트 문제마다 일정 이상의 알고력과 코딩력을 요구함.
# 각각 1을 높이기 위해서는 1의 시간이 필요함.
# 문제마다 소요 시간이 필요, 풀었을 때 알고력과 코딩력이 올라간다. 중복 풀이 가능
# 모든 문제를 풀 수 있는 알고력과 코딩력을 얻는 최단 시간은?
# [alp_req, cop_req, alp_rwd, cop_rwd, cost]
    # dp로 풀 수 있을까?                 
    # dp[i][j] = 알고력이 i가 되고, 코딩력이 j가 되는 시간
    # alp_req <= i, cop_req <= j 인 아이들 중 dp[i-alp_rwd][j-cop_rwd]_cost]
    # dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1)
def solution(alp, cop, problems):
    max_alp = 0
    max_cop = 0
    time = 0
    for a,b,c,d,e in problems:
        max_alp = max(max_alp,a)
        max_cop = max(max_cop,b)
        time += e
    # 목표 알고력
    alp = min(alp, max_alp)
    cop = min(cop, max_cop)
    INF = float('inf')
    dp = [[INF]*(max_cop + 1) for _ in range(max_alp + 1)]
    dp[alp][cop] = 0
    
    for i in range(alp, max_alp + 1):
        for j in range(cop, max_cop + 1):
            if i + 1 <= max_alp:
                dp[i + 1][j    ] = min (dp[i + 1][j    ],dp[i][j] + 1)
            if j + 1 <= max_cop:
                dp[i    ][j + 1] = min (dp[i    ][j + 1],dp[i][j] + 1)

            for alp_req,cop_req,alp_rwd,cop_rwd,cost in problems:
                if i >= alp_req and j >= cop_req:
                    next_alp,next_cop = min(max_alp,i + alp_rwd), min(max_cop,j + cop_rwd)
                    dp[next_alp][next_cop] = min(dp[next_alp][next_cop],dp[i][j] + cost)
    return dp[-1][-1] 

alp = 10
cop = 10
problems = [[10,15,2,1,2],[20,20,3,3,4]]
print(solution(alp, cop, problems))