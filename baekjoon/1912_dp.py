# 백준 - 연속값 최대 구하기 (동적프로그래밍1)
import sys
N = int(input())
array = list(map(int, sys.stdin.readline().split(' ')))
dp = [0] * N
dp[0] = array[0]
for n in range(1, N):
    dp[n] = max(dp[n-1]+array[n], array[n])
    
print(max(dp))