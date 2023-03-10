import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split(' ')))
dp_1 = [1] * n
for i in range(1, n):
    for j in range(0, i):
        if arr[j] < arr[i]:
            dp_1[i] = max(dp_1[i], dp_1[j] + 1)

dp_2 = [1] * n
for i in range(n-2, -1, -1):
    for j in range(n-1, i, -1):
        if arr[j] < arr[i]:
            dp_2[i] = max(dp_2[i], dp_2[j] + 1)
dp = []
for i in range(n):
    dp.append(dp_1[i]+dp_2[i])

for i in range(n):
    dp.append(dp_1[i]+dp_2[i])

    today i 
print(max(dp)-1)
