import sys

n, m = map(int, sys.stdin.readline().split(' '))
arr = [[0 for _ in range(m+1)]]
sum_arr = [[0 for _ in range(m+1)] for _ in range(n+1)]

for i in range(n):
    line = list(map(int, sys.stdin.readline().split(' ')))
    arr.append([0] + line)

for i in range(1, n+1):
	for j in range(1, m+1):
		sum_arr[i][j] = arr[i][j] + sum_arr[i-1][j] + sum_arr[i][j-1] - sum_arr[i-1][j-1]

k = int(sys.stdin.readline())
for _ in range(k):
    i, j, x, y = map(int, sys.stdin.readline().split(' '))
    answer = sum_arr[x][y] - sum_arr[i-1][y] - sum_arr[x][j-1] + sum_arr[i-1][j-1]
    print(answer)
    
                     