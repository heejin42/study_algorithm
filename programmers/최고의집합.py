def solution(n,s):
    if n>s:
        return [-1]
    initial = s//n
    nums = [initial] * n
    print(nums)
    for i in range(1, s%n+1):
        nums[-i] += 1
    return nums

n = 2
s = 9
print(solution(n,s))