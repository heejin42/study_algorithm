import sys
import heapq
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

n, m = map(int, input().split(' '))
answer = [] # 정답(풀이 과정)을 기록할 리스트 
degrees = [0 for _ in range(n+1)] # 차수를 기록할 리스트
direct = {} # 방향을 기록할 딕셔너리

for _ in range(m):
    a, b = map(int, input().split(' '))
    degrees[b] += 1
    if a in direct:
        direct[a].append(b
    else:
        direct[a] = [b]

queue = [x for x in range(1, n+1) if degrees[x] == 0]
queue.sort()
while queue:
    x = heapq.heappop(queue)
    answer.append(x)
    if x in direct:
        for i in direct[x]:
            degrees[i] -= 1
            if degrees[i] == 0:
                heapq.heappush(queue, i)
print(*answer)