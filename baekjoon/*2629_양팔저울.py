import sys
input = sys.stdin.readline

wn = int(input().strip())
weights = list(map(int, input().strip().split(' ')))
bn = int(input().strip()) 
balls = list(map(int, input().strip().split(' ')))

dp = [[0]*(30*500+1) for _ in range(wn+1)] 

result = set()
def get_result(now, left, right):
    global wn, weights, bn, balls, dp, result
    new = abs(left - right)
    if new not in result:
        result.add(new)
    if now == wn:
        return 
    if dp[now][new] == 0:
        get_result(now+1, left + weights[now], right) # 왼쪽에 놓기
        get_result(now+1, left, right + weights[now]) # 오른쪽에 놓기
        get_result(now+1, left, right) # 놓지 않기
        dp[now][new] = 1
 
get_result(0, 0, 0)
for ball in balls:
    if ball in result:
        print("Y")
    else:
        print("N")