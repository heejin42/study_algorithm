from collections import deque
def bfs(graph, start):
    visited = [False] * (len(graph)+1)
    queue = deque([start])
    visited[start] = True
    while queue:
        now = queue.popleft()
        for next in graph[now]:
            if not visited[next]:
                queue.append(next)
                visited[next] = True
    return visited.count(True)
        

def solution(n, wires):
    answer = 2e9
    graph = [[] for _ in range(n+1)]
    for a,b in wires:
        graph[a].append(b)
        graph[b].append(a)
        
    for a,b in wires:
        graph[a].remove(b)
        graph[b].remove(a)
        answer = min(answer, abs(bfs(graph, a) - bfs(graph, b)))
        graph[a].append(b)
        graph[b].append(a)
    return answer

n = 9
wires = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]
print(solution(n, wires))