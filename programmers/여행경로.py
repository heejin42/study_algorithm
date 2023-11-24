# 주어진 항공권을 모두 이용하여 여행 경로를 짤 때, 방문하는 공항 경로 리턴하는 문제
# 여러 경로가 있을 경우, 알파벳 순으로 빠른 경로를 리턴할 것
# 알파벳 순으로 dfs -> 재귀 함수로 구현하자.
from collections import deque
import copy
def solution(tickets):
    # 출발지는 ICN
    queue = deque([['ICN']])
    used = [0 for _ in range(len(tickets))]
    check = deque([used])
    tickets.sort()
    while queue:
        course = queue.popleft()
        used = check.popleft()
        if 0 not in used:
            return course
        last = course[-1]
        for i in range(len(tickets)):
            t_from, t_to = tickets[i]
            if used[i] == 0 and t_from == last:
                tmp_used = copy.deepcopy(used)
                tmp_used[i] = 1
                queue.append(course+[t_to])  
                check.append(tmp_used)   
    return []

tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
print(solution(tickets))
