import sys
input = sys.stdin.readline

N, M = map(int, input().split(' '))
p = [[0]*(N+1) for _ in range(N+1)]
for n in range(1, N+1):
    arr = list(map(int, input().split(' ')))
    for i in range(1, len(arr)+1):
        p[n][i] = p[n][i-1] + p[n-1][i] - p[n-1][i-1] + arr[i-1]

for m in range(M):
    x1, y1, x2, y2 = map(int, input().split(' '))
    print(p[x2][y2] - p[x2][y1-1] - p[x1-1][y2] + p[x1-1][y1-1])

