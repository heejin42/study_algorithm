n = int(input())
graph = []
max_height = 0
min_height = 101 
for _ in range(n):
    line = list(map(int, input().split(' ')))
    max_height = max(max_height, max(line))
    min_height = min(min_height, min(line))
print(graph)

count_safezone = 0
for rain in range(min_height, max_height):
    visited = [0 for _ in range(n*n)]
    safezone =
    
# safezone 체크는 dfs()