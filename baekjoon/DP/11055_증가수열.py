def solution(arrA):
    dp = [0 for _ in range(len(arrA))]
    dp[0] = arrA[0]
    for i in range(len(arrA)):
        for j in range(i):
            if arrA[j] < arrA[i]:
                dp[i] = max(dp[i], dp[j] + arrA[i])
            else:
                dp[i] = max(dp[i], arrA[i])
    return max(dp)
    

n = int(input())
arrA = list(map(int, input().split(' ')))
print(solution(arrA))