# 이분 탐색으로 풀어보자
def solution(diffs, times, limit):
    head = 0
    tail = max(diffs)
    answer = tail
    while head < tail:
        mid = (head + tail) // 2
        total_time = 0
        over_flag = False
        for i in range(len(diffs)):
            if diffs[i] <= mid:
                total_time += times[i]
            else:
                k = diffs[i] - mid
                total_time += (times[i] + times[i-1])*k + times[i]
            
            if total_time > limit:
                over_flag = True
                break
            
        if over_flag:
            head = mid + 1
        else:
            tail = mid
            answer = tail
    return answer

diffs = [1, 99999, 100000, 99995]
times = [9999, 9001, 9999, 9001]
limit = 3456789012
print(solution(diffs, times, limit))