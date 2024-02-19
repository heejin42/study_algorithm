# 행렬 w[i][j]는 i에서 j로 가기 위한 비용이다. 갈 수 없으면 0
# 가장 적은 비용의 순회 여행 경로를 구하라
# n <= 10
def dfs(x, val, depth=1):
    global cost
    global first
    global n

    if depth == n:
        for nx, _cost in graph[x]:
            if nx == first:
                cost = min(cost, val+_cost)
        return

    if visit[x]:
        return

    visit[x] = True

    for nx, _cost in graph[x]:
        if not visit[nx]:
            dfs(nx, val+_cost, depth+1)
            visit[nx] = False


n = int(input())
graph = [[] for _ in range(n)]
cost = float('inf')

for i in range(n):
    arr = list(map(int, input().split()))
    for j in range(n):
        if i == j or arr[j] == 0: continue
        graph[i].append((j, arr[j]))

for i in range(n):
    visit = [False] * n
    first = i
    dfs(i, 0)

print(cost)


