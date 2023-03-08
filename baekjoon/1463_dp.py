# 백준 - 1로 만들기 (동적프로그래밍1)
n = int(input())
arr = [n]*(n+1)
arr[n] = 0
for i in range(n-1, 0, -1):
    if i * 3 <= n:
        arr[i] = min(arr[i*3], arr[i*2], arr[i+1]) + 1
    elif i * 2 <= n and i*3 > n:
        arr[i] = min(arr[i*2], arr[i+1]) + 1
    elif i * 2 > n:
        arr[i] = arr[i+1] + 1

print(arr[1])