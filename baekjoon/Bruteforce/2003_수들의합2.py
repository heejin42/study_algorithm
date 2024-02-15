# 길이 N의 수열이 있을 떄, 수열의 일부 합이 M이 되는 경우의 수를 구하라
# 1 < n < 10,000

n, m = map(int, input().split(' '))
nums = list(map(int, input().split(' ')))
answer = 0
# for i in range(n):
#     sum_of_nums = nums[i]
#     for j in range(i+1, n):
#         if sum_of_nums == m:
#             answer += 1
#             break
#         elif sum_of_nums > m:
#             break
#         else:
#             sum_of_nums += nums[j]
# print(answer)

left = 0
right = 1
sum_of_nums = nums[0]
while True:
    if sum_of_nums == m:
        answer += 1
        sum_of_nums -= nums[left]
        left += 1
    elif sum_of_nums < m:
        if right >= n:
            break
        sum_of_nums += nums[right]
        right += 1
    else:
        sum_of_nums -= nums[left]
        left += 1
        
print(answer)
        
        
        