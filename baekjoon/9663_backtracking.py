# 백트래킹 알고리즘 N-Queen
N = int(input())
# 크기 n짜리 배열을 생성해준다. 퀸 위치 (1,2) -> arr[1] = 2
visited = [0]*(N+1)
arr = []
count = 0
# 조건 1 - 같은 열이나 행에 놓지 않는다.
# 조건 2 - 사선으로 같은 줄에 놓지 않는다. 
def dfs(n):
    global count
    if n == N+1:
        count += 1
        return
    for j in range(1, N+1):
        visited[n] = j
        flag = True
        for x in range(1, n):
            if visited[n]==visited[x] or (n-x == abs(visited[n]-visited[x])):
                flag = False
                break
        if flag:
            arr.append([n,j])
            dfs(len(arr)+1)
            arr.pop()

dfs(len(arr)+1)
print(count)
