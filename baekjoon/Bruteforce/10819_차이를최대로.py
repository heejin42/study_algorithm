# 연속된 수의 차이의 합을 최대로 하는 경우의 최댓값을 출력할 것
# 차이를 최대로? 
from itertools import permutations

n = int(input())
nums = list(map(int, input().split(' ')))
p = list(permutations(nums, n))

answer = 0
for nums in p:
    sum = 0
    for i in range(n-1):
        sum += abs(nums[i]-nums[i+1])
    answer = max(answer, sum)
print(answer)
