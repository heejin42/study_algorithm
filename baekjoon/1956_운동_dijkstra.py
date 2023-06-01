import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

v, e = map(int, input().split(' '))
graph = [[] for _ in range(v+1)]
dist = [[INF for _ in range(v+1)] for _ in range(v+1)]
heap = []
for _ in range(e):
    x, y, d = map(int, input().split(' '))
    graph[x].append([d, y])
    dist[x][y] = d
    heapq.heappush(heap,[d, x, y])
answer = -1
while heap:
    d, x, y = heapq.heappop(heap)
    if x == y:
        answer = d
        break
    for new_dist, new_node in graph[y]:
        if dist[x][new_node] > new_dist + d:
            dist[x][new_node] = new_dist + d
            heapq.heappush(heap, [dist[x][new_node], x, new_node])
    
print(answer)
