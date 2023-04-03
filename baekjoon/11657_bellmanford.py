import sys
from  collections import deque
input = sys.stdin.readline
inf = sys.maxsize

def solve():
    global n, m, buses, inf
    start = 1
    queue = deque([start])
    dp = [0]* (n+1)
    times = [inf] * (n+1)
    times[start] = 0
    while queue:
        now = queue.popleft()
        for bus in buses[now]:
            next = bus[0]
            delay = bus[1]
            if times[next] > times[now] + delay:
                times[next] = times[now] + delay
                queue.append(next)
                if delay < 0:
                    dp[next] += 1
                if dp[next] == n+1:
                    print(-1)
                    return
    for time in times[2:]:
        if time == inf:
            print(-1)
        else:
            print(time)
    return


    
n, m = map(int, input().split(' '))
buses = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split(' '))
    buses[a].append([b, c])

solve()