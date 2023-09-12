from collections import defaultdict
from itertools import combinations_with_replacement
def solution(k,n,reqs):
    # n 명의 멘토, k개의 상담 유형, reqs의 상담 요청
    # req의 형식 = 시각, 시간, 유형
    # 대기 시간을 가장 짧게 만드는 유형별 멘토 정리 (최소 유형별 1명씩 있어야 된다.)
    # 1 ≤ k ≤ 5, k ≤ n ≤ 20, 3 ≤ reqs의 길이 ≤ 300
    # 먼저 k개 유형에 멘토를 지정해준다. 최소 1명 이상
    answer = 999999999
    comb = combinations_with_replacement([i for i in range(k)], r=n-k)
    cases = []
    for case in comb:
        base = [1 for i in range(k)]
        for c in case:
            base[c] += 1
        cases.append(base)

    participants = defaultdict(list)
    for start_time, minutes, category in reqs:
        participants[category].append([start_time, start_time + minutes])
    
    for case in cases:
        wait_time = 0
        for i in range(1, k+1):
            p_list = sorted(participants[i], key=lambda x:x[0])
            mento_list = [0 for i in range(case[i-1])]
            for start, end in participants[i]:
                mento_list.sort()
                if mento_list[0] <= start:
                    mento_list[0] = end
                else:
                    wait = mento_list[0]-start
                    mento_list[0] = end + wait
                    wait_time += wait
            if wait_time > answer:
                break
        answer = min(answer, wait_time)
    return answer

k = 3
n = 5
reqs = [[10, 60, 1], [15, 100, 3], [20, 30, 1], [30, 50, 3], [50, 40, 1], [60, 30, 2], [65, 30, 1], [70, 100, 2]]
print(solution(k,n,reqs))