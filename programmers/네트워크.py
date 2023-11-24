# 컴퓨터의 개수 n과 연결에 대한 정보 n*n 이차원 배열
# 네트워크의 개수를 구하라 -> 후보 중 하나 선택 -> dfs 해서 연결된 모든 컴퓨터 확인

def visit(i, computers, visited):
    visited[i] = 1
    for j in range(len(visited)):
        if visited[j] == 0 and computers[i][j] == 1:
            visit(j, computers, visited)
            
def solution(n,computers):
    answer = 0
    visited = [0 for _ in range(n)]
    for i in range(n):
        if visited[i] == 0:
            visit(i, computers, visited)
            answer += 1
        if 0 not in visited:
            break
    return answer
        

n = 3
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
print(solution(n, computers))