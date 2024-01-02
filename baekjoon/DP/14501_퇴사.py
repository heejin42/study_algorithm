# 오늘부터 n일동안 일해서 최대 수익을 얻을 수 있는 방법은?
# 하루에 한 사람씩, t(걸리는 날짜)와 p(금액)

n = int(input())

schedule = []

for _ in range(n):
    schedule.append(list(map(int, input().split())))

dp = [0] * (n+1)

for i in range(n-1, -1, -1): #큰 것부터 찾는다.(상담 일수가 넘어가면 안됨)
    if i + schedule[i][0] > n:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(schedule[i][1] + dp[i+schedule[i][0]], dp[i+1])

# print(dp)
print(dp[0])