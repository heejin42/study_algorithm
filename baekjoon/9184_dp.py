def w(a, b, c):
    if a<=0 or b<=0 or c<=0:
        return 1
    elif a>20 or b>20 or c>20:
        return w(a, b, c)
    elif a<b and b<c:
        return w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
    else:
        return w(a-1, b, c)+ w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)

def dp_w(a, b, c):
    if a<=0 or b<=0 or c<=0:
        return 1
    if a>20 or b>20 or c>20:
        return dp_w(20, 20, 20)

    if dp[a][b][c]:
        return dp[a][b][c]
    elif a<b and b<c:
        dp[a][b][c] =  dp_w(a, b, c-1) + dp_w(a, b-1, c-1) - dp_w(a, b-1, c)
        return dp[a][b][c]
    else:
        dp[a][b][c] = dp_w(a-1, b, c) + dp_w(a-1, b-1, c) + dp_w(a-1, b, c-1) - dp_w(a-1, b-1, c-1)        
        return dp[a][b][c]
while True:        
    a, b, c = map(int, input().split(' '))
    if a == -1 and b == -1 and c == -1:
        break
    dp = [[[False] * 21 for _ in range(21)] for _ in range(21)]
    print("w({}, {}, {}) = {}".format(a,b,c,dp_w(a,b,c)))