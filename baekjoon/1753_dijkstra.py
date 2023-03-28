import heapq
import sys
input = sys.stdin.readline

def dijkstra():
    global graph, V, E, k
    distance = ["INF" for _ in range(V+1)]
    distance[k] = 0
    q = []
    heapq.heappush(q, (0, k))
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue

        for node in graph[now]:
            v = node[0]
            w = node[1]
            if distance[v] == "INF":
                distance[v] = dist + w
                heapq.heappush(q, (dist + w, v))
            else:    
                if dist + w < distance[v]:
                    distance[v] = dist + w
                    heapq.heappush(q, (dist + w, v))
    for i in distance[1:]:
        print(i)


V, E = map(int, input().split(' '))
k = int(input())
graph = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split(' '))
    graph[u].append((v, w))

dijkstra()
