def solution(sticker):
    if len(sticker) <= 3:
        return max(sticker)
    
    # case 1 = 맨 앞 포함
    dp1 = [0 for _ in range(len(sticker))]
    dp1[0] = sticker[0]
    dp1[2] = sticker[0]+sticker[2]
    for i in range(3, len(sticker)-1):
        dp1[i] = max(dp1[i-1], dp1[i-2] + sticker[i], dp1[i-3]+sticker[i])
    
    # case 2 = 맨 앞 미포함
    dp2 = [0 for _ in range(len(sticker))]
    dp2[1] = sticker[1]
    dp2[2] = sticker[2]
    for i in range(3, len(sticker)):
        dp2[i] = max(dp2[i-1], dp2[i-2] + sticker[i], dp2[i-3]+sticker[i])
    answer = max(dp1[-2], dp2[-1])
    return answer

sticker = [14, 6, 5, 11, 3, 9, 2, 10] 
print(solution(sticker))