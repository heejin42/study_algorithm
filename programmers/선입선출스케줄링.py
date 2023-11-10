# 선입선출 스케줄링 문제
# 처리해야 할 작업이 50,000 이하의 n개, 코어의 처리 시간 cores
# CPU에는 여러 개의 코어가 있고, 코어 별로 처리 시간이 다르다. 2이상 10,000 이하
# 작업이 없는 코어 중 앞의 코어부터 작업 처리
# 마지막 작업을 처리하는 코어의 번호 return

# import heapq

# def solution(n, cores):
#     running_list = [(0, n) for n in range(len(cores))]
    
#     for i in range(n):
#         time, core = heapq.heappop(running_list)
#         heapq.heappush(running_list, (time+cores[core], core))  
              
#         if i == n-1:
#             return core+1          

def solution(n, cores):
    
    if n <= len(cores):
        return n
    else:
        n -= len(cores)
        left = 1
        right = max(cores) * n

        while left < right:
            mid = (left + right) // 2
            capacity = 0
            for c in cores:
                capacity += mid // c
            if capacity >= n:
                right = mid
            else:
                left = mid + 1

        for c in cores:
            n -= (right-1) // c

        for i in range(len(cores)):
            if right % cores[i] == 0:
                n -= 1
                if n == 0:
                    return i + 1
    
    

n = 6
cores = [1,2,3]
print(solution(n, cores))
