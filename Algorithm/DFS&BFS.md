# DFS(깊이 우선 탐색) & BFS(넓이 우선 탐색)
bfs와 dfs는 그래프 탐색 알고리즘으로, 문제를 풀 때 상당히 많이 사용한다.

그래프란? 여러 개체들이 연결되어 있는 자료구조
탐색이란? 특정 개체를 찾는 것

대표적인 문제 유형
1. 경로 탐색 유형 (최단거리, 시간)
2. 네트워크 유형 (연결, 그룹 개수)
3. 조합 유형 (모든 조합 구하기)

상황에 맞게 DFS와 BFS 중 적절한 것을 선택해야 한다.

## DFS - 깊이 우선 탐색
루트 노트 혹은 임의의 노드에서 다음 브랜치로 넘어가기 전에 해당 브랜치를 최대한 깊게 탐색한다. 모든 경로를 구해야하는 경우에 적합하며 스택이나 재귀함수로 구현한다.

**예시**
function dfs(pos) {
    visit pos
    for children of pos:
        if visited[children] == False:
            dfs(children)
}

### 시간 복잡도
* 인접 행렬: O(V^2)
* 인접 리스트: O(V+E)



## BFS - 너비 우선 탐색
자신의 자식들부터 순차적으로 탐색하며, 순차 탐색 이후 다른 자식의 노드의 자식을 확인한다.
큐나 우선순위 큐(덱)을 이용해 구현하며, 가장 짧은 길이나 빠른 경로를 찾는데 적합하다.

**예시**
function bfs(pos){
    set q = queue
    q.append(pos)
    while q:
        set node = q.popleft()
        for children of pos:
            if visited[child] == False:
                visit child
                q.append(child)
}

### 시간 복잡도
* 인접 행렬: O(V^2)
* 인접 리스트: O(V+E)
