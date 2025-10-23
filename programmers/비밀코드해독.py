# 1부터 n까지의 서로 다른 정수 5개가 오름차순으로 정렬되어 있음
# m번 시도로 얻은 응답이 주어질 때, 비밀 코드로 가능한 정수 조합 개수를 return
from itertools import combinations

def solution(n, q, ans):
    answer = 0
    nums = [x for x in range(1, n+1)]
    candidates = list(combinations(nums, 5))
    for candidate in candidates:
        flag = True
        for i in range(len(q)):
            cnt = 0
            for n in q[i]:
                if n in candidate:
                    cnt += 1
            if cnt != ans[i]:
                flag = False
                break
        if flag:
            answer += 1
    return answer

n = 10
q = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [3, 7, 8, 9, 10], [2, 5, 7, 9, 10], [3, 4, 5, 6, 7]]
ans = [2, 3, 4, 3, 3]
print(solution(n, q, ans))