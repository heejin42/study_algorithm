# 회전판에 n개의 음식이 있다. 각 음식을 먹는 데에 일정 시간이 걸린다.
# 무지는 1번부터 시작해 회전판이 돌아가며 앞에 오는 음식을 1초씩 먹게 된다.
# 마지막 번호 -> 1번
# 여기서 다음 음식이란 아직 남은 음식 중 가장 가까운 번호의 음식, 돌리는 시간은 없다.
# 시작해서 k초 후에 몇번 음식을 먹는지 구하라
from collections import deque

def solution(food_times, k):
    answer = 0
    q = deque(food_times)
    for _ in range(k+1):
        if len(q) == 0:
            f = -1
            break
        f = q.popleft()
        food_times[f-1] -= 1
        if food_times[f-1] == 0:
            continue
        else:
            q.append(f)
    answer = f
    return answer

food_times = [3, 1, 2]
k = 5
print(solution(food_times, k))