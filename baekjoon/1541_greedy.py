import sys

S = list(map(str, sys.stdin.readline().split('-')))
nums = []
for s in S:
    if '+' in s:
        tmp = list(map(int, s.split('+')))
        nums.append(sum(tmp))
    else:
        nums.append(int(s))

sum_ = nums[0]
for num in nums[1:]:
    sum_ -= num

print(sum_)