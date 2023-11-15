def solution(data,col,row_begin,row_end):
    # col번째 컬럼의 값을 기준으로 오름차순 정렬을 하되, 그 값이 동일하면 기본키를 기준으로 내림차순 정렬한다.
    # 정렬된 데이터에서 i번째 행의 튜플에 대해 각 컬럼 값을 i로 나눈 나머지들의 합을 구한다.
    # row_beginqnxj row_end까지의 합을 누적하여 bitwise XOR한 값을 해시 값으로 반환한다.
    answer = 0
    data.sort(key=lambda x:(x[col-1], -x[0]))
    for i in range(row_begin, row_end+1):
        target = data[i-1]
        s_i = 0
        for x in target:
            s_i += x%i 
        answer ^= s_i
    return answer

data = [[2,2,6],[1,5,10],[4,2,9],[3,8,3]]
col = 2
row_begin = 2
row_end = 3

print(solution(data,col,row_begin,row_end))