# 최소한의 다트로 0을 만드는 경우 중 -> 싱글 또는 불을 많이 맞춘 경우 -> 다트수 + 싱글불의 합

def solution(target):
    if target <= 20 or target == 50:
        return [1, 1]
    good = [i for i in range(1, 21)] + [50]
    soso = [2*i for i in range(1, 21)] + [3*i for i in range(1, 21)]
    soso = list(set(soso))
    soso.sort()
    # dp[i] = dp[i-soso] / dp[i][0] += 1
    # dp[i] = dp[i-good] / dp[i][0] += 1 , dp[i][1] += 1
    dp = [[100000, 0] for _ in range(target+1)]
    dp[0] = [0,0]
    for i in range(target+1):
        for j in good:
            if j > i:
                break
            if dp[i][0] > dp[i-j][0]+1:
                dp[i][0] = dp[i-j][0]+1
                dp[i][1] = dp[i-j][1]+1
            elif dp[i][0] == dp[i-j][0]+1:
                if dp[i][1] < dp[i-j][1]+1:
                    dp[i][1] = dp[i-j][1]+1
        for j in soso :
            if j > i:
                break
            if dp[i][0] > dp[i-j][0]+1:
                dp[i][0] = dp[i-j][0]+1
                dp[i][1] = dp[i-j][1]
            elif dp[i][0] == dp[i-j][0]+1:
                if dp[i][1] < dp[i-j][1]:
                    dp[i][1] = dp[i-j][1]
    answer = dp[target]
    return answer

target = 58
print(solution(target))