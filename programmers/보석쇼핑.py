# import copy
# def solution(gems):
#     # 진열된 모든 종류의 보석을 1개 이상 포함하는 짧은 구간 구매
#     # answer = [시작 번호, 끝 번호]
#     # gems 길이 1이상 100,000 이하
#     # 만약 각 위치마다 앞에 포함한 것을 체크한다면 n^2의 시간복잡도
#     # 
#     target = list(set(gems))
#     length = len(gems)
#     answer = [(length+1) for _ in range(length)]
#     for i in range(len(target)-1, len(gems)):
#         reset_target = copy.deepcopy(target)
#         for j in range(i, -1, -1):
#             if i-j > length:
#                 break
#             if gems[j] in reset_target:
#                 reset_target.remove(gems[j])
#                 if len(reset_target) == 0:
#                     answer[i] = i-j+1
#                     length = min(length, answer[i])
#                     break
#     end = answer.index(min(answer))
#     start = end - answer[end] + 1         
#     answer = [start+1, end+1]
#     return answer

def solution(gems):
    
    board = []
    n = len(board)
    
    for i in range(n):
        for j in ragne(n):
            if board[i][j] == 0:
                
    N = len(gems)
    answer = [0, N-1]
    kind = len(set(gems))  # 보석종류
    dic = {gems[0]:1,}  # 종류 체크할 딕셔너리
    s,e = 0,0  # 투포인터
    while s<N and e<N:
        if len(dic) < kind:  # 종류 부족하면 end point 증가 & dic 개수 증가
            e += 1
            if e == N:
                break
            dic[gems[e]] = dic.get(gems[e], 0) + 1
            
        else:  # 종류 같으면 ans 비교 후 답 갱신하고, start point 증가 & dic 개수 다운
            if (e-s+1) < (answer[1]-answer[0]+1):
                answer = [s,e]
            if dic[gems[s]] == 1:
                del dic[gems[s]]
            else:
                dic[gems[s]] -= 1
            s += 1

    answer[0] += 1
    answer[1] += 1
    return answer

gems = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
print(solution(gems))
