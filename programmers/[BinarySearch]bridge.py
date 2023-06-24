def solution(distance, rocks, n):
    rocks.sort()
    answer = 0
    start, end = 0, distance
    rocks.append(distance)
    while start <= end:
        mid = (start + end) // 2
        count_stone = 0
        pre_stone = 0
        min_distance = float('inf')
        for rock in rocks:
            dis = rock - pre_stone
            if  dis < mid:
                count_stone += 1
            else:
                pre_stone = rock
                min_distance = min(min_distance, dis)
            
        if count_stone > n:
            end = mid - 1
        else:
            answer = min_distance
            start = mid + 1
    return answer
    
distance = 25
rocks = [2, 14, 11, 21, 17]
rocks.sort()
n = 2
print(solution(distance, rocks, n))