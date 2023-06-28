def solution(money):
    # 먼저 경우가 두가지 존재, 마지막집고 첫집 둘중 하나 터는 경우
    # 도둑이 털 수 있는 집 위치는 최소 한집 띄고
    # n-1, n-2 + now 중 큰 걸 선택해갈것
    dp1 = [0] * len(money)
    dp1[0] = money[0]
    dp1[1] = max(money[0], money[1])
    for i in range(2, len(money)-1):
        dp1[i] = max(dp1[i-1], dp1[i-2]+money[i])
        
    dp2 = [0] * len(money)
    dp2[0] = 0
    dp2[1] = money[1]
    for i in range(2, len(money)):
        dp2[i] = max(dp2[i-1], dp2[i-2]+money[i])
     
    return max(max(dp1), max(dp2))

money = [1, 2, 3, 1]
print(solution(money))