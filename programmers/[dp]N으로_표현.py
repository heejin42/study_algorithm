from collections import deque
def solution(n, number):
    dp = [[] for _ in range(9)]
    for i in range(1, 9):
        dp[i].append(int(str(n)*i))
        for j in range(1, i):
            for a in dp[j]:
                for b in dp[i-j]:
                    dp[i].append(a+b)
                    dp[i].append(a-b)
                    if b != 0:
                        dp[i].append(a//b)
                    dp[i].append(a*b)
        if number in dp[i]:
            return i
    return -1
    
    
    
N = 5
number = 12
print(solution(N, number))