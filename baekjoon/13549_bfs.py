from collections import deque
import sys
input = sys.stdin.readline

def solve():
    global n, k
    max_x = 100001
    graph = [0 for _ in range(max_x)]
    graph[n] = 1
    queue = deque([n])
    while queue:
        x = queue.popleft()
        if x == k:
            break
        for i in [2*x, x+1, x-1]:
            if 0 <= i < max_x and graph[i]==0:
                if i == 2*x:
                    queue.appendleft(i)
                    graph[i] = graph[x]
                else:
                    queue.append(i)
                    graph[i] = graph[x] + 1    
    print(graph[k]-1)



n, k = map(int, input().split(' '))
solve()