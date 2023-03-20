import sys

def solve():
    n, k = [int(x) for x in sys.stdin.readline().split()]
    dp = [[0]*(k+1) for _ in range(n+1)]
    things = [(0,0)]
    for i in range(n):
        w, v = [int(x) for x in sys.stdin.readline().split()]
        things.append((w,v))
    for i in range(1, n+1):
        for j in range(1, k+1):
            w = things[i][0]
            v = things[i][1]
            if w > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], v + dp[i-1][j-w])
        
    print(dp[n][k])
    
solve()