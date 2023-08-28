# k진법으로 나눈다 -> 0을 기준으로 나눈다 -> 각각의 숫자가 소수인지 아닌지 체크
def isprime(k):
    if k == 2 or k == 3: return True
    if k % 2 == 0 or k < 2: return False 
    for i in range(3, int(k ** 0.5) + 1, 2):
        if k % i == 0:
            return False
    return True


def solution(n, k):
    answer = 0
    word = ''
    while n > 0:
        word = str(n%k)+word
        n = n//k
    nums = word.split('0')
    for num in nums:
        if len(num) == 0 or int(num) < 2:
            continue
        else:
            if isprime(int(num)):
                answer += 1
    return answer



n = 437674
k = 3
print(solution(n,k))