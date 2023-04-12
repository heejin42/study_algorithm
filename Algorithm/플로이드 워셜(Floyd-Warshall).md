## 플로이드 워셜(Floyd-Warshall)
플로이드 워셜 알고리즘은 모든 노드에서 다른 모든 노드까지의 최단 경로를 계산하는 알고리즘으로, 다익스트라 알고리즘과 마찬가지로 단계별로 거쳐 가는 노드를 기준으로 진행된다.
다만 매 단계마다 방문하지 않은 노드 중에 최단 거리의 노드를 찾는 과정은 필요하지 않다.
다이나믹 프로그래밍 유형에 속하며 2차원 테이블에 최단 거리 정보를 저장한다.

### 알고리즘 동작 과정
0. 그래프를 준비하고 최단 거리 테이블(2차원 배열)을 초기화한다.
(img)[https://blog.kakaocdn.net/dn/c0b3mJ/btqSmzRxbKw/AFr6HNli1JPcRkicbZ8uM0/img.png]

1. 시작 노드인 1번 노드를 거쳐 가는 경우를 고려하여 테이블을 갱신한다.
(img)[https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FpGzgI%2FbtqSpGpfTGj%2F9M53sB6KMk5Tdio0Aryxmk%2Fimg.png]

2. 2번 노드를 거쳐 가는 경우를 고려하여 테이블을 갱신한다.
(img)[https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbO0GVm%2FbtqSsQSEsmc%2FFsgbpWf2y2RgtrspEAQkN0%2Fimg.png]

3. 3번 노드를 거쳐 가는 경우를 고려하여 테이블을 갱신한다.
(img)[https://blog.kakaocdn.net/dn/OgWop/btqSEKcIr8X/zW44u4yRK0JimbeDub1N70/img.png]

4. 3번 노드를 거쳐 가는 경우를 고려하여 테이블을 갱신한다.
(img)[https://blog.kakaocdn.net/dn/7Lyb9/btqSgLZbDeP/AfiK6gyoNAwdZ6s4wEqSKk/img.png]


### 예시 코드 - 파이썬
```python
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수 및 간선의 개수를 입력받기
n = int(input())
m = int(input())
# 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력 받아, 그 값으로 초기화
for _ in range(m):
    # A에서 B로 가는 비용은 C라고 설정
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과를 출력
for a in range(1, n + 1):
    for b in range(1, n + 1):
        # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
        if graph[a][b] == 1e9:
            print("INFINITY", end=" ")
        # 도달할 수 있는 경우 거리를 출력
        else:
            print(graph[a][b], end=" ")
    print()
```
