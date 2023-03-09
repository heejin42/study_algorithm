import sys
n = int(sys.stdin.readline())
arr = []
for i in range(n):
    arr.append(int(sys.stdin.readline()))

dp = [0] * n


for i in range(0, n):
    if i == 0:
        dp[i] = arr[i]
    elif i == 1:
        dp[i] = dp[i-1] + arr[i]
    else:
        a = dp[i-1]
        b = dp[i-2] + arr[i]
        c = dp[i-3] + arr[i-1] + arr[i]
        dp[i] = max(a,b,c)

print(dp[-1])