# 다익스트라(Dijkstra) 알고리즘이란?
다익스트라 알고리즘은 그래프 상에서 시작 정점부터 나머지 각 정점까지의 최단 거리를 구하는 알고리즘이다.
그래프에는 간선마다 가중치가 있으며, 음수는 될 수 없다. (벨만-포드 알고리즘은 음수도 가능)

### 구현 방법
graph 자료 구조와 우선순위 큐를 사용하며, 아래 과정을 반복함으로써 다익스트라 알고리즘을 구현할 수 있다.
1. 방문하지 않은 정점 중 가장 가중치 값이 작은 정점을 방문한다. (처음엔 시작 정점)
2. 해당 정점을 거쳐서 갈 수 있는 정점의 거리가 이전의 기록보다 작으면 그 거리를 갱신한다.

### 코드 구현
- 출발 노드, 도착 노드 설정 (전체 거리를 알고 싶을 때는, 출발 노드만 설정 하여도 무방)
- 알고 있는 모든 거리 값을 부여 (Python에서는 dictionary 객체를 이용하여 graph를 표현)
```python
graph = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
}
```
출발 노드부터 시작해 방문하지 않은 인접 노드를 방문하는데, 
거리를 계산한 다음 현재 알고있는 거리보다 짧으면 해당 값으로 갱신한다.
현재 노드에 인접한 모든 방문 노드까지의 거리를 계산했다면 현재 노드를 미방문 집합에서 제거한다.

(예제)
```python
n, m = map(int, input().split())
k = int(input())                 # 시작할 노드
INF = 1e8

graph = [[] for _ in range(n+1)] # 1번 노드부터 시작하므로 하나더 추가

distance = [INF] * (n+1)

for _ in range(m):
  u, v, w = map(int, input().split()) # u: 출발노드, v: 도착노드, w: 연결된 간선의 가중치 
  graph[u].append((v, w))             # 거리 정보와 도착노드를 같이 입력합니다.


import heapq

def dijkstra(start):
  q = []
  heapq.heappush(q, (0, start)) # 우선순위, 값 형태로 들어간다.
  distance[start] = 0

  while q:
    dist, now = heapq.heappop(q) # 우선순위가 가장 낮은 값(가장 작은 거리)이 나온다.
    if distance[now] < dist: # 이미 입력되어있는 값이 현재노드까지의 거리보다 작다면 이미 방문한 노드이다.
      continue               # 따라서 다음으로 넘어간다.

    for i in graph[now]:     # 연결된 모든 노드 탐색
      if dist+i[1] < distance[i[0]]: # 기존에 입력되어있는 값보다 크다면
        distance[i[0]] = dist+i[1]   #
        heapq.heappush(q, (dist+i[1], i[0]))
dijkstra(k)
print(distance)
```
