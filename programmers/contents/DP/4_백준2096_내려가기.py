# 맨 윗줄에서 맨 아랫줄로 이동 -> 아래칸이나 사선 칸으로 이동 가능
# 최소값 최대값 구할 것
import sys
input = sys.stdin.readline
n = int(input().rstrip())
board = list(map(int, input().rstrip().split(' ')))
max_dp = board
min_dp = board
for _ in range(n-1):
    board = list(map(int, input().rstrip().split(' ')))
    max_dp = [max(max_dp[:2])+board[0], max(max_dp)+board[1], max(max_dp[1:])+board[2]]
    min_dp = [min(min_dp[:2])+board[0], min(min_dp)+board[1], min(min_dp[1:])+board[2]]    
print(max(max_dp), min(min_dp))