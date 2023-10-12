def solution(land):
    # n행 4열로 이루어진 땅따먹기 판, n<100,000
    # 1행부터 한 행씩 내려오면서 한칸만 밟을 수 있고, 같은 열을 밟을 수는 없다.
    # 최고점을 구할 것
    for i in range(1, len(land)):
        for j in range(4):
            land[i][j] += max(land[i-1][:j] + land[i-1][j+1:])
    return max(land[-1])

land = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]
print(solution(land))