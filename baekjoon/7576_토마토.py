from collections import deque
import sys

def solve(arr):
    tomatoes = []
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                tomatoes.append((i,j))
    queue = deque(tomatoes)
    di = [-1, 0, 1, 0]
    dj = [0, -1, 0, 1]
    while queue:
        i, j = queue.popleft()
        for x in range(4):
            new_i = i + di[x]
            new_j = j + dj[x]
            if 0<=new_i<n and 0<=new_j<m and arr[new_i][new_j] == 0:
                arr[new_i][new_j] = arr[i][j] + 1
                queue.append((new_i, new_j))
    
    flag = False
    for tomatoes in arr:
        if 0 in tomatoes:
            flag = True
            break

    if flag:
        print(-1)
    else:
        print(max(map(max, arr))-1)
m = 6
n = 4
arr = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,1]]
solve(arr)