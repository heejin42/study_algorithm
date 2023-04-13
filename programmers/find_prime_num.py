import itertools

def is_prime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, n):
        if n%i == 0:
            return False
    return True

def solution(numbers):
    numbers = list(numbers)
    nums = []
    for i in range(1,len(numbers)+1):
        tmps = itertools.permutations(numbers, i)
        for tmp in tmps:
            nums.append(int(("").join(tmp)))
    nums = list(set(nums))
    answer = 0
    for num in nums:
        if is_prime(num):
            answer += 1
    return answer

numbers = "0117"
print(solution(numbers))