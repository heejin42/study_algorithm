from collections import deque
def solution(n, number):
    dp = [[] for _ in range(9)]
    done = [n]
    num = n
    for i in range(1, 9):
        dp[i].append(num)
        i += 1
        num = int(str(n)*i) 
    for i in range(1, 8):
        for num in dp[i]:
            if not (num+n) in done:
                dp[i+1].append(num+n)
                done.append(num+n)
            if (not (num-n) in done) and (num-n > 0):
                dp[i+1].append(num-n) 
                done.append(num-n)
            if not (num//n) in done and (num//n > 0):
                dp[i+1].append(num//n)
                done.append(num//n)
            if not (num*n) in done:
                dp[i+1].append(num*n)
                done.append(num*n) 
        if number in dp[i+1]:
            return i+1
    return -1

N = 2
number = 11
print(solution(N, number))