def solution(n):
    # 거꾸로 2로 나누어지면서 구할까? 2로 안 나누어지면 점프
    # 이진수로 바꿨을 때 1의 개수라고도 할 수 있다.
    answer = 0 
    while n > 0:
        answer += n % 2
        n = n//2
    return answer

n = 5000
print(solution(n))