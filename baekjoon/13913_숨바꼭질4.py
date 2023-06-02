import heapq
import sys
input = sys.stdin.readline
n, k = map(int, input().split(' '))
queue = []
heapq.heappush(queue, [0, n])
dp = [2e9 for _ in range(100001)]
dp[n] = 0
path = [0 for _ in range(100001)]
path[n] = -1

def find_path(node):
    res = []
    while True:
        res.append(node)
        node = path[node]
        if node == -1:
            break
    res.reverse()
    print(*res)

while queue:
    time, now = heapq.heappop(queue)
    if now == k:
        print(time)
        find_path(now)
        break
    for x in [now - 1, now + 1, now * 2]:
        if 0 <= x <= 100000 and time + 1 <= dp[x]:
            heapq.heappush(queue, [time+1, x])
            dp[x] = time + 1
            path[x] = now

# case = x+1, x-1, 2*x
# heapq - (시간, 위치 입력)
# dp - 경로 저장