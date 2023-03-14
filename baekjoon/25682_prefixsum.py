import sys
input = sys.stdin.readline
n, m, k = map(int, input().split(' '))
p = [[0]*(m+1) for _ in range(n+1)]

for i in range(1, n+1):
    arr = list(input())
    for j in range(1, m+1):
        if (i+j)%2 == 0 and arr[j-1] == 'B':
            p[i][j] = p[i-1][j] + p[i][j-1] - p[i-1][j-1]
        elif (i+j)%2 == 1 and arr[j-1] == 'W':
            p[i][j] = p[i-1][j] + p[i][j-1] - p[i-1][j-1]
        else:
            p[i][j] = p[i-1][j] + p[i][j-1] - p[i-1][j-1] + 1
    

min_ = float('inf')
max_ = -float('inf')
for r in range(k, n+1):
    for c in range(k, m+1):
        min_ = min(p[r][c] - p[r-k][c] - p[r][c-k] + p[r-k][c-k], min_)
        max_ = max(p[r][c] - p[r-k][c] - p[r][c-k] + p[r-k][c-k], max_)

print(min(min_, max_, k*k-min_, k*k-max_))