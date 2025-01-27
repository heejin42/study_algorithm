n = int(input())
children = []
for _ in range(n):
    children.append(int(input()))
    
# 가장 긴 증가 수열의 길이를 구하면, 그 수열의 수는 순서에 맞게 자리는 수, 나머지가 최소 횟수가 된다.
dp = [1 for _ in range(n)]
for i in range(1, n):
    for j in range(i):
        if children[j] <= children[i]:
            dp[i] = max(dp[i], dp[j]+1)
print(n - max(dp))