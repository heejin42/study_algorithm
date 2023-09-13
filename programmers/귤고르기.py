def solution(k, tangerine):
    # tangerine 에서 k개를 고를 때 종류가 가장 적은 경우를 찾는 문제
    # 개수를 모두 count한 다음에 큰 것부터 k에서 뺄까?
    dic = {}
    for t in tangerine:
        if t in dic:
            dic[t] += 1
        else:
            dic[t] = 1
        
    total_list = list(dic.items())
    total_list.sort(reverse=True, key = lambda x:x[1])
    answer = 0
    count = 0
    for size, n in total_list:
        count += n
        answer += 1
        if count >= k:
            break
    return answer


k = 6
tangerine = [1, 3, 2, 5, 4, 5, 2, 3]
print(solution(k, tangerine))