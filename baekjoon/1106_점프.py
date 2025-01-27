n = int(input())
arr = list(map(int, input().split(' ')))
dp = [1000 for _ in range(n)]
dp[0] = 0
for i in range(n):
    for j in range(1, arr[i]+1):
        if i+j < n:
            dp[i+j] = min(dp[i+j], dp[i]+1)
                    
if dp[-1] == 1000:
    print(-1)
else:
    print(dp[-1])