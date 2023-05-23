from collections import Counter
import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split(' ')))
nums_count = Counter(nums)

answer = [-1 for _ in range(n)]
stack = [0]

for i in range(1, n):
    target = nums[i]
    while stack and nums_count[target] > nums_count[nums[stack[-1]]]:
        x = stack.pop()
        answer[x] = nums[i]
    stack.append(i)
    
print(*answer)

    