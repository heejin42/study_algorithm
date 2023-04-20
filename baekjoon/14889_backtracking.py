import sys
input = sys.stdin.readline

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split(' '))))

visited = [False for _ in range(n)]   
result = 2e9

def solution(depth, idx):
    global graph, n, visited, result
    if depth == (n//2):
        start = 0
        link = 0
        for i in range(n):
            for j in range(i+1, n):
                if visited[i] and visited[j]:
                    start += (graph[i][j] + graph[j][i])
                elif not visited[i] and not visited[j]:
                    link += (graph[i][j] + graph[j][i])
        result = min(result, abs(start - link))
    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True 
            solution(depth+1, i+1)
            visited[i] = False
    
solution(0,0)
print(result)