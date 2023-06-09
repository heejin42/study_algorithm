from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
bus = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split(' '))
    bus[a].append([a, b, c])
    
start, end = map(int, input().split(' '))
graph = [[] for _ in range(n+1)]
cost = [2e9 for _ in range(n+1)]
cost[start] = 0
queue = deque([start])
while queue:
    now = queue.popleft()
    for a,b,c in bus[now]:
        if cost[b] > cost[a] + c:
            cost[b] = cost[a] + c
            graph[b] = graph[a] + [a]
            queue.append(b)
            bus[now].remove([a,b,c])

graph[end].append(end)

print(cost[end])
print(len(graph[end]))
print(*graph[end])
            
    