# https://www.acmicpc.net/problem/1562
# 길이가 n이면서 0~9 가 모두 들어가는 계단수 개수를 구하라
# 비트 마스킹, DP

import sys
mod = 1000000000
n = int(sys.stdin.readline())
dp = [[[-1]*11] for _ in range(10)]
for i in range(1, 11):
    dp[i]





