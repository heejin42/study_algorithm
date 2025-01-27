def dfs(visited, lighthouse, answer):
    if len(lighthouse) == 0:
        answer = min(answer, visited.count(1))
        return answer
    
    a, b = lighthouse[0]
    if visited[a] == 1 or visited[b] == 1:
        answer = dfs(visited, lighthouse[1:], answer)
    else:
        visited[a] = 1
        answer = dfs(visited, lighthouse[1:], answer)
        visited[a] = 0
        visited[b] = 1
        answer = dfs(visited, lighthouse[1:], answer)
        visited[b] = 0
    return answer
        
        

def solution(n, lighthouse):
    answer = n
    visited = [0 for _ in range(n+1)]
    answer = dfs(visited, lighthouse, answer)
    return answer

n = 8
lighthouse = [[1, 2], [1, 3], [1, 4], [1, 5], [5, 6], [5, 7], [5, 8]]
print(solution(n, lighthouse))

