import sys
n = int(input())
arr = []
for i in range(n):
    a, b = map(int, sys.stdin.readline().split(' '))
    arr.append([a,b])

arr.sort()
dp = [1] * n
for i in range(n):
    if i == 0:
        continue
    for j in range(i):
        if arr[i][1] > arr[j][1]:
            dp[i] = max(dp[i], dp[j]+1)

print(n - max(dp))

