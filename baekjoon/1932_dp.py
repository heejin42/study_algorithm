n = int(input())
nums = []
for i in range(n):
    nums.append(list(map(int, input().split(' '))))

for i in range(1, n):
    nums[i][0] = nums[i-1][0] + nums[i][0]
    for j in range(1, len(nums[i])-1):
        nums[i][j] = max(nums[i-1][j-1], nums[i-1][j]) +  nums[i][j]
    nums[i][-1] = nums[i-1][-1] + nums[i][-1]

print(max(nums[-1]))