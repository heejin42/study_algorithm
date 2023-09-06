def solution(storey):
    # storey < 100,000,000
    # -1 +1 -10 +10 -100 +100 등 가능
    # 0층으로 가기 위한 가장 빠른 길
    # 각각의 위치에서 1000으로 떨어지는 수 중 가장 가까운 수 -> 100으로 떨어지는 수 중 가장 가까운수 =
    answer = 0
    while storey:
        remainder = storey % 10
        # 6 ~ 9
        if remainder > 5:
            answer += (10 - remainder)
            storey += 10
        # 0 ~ 4
        elif remainder < 5:
            answer += remainder
        # 5
        else:
            if (storey // 10) % 10 > 4:
                storey += 10
            answer += remainder
        storey //= 10
                
    return answer

storey = 2554
print(solution(storey))