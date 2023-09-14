def solution(k, d):
    # 양의 정수 k, d가 주어진다. > 1,000,000
    # (a*k, b*k) 위치에 점을 찍는다. 하지만 원점에서부터 거리가 d가 넘지 않게 한다.
    # 총 몇개의 점을 찍을 수 있는가?
    # 즉, d*d >= x^2 + y^2, x와 y인 k의 배수
    answer = 0
    
    for a in range(0, d+1, k):
        answer += (int((d**2 - a**2)**0.5))//k + 1
    return answer
        
k = 2
d = 4
print(solution(k, d))