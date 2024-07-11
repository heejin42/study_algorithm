import sys
from collections import deque

def solution(n, cost, prepare):
    answer = [0 for _ in range(n+1)]
    queue = deque([i for i in range(n+1)])
    while queue:
        x = queue.popleft()
        now_cost = cost[x]
        for i in prepare[x]:
            if answer[i] == 0:
                queue.append(x)
                now_cost = -1
                break
            else:
                now_cost += answer[i]
        if now_cost == -1:
            continue
        answer[x] = now_cost
    print(answer[1:], sep='\n')

n = int(input())
cost = [0]
prepare = [[]]
for _ in range(n):
    line = list(map(int, sys.stdin.readline().strip().split(' ')))
    cost.append(line[0])
    prepare.append(line[1:-1])
solution(n, cost, prepare)