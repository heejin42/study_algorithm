def solution(n):
    cnt = bin(n).count('1')
    # n보다 큰 자연수, 이진수로 변환했을 때 1의 갯수가 같은 수 중 가장 작은 수
    while True:
        n += 1
        if bin(n).count("1") == cnt:
            return n
n = 78 
print(solution(n))