import sys
input = sys.stdin.readline

def solve():
    global n, arr
    start = 0
    end = n-1
    memo = [0] * n
    for target in n:
        start = 0
        end = target
        while start <= end:
            mid = (start + end) // 2
            if arr[mid] < arr[target]:
                memo[target] = max(memo[target], memo[mid]+1)
                start = mid + 1
            elif arr[mid] => arr[target]:
                
    # dp = [0] * n  
    # for i in range(n):
    #     if i == 0:
    #         dp[i] = 1
    #     else:
    #         for j in range(i):
    #             if arr[j] < arr[i]:
    #                 dp[i] = max(dp[i], dp[j]+1)
    print(max(dp))

n = int(input())
arr = list(map(int, input().split(' ')))
solve()