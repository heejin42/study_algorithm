import sys
from collections import deque

def solution(n, cost, prepare):
    q = deque([i for i in range(1, n+1)])
    dp = [0 for _ in range(n+1)]
    
    while q:
        flag = 1
        i = q.popleft()
        needed = 0
        for pre in prepare[i]:
            if dp[pre] == 0:
                q.append(i)
                flag = 0
                break
            needed = max(dp[pre], needed)
        if flag:
            needed += cost[i]
            dp[i] = needed
    print(*dp[1:], sep='\n')

n = int(input())
cost = [0]
prepare = [[]]
for _ in range(n):
    line = list(map(int, sys.stdin.readline().strip().split(' ')))
    cost.append(line[0])
    prepare.append(line[1:-1])
solution(n, cost, prepare)