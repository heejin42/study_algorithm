def getWays(n, c):
    m=len(c)
    c.sort()
    dp=[[0]*(n+1) for _ in range(m+1)]
    for i in range(m+1):
        dp[i][0]=1
    for i in range(1,m+1):
        for j in range(1,n+1):
            dp[i][j]=dp[i-1][j]
            for k in range(1,j//c[i-1]+1):
                dp[i][j]+=dp[i-1][j-k*c[i-1]]
    print(dp[-1][-1])
    return
    

n = 166
c = [5,37,8,39,33,17,22,32,13,7,10,35,40,2,43,49,46,19,41,1,12,11,28]

getWays(n, c)