# 가장 긴 감소하는 수열을 구하라
n = int(input())
arrA = list(map(int, input().split(' ')))

dp = [1 for _ in range(n)]
for i in range(n):
    for j in range(i):
        if arrA[j] > arrA[i]:
            dp[i] = max(dp[j] + 1, dp[i])
print(max(dp))