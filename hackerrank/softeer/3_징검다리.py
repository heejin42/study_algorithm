# 서쪽부터 동쪽으로 높아지게 돌을 밟아갈 때, 최대 개수는?
# dp로? 현재 위치까지 가장 많이 밟는 수는 자기보다 앞쪽, 낮은 돌의 dp값 최대 + 1

def solution(n, heights):
    #밟은개수, 높이
    dp = [(1, heights[0])]
    for i in range(1, n):
        # dp[:i] 정렬, 최대 지만 자기보다 작은 거 찾기, 없으면 1, heights[i]
        dp.sort(key = lambda x:(-x[0], x[1]))
        for x, h in dp[:i]:
            if h < heights[i]:
                dp.append((x+1, heights[i]))
                break
        if len(dp) == i:
            dp.append((1, heights[i]))
    dp.sort()
    return dp[-1][0]
                

n = int(input())
heights = list(map(int, input().split(' ')))
print(solution(n, heights))