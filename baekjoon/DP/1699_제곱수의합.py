# n이 주어졌을 때, 제곱 수의 합으로 나타낼 수 있는 항의 최소개수
# dp[i] = i를 제곱수로 나타낼 수 있는 최소 항 개수
n = int(input())
dp = [i for i in range(n+1)]

for i in range(1, n+1):
    for j in range(1, i):
        if j*j > i:
            break
        dp[i] = min(dp[i], dp[i-j*j]+1)
print(dp[n])

