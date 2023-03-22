from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

lines = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split(' '))
    lines[u].append(v)
    lines[v].append(u)

visited = [False] * (n+1)
cnt = 0
def bfs(r):
    global cnt, visited, lines
    visited[r] = True
    queue = deque([r])
    while queue:
        x = queue.popleft()
        for num in lines[x]:
            if visited[num]:
                continue
            queue.append(num)
            cnt += 1
            visited[num] = True
        
bfs(1)
print(cnt)