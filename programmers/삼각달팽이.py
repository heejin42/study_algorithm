def solution(n):
    # 초기 삼각형 생성
    tri = [[0 for j in range(1,i+1)] for i in range(1,n+1) ]
    x,y = -1,0 # 시작 좌표
    num = 1    # 시작값

    for i in range(n): # n번 반복
        for j in range(i,n): # n,n-1,...,1
            if i % 3 == 0: # 아래로
                x += 1
            elif i % 3 == 1: # 오른쪽으로
                y += 1
            else: # 위로
                x -= 1
                y -= 1
            tri[x][y] = num # 값 갱신
            num += 1 # 다음 값
            
    return sum(tri,[])

n = 4
print(solution(n))