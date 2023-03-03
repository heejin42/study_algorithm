N = int(input())

def get_length(n):
    if dp[n]:
        return dp[n]
    else:
        if n < 3:
            dp[n] = 1
        else:
            dp[n] = get_length(n-2) + get_length(n-3)
        return dp[n]


for i in range(N):
    n = int(input())
    dp = [False]*n
    print(get_length(n-1))


    
