import sys

def solution(n, records):
    dp = [[0, 0] for _ in range(n)]
    dp[0] = records[0][0:2]
    for i in range(1, n):
        dp[i][0] = min(dp[i-1][0], dp[i-1][1]+records[i-1][3]) + records[i][0]
        dp[i][1] = min(dp[i-1][1], dp[i-1][0]+records[i-1][2]) + records[i][1]
    return min(dp[-1])

n = int(input())
records = []
for _ in range(n):
    records.append(list(map(int, sys.stdin.readline().strip().split(' '))))

print(solution(n, records)) 
                   