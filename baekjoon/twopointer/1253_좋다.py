# 시간 초과를 해결하기 위한 투포인터 풀이
# 2 3 4 4 5 5 6 9 10
n = int(input())
arr = list(map(int, input().split(' ')))
arr.sort()
answer = 0
for i in range(n):
    goal = arr[i]
    start = 0
    end = n-1  
    while start < end:
        if arr[start] + arr[end] == goal:
            if start == i:
                start += 1
            elif end == i:
                end -= 1
            else:
                answer += 1
                break
        elif arr[start] + arr[end] < goal:
            start += 1
        else: 
            end -= 1       
print(answer)

# from itertools import combinations
# n = int(input())
# arr = list(map(int, input().split(' ')))
# sum_list = list(combinations(arr, 2))
# for a,b in sum_list:
#     if a+b in arr:
#         arr.remove(a+b)
# print(n-len(arr))


# n = int(input())
# arr = list(map(int, input().split(' ')))
# sums = []
# goods = 0
# for i in range(n):
#     for j in range(i+1, n):
#         check_sum = arr[i] + arr[j]
#         if check_sum in arr and check_sum not in sums:
#             goods += 1
#             sums.append(check_sum)
# print(goods)