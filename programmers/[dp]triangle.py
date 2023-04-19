def solution(triangle):
    for i in range(1, len(triangle)):
        line = triangle[i]
        for j in range(len(line)):
            if j == 0:
                triangle[i][j] = triangle[i-1][0] + triangle[i][j]            
            elif j == (len(line)-1):
                triangle[i][j] = triangle[i-1][-1] + triangle[i][j]
            else:
                triangle[i][j] = max(triangle[i-1][j-1], triangle[i-1][j]) + triangle[i][j]
    answer = max(triangle[-1])
    return answer

triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]