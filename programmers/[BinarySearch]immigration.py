
def solution(n, times):
    answer = 0
    # 임의의 시간 x동안 심사 가능한 사람의 수는?
    left = times[0]
    right = times[-1] * n
    while left <= right:
        mid = (left + right) // 2
        checked = 0
        for time in times:
            checked += mid // time
            if checked >= n:
                break
        if checked >= n:
            answer = mid
            right = mid - 1
        elif checked < n:
            left = mid + 1
    return answer

n = 6	
times = [7, 10]
times.sort()
print(solution(n, times))