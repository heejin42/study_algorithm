n = int(input())
arr = [[0,1,1,1,1,1,1,1,1,1] for _ in range(n)]
for i in range(1, n):
    arr[i][0] = arr[i-1][1]
    for j in range(1, 9):
        arr[i][j] = arr[i-1][j+1] + arr[i-1][j-1]
    arr[i][9] = arr[i-1][8]

print(sum(arr[-1])%1000000000)

