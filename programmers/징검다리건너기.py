# import copy
# def solution(stones, k): 
#     answer = -1
#     while True:
#         answer += 1
#         jump = copy.deepcopy(k)
#         for i in range(len(stones)):
#             if stones[i] > 0:
#                 stones[i] -= 1
#                 jump = copy.deepcopy(k)
#             else:
#                 if jump > 1:
#                    jump -= 1
#                 else:
#                     return answer

# 효율성 테스트 통과를 위해 이진탐색으로 풀자

def solution(stones, k):
    left = 1
    right = 200000000
    while left <= right:
        temp = stones.copy()
        mid = (left + right) // 2
        cnt = 0
        for t in temp:
            if t - mid <= 0:
                cnt += 1
            else:
                cnt = 0
            if cnt >= k:
                break
        if cnt >= k:
            right = mid - 1
        else:
            left = mid + 1
        
    return left

stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k = 3
print(solution(stones, k))