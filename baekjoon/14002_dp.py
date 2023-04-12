import sys
input = sys.stdin.readline

def solve():
    global n, arr
    dp = [[0, []] for _ in range(n)]
    dp[0][0] = 1
    dp[0][1] = [arr[0]]
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                if dp[j][0] + 1 > dp[i][0]:
                    dp[i][0] = dp[j][0] + 1
                    dp[i][1] = dp[j][1] + [arr[i]] 
        if dp[i][0] == 0:
            dp[i][0] = 1
            dp[i][1] = [arr[i]]
            
    dp.sort(reverse = True)
    
    print(dp[0][0])
    for i in dp[0][1]:
        print(i, end = ' ')
    
n = int(input())
arr = list(map(int, input().split(' ')))
solve()