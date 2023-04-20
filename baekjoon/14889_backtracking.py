import itertools
import sys
input = sys.stdin.readline

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split(' '))))

visited = [False for _ in range(n)]   

def solution(depth, id):
    global graph, n, visited
    if depth == (n//2):
        start = 0
        link = 0
        for i in range(n):
            for j in range(i+1, n):
                if visited[i] and visited[j]:
                    start += (array[i][j] + array[j][i])
                elif not visited[i] and not visited[j]:
                    link += (array[i][j] + array[j][i])
        result = min(result, abs(start - link))
        for i in range(idx, n):
            if nott visited[i]:
                visited[i] = True 
                solution(depth+1, i+1)
                visited[i] = False
    
solution(graph, n)
print(result)