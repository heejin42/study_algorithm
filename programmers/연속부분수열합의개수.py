# 원형 수열이라고 가정했을 때, 부분 수열의 합의 개수를 구하라


def solution(elements):
    n = len(elements)
    sums = [sum(elements)]
    # dp[i][j] = i부터 j개의 합
    # 0 0,1 0,1,2 0,1,2,3,4
    # 1 1,2 1,2,3 1,2,3,4,0
    for i in range(n):
        dp = [elements[i] for _ in range(n)]
        for j in range(1, n):
            if i+j >= n:
                dp[j] = dp[j-1] + elements[i+j-n]
            else:
                dp[j] = dp[j-1] + elements[i+j]
        sums += dp
    sums = list(set(sums))
    answer = len(sums)
    return answer

elements = [7,9,1,1,4]
print(solution(elements))