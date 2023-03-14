import sys
input = sys.stdin.readline
n, m, k = map(int, input().split(' '))
p_1 = [[0]*(n+1) for _ in range(m+1)]

for i in range(1, m+1):
    arr = list(input())
    for j in range(1, n+1):
        if (i+j)%2 == 0 and arr[j-1] == 'B':
            p_1[i][j] = p_1[i-1][j] + p_1[i][j-1] - p_1[i-1][j-1]
        elif (i+j)%2 == 1 and arr[j-1] == 'W':
            p_1[i][j] = p_1[i-1][j] + p_1[i][j-1] - p_1[i-1][j-1]
        else:
            p_1[i][j] = p_1[i-1][j] + p_1[i][j-1] - p_1[i-1][j-1] + 1
    

min_ = float('inf')
max_ = -float('inf')
for r in range(k, n+1):
    for c in range(k, m+1):
        min_ = min(p_1[r][c] - p_1[r-k][c] - p_1[r][c-k] + p_1[r-k][c-k], min_)
        max_ = max(p_1[r][c] - p_1[r-k][c] - p_1[r][c-k] + p_1[r-k][c-k], max_)

print(min(min_, k*k-max_))