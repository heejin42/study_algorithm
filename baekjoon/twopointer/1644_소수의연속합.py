def prime_nums(n):
    arr = [i for i in range(n+1)]
    for i in range(2, n+1):
        if arr[i] == 0:
            continue
        for j in range(i*i, n+1, i):
            arr[j] = 0
    return [i for i in arr[2:] if arr[i]]

n = int(input())
# 2~n 사이의 소수 리스트를 구하기
# 리스트에 투포인터로 합이 되는 경우 찾기
nums = prime_nums(n)
answer = 0
left = 0
right = 1

while left < right and right <= len(nums):
    if sum(nums[left:right]) == n:
        answer += 1
        left += 1
    elif sum(nums[left:right]) > n:
        left += 1
    elif sum(nums[left:right]) < n:
        right += 1
print(answer)
        
    